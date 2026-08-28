#!/usr/bin/env python3
"""Deploy a clean runtime checkout outside macOS protected Desktop/Documents paths."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
from pathlib import Path


SOURCE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DESTINATION = Path.home() / "Services" / "daily-paper-reader"
PRIVATE_FILES = (".env", "secret.private")


def run(*args: str, cwd: Path | None = None, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(args),
        cwd=str(cwd) if cwd else None,
        check=check,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def git_text(root: Path, *args: str) -> str:
    return run("git", *args, cwd=root).stdout.strip()


def validate_source(root: Path) -> tuple[str, str]:
    if not (root / ".git").exists():
        raise SystemExit(f"源目录不是 Git 仓库：{root}")
    dirty = git_text(root, "status", "--porcelain")
    if dirty:
        raise SystemExit("源仓库存在未提交改动；请先完成测试并提交，再部署稳定运行副本")
    branch = git_text(root, "branch", "--show-current")
    if not branch:
        raise SystemExit("源仓库当前处于 detached HEAD，无法部署")
    origin = git_text(root, "remote", "get-url", "origin")
    return branch, origin


def is_macos_protected_user_path(path: Path, home: Path | None = None) -> bool:
    user_home = (home or Path.home()).expanduser().resolve()
    resolved = path.expanduser().resolve()
    return any(parent == resolved or parent in resolved.parents for parent in (
        user_home / "Desktop",
        user_home / "Documents",
        user_home / "Downloads",
    ))


def clone_or_fast_forward(source: Path, destination: Path, branch: str, origin: str) -> None:
    if not destination.exists():
        destination.parent.mkdir(parents=True, exist_ok=True)
        result = run(
            "git",
            "clone",
            "--local",
            "--no-hardlinks",
            "--branch",
            branch,
            str(source),
            str(destination),
            check=False,
        )
        if result.returncode != 0:
            raise SystemExit(f"创建运行副本失败：{result.stdout.strip()}")
        run("git", "remote", "set-url", "origin", origin, cwd=destination)
        run("git", "remote", "add", "deployment-source", str(source), cwd=destination)
        return

    if not (destination / ".git").exists():
        raise SystemExit(f"目标已存在但不是 Git 仓库，拒绝覆盖：{destination}")
    remotes = git_text(destination, "remote").splitlines()
    if "deployment-source" not in remotes:
        run("git", "remote", "add", "deployment-source", str(source), cwd=destination)
    else:
        run("git", "remote", "set-url", "deployment-source", str(source), cwd=destination)
    result = run("git", "fetch", "deployment-source", branch, cwd=destination, check=False)
    if result.returncode != 0:
        raise SystemExit(f"读取源分支失败：{result.stdout.strip()}")
    result = run("git", "merge", "--ff-only", "FETCH_HEAD", cwd=destination, check=False)
    if result.returncode != 0:
        raise SystemExit(
            "运行副本无法快进更新；请先处理其中的提交或冲突。\n" + result.stdout.strip()
        )


def sync_private_files(source: Path, destination: Path, *, force: bool) -> None:
    for name in PRIVATE_FILES:
        src = source / name
        dst = destination / name
        if not src.exists() or (dst.exists() and not force):
            continue
        shutil.copy2(src, dst)
        if name == ".env":
            os.chmod(dst, 0o600)


def prepare_runtime(destination: Path, *, skip_deps: bool) -> None:
    env = os.environ.copy()
    if skip_deps:
        env["DPR_SKIP_INSTALL"] = "1"
    result = subprocess.run(
        [str(destination / "scripts" / "bootstrap_local.sh"), "--prepare-only"],
        cwd=str(destination),
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if result.returncode != 0:
        raise SystemExit(f"运行环境准备失败：\n{result.stdout}")
    print(result.stdout.rstrip())


def install_launchagents(destination: Path, *, host: str, port: int, hour: int, minute: int) -> None:
    result = run(
        str(destination / ".venv" / "bin" / "python"),
        str(destination / "scripts" / "manage_local_launchagents.py"),
        "--root",
        str(destination),
        "install",
        "--host",
        host,
        "--port",
        str(port),
        "--hour",
        str(hour),
        "--minute",
        str(minute),
        cwd=destination,
        check=False,
    )
    if result.returncode != 0:
        raise SystemExit(f"LaunchAgent 安装失败：\n{result.stdout}")
    print(result.stdout.rstrip())


def main() -> int:
    parser = argparse.ArgumentParser(description="部署 Daily Paper Reader 本地运行副本")
    parser.add_argument("--source", type=Path, default=SOURCE_ROOT)
    parser.add_argument("--destination", type=Path, default=DEFAULT_DESTINATION)
    parser.add_argument("--sync-private", action="store_true", help="覆盖运行副本中的 .env/secret.private")
    parser.add_argument("--skip-deps", action="store_true")
    parser.add_argument("--no-install", action="store_true")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8567)
    parser.add_argument("--hour", type=int, default=2)
    parser.add_argument("--minute", type=int, default=30)
    args = parser.parse_args()

    source = args.source.expanduser().resolve()
    destination = args.destination.expanduser().resolve()
    if is_macos_protected_user_path(destination):
        raise SystemExit("运行副本不能放在 Desktop/Documents/Downloads；请使用 ~/Services 等目录")
    if source == destination:
        raise SystemExit("源目录与运行目录不能相同")
    branch, origin = validate_source(source)
    clone_or_fast_forward(source, destination, branch, origin)
    sync_private_files(source, destination, force=args.sync_private)
    prepare_runtime(destination, skip_deps=args.skip_deps)
    if not args.no_install:
        install_launchagents(
            destination,
            host=args.host,
            port=args.port,
            hour=args.hour,
            minute=args.minute,
        )
    print(f"本地运行副本：{destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
