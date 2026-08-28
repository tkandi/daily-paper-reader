#!/usr/bin/env python3
"""Install, inspect, or recoverably uninstall DPR launchd jobs on macOS."""

from __future__ import annotations

import argparse
import datetime as dt
import os
import plistlib
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT_DIR = Path(__file__).resolve().parents[1]
WEB_LABEL = "com.tkandi.daily-paper-reader.web"
DAILY_LABEL = "com.tkandi.daily-paper-reader.daily"


def launch_agents_dir(home: Path) -> Path:
    return home / "Library" / "LaunchAgents"


def log_dir(root: Path) -> Path:
    return root / ".local-runs" / "launchd"


def common_environment(root: Path) -> dict[str, str]:
    return {
        "DPR_DOTENV_PATH": str(root / ".env"),
        "PYTHONUNBUFFERED": "1",
        "PATH": "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin",
    }


def build_web_plist(root: Path, *, host: str, port: int) -> dict[str, Any]:
    logs = log_dir(root)
    return {
        "Label": WEB_LABEL,
        "ProgramArguments": [
            str(root / ".venv" / "bin" / "python"),
            str(root / "src" / "local_debug_server.py"),
            "--host",
            host,
            "--port",
            str(port),
        ],
        "WorkingDirectory": str(root),
        "EnvironmentVariables": common_environment(root),
        "RunAtLoad": True,
        "KeepAlive": True,
        "ProcessType": "Background",
        "StandardOutPath": str(logs / "web.stdout.log"),
        "StandardErrorPath": str(logs / "web.stderr.log"),
    }


def build_daily_plist(root: Path, *, hour: int, minute: int) -> dict[str, Any]:
    logs = log_dir(root)
    return {
        "Label": DAILY_LABEL,
        "ProgramArguments": ["/bin/zsh", str(root / "scripts" / "run_local_daily.sh")],
        "WorkingDirectory": str(root),
        "EnvironmentVariables": common_environment(root),
        "StartCalendarInterval": {"Hour": int(hour), "Minute": int(minute)},
        "ProcessType": "Background",
        "StandardOutPath": str(logs / "daily.stdout.log"),
        "StandardErrorPath": str(logs / "daily.stderr.log"),
    }


def _launchctl(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["/bin/launchctl", *args],
        check=check,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def _write_plist(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as handle:
        plistlib.dump(payload, handle, sort_keys=False)
    os.chmod(path, 0o600)


def install(args: argparse.Namespace) -> int:
    root = args.root.expanduser().resolve()
    home = args.home.expanduser().resolve()
    python = root / ".venv" / "bin" / "python"
    if not python.exists():
        raise SystemExit("缺少 .venv；请先运行 scripts/bootstrap_local.sh --prepare-only")
    if not (root / ".env").exists():
        raise SystemExit("缺少 .env；请先运行 scripts/configure_local_cliproxyapi.py")
    logs = log_dir(root)
    logs.mkdir(parents=True, exist_ok=True)
    agent_dir = launch_agents_dir(home)
    web_path = agent_dir / f"{WEB_LABEL}.plist"
    daily_path = agent_dir / f"{DAILY_LABEL}.plist"
    _write_plist(web_path, build_web_plist(root, host=args.host, port=args.port))
    _write_plist(daily_path, build_daily_plist(root, hour=args.hour, minute=args.minute))

    domain = f"gui/{os.getuid()}"
    for label, path in ((WEB_LABEL, web_path), (DAILY_LABEL, daily_path)):
        _launchctl("bootout", f"{domain}/{label}", check=False)
        result = _launchctl("bootstrap", domain, str(path), check=False)
        if result.returncode != 0:
            raise SystemExit(f"加载 {label} 失败：{result.stdout.strip()}")
    print(f"已安装本地网页：http://{args.host}:{args.port}")
    print(f"已安装每日本地任务：{args.hour:02d}:{args.minute:02d}")
    print(f"LaunchAgent 日志：{logs}")
    return 0


def status(args: argparse.Namespace) -> int:
    domain = f"gui/{os.getuid()}"
    failed = False
    for label in (WEB_LABEL, DAILY_LABEL):
        result = _launchctl("print", f"{domain}/{label}", check=False)
        if result.returncode == 0:
            first_lines = "\n".join(result.stdout.splitlines()[:12])
            print(f"[{label}] loaded\n{first_lines}")
        else:
            print(f"[{label}] not loaded")
            failed = True
    return 1 if failed else 0


def uninstall(args: argparse.Namespace) -> int:
    home = args.home.expanduser().resolve()
    domain = f"gui/{os.getuid()}"
    trash = home / ".Trash"
    trash.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    for label in (WEB_LABEL, DAILY_LABEL):
        _launchctl("bootout", f"{domain}/{label}", check=False)
        path = launch_agents_dir(home) / f"{label}.plist"
        if path.exists():
            target = trash / f"{label}.{stamp}.plist"
            shutil.move(str(path), str(target))
            print(f"已移至废纸篓：{target}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="管理 Daily Paper Reader 本地 LaunchAgent")
    parser.add_argument("--root", type=Path, default=ROOT_DIR)
    parser.add_argument("--home", type=Path, default=Path.home())
    sub = parser.add_subparsers(dest="command", required=True)
    install_parser = sub.add_parser("install")
    install_parser.add_argument("--host", default="127.0.0.1")
    install_parser.add_argument("--port", type=int, default=8567)
    install_parser.add_argument("--hour", type=int, default=2)
    install_parser.add_argument("--minute", type=int, default=30)
    install_parser.set_defaults(func=install)
    status_parser = sub.add_parser("status")
    status_parser.set_defaults(func=status)
    uninstall_parser = sub.add_parser("uninstall")
    uninstall_parser.set_defaults(func=uninstall)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if getattr(args, "hour", 0) not in range(24) or getattr(args, "minute", 0) not in range(60):
        parser.error("hour/minute 超出范围")
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
