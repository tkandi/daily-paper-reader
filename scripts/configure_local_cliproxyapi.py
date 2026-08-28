#!/usr/bin/env python3
"""Configure the local Daily Paper Reader runtime for CLIProxyAPI.

The client API key is read from the local CLIProxyAPI config or hidden input and
is never printed. The resulting .env is ignored by Git and chmod'ed to 0600.
"""

from __future__ import annotations

import argparse
import ast
import getpass
import json
import os
import re
import shutil
import sys
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from local_debug_server import update_env_file  # noqa: E402


DEFAULT_BASE_URL = "http://127.0.0.1:8317"
DEFAULT_CONFIG_PATH = Path("/opt/homebrew/etc/cliproxyapi.conf")


def _norm(value: Any) -> str:
    return str(value or "").strip()


def _unquote_yaml_scalar(value: str) -> str:
    text = _norm(value)
    if not text:
        return ""
    try:
        parsed = ast.literal_eval(text)
        return _norm(parsed)
    except Exception:
        return text.split(" #", 1)[0].strip()


def read_first_client_api_key(path: Path) -> str:
    try:
        import yaml  # type: ignore

        config = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        keys = config.get("api-keys") if isinstance(config, dict) else []
        if isinstance(keys, list):
            for value in keys:
                key = _norm(value)
                if key:
                    return key
    except Exception:
        pass

    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return ""
    in_api_keys = False
    parent_indent = 0
    for raw in lines:
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip())
        if not in_api_keys:
            if re.match(r"^api-keys\s*:\s*$", stripped):
                in_api_keys = True
                parent_indent = indent
            continue
        if indent <= parent_indent and not stripped.startswith("-"):
            break
        matched = re.match(r"^-\s*(.+?)\s*$", stripped)
        if matched:
            key = _unquote_yaml_scalar(matched.group(1))
            if key:
                return key
    return ""


def build_models_url(base_url: str) -> str:
    raw = _norm(base_url).rstrip("/")
    if not raw:
        raise ValueError("CLIProxyAPI Base URL 不能为空")
    if raw.lower().endswith("/models"):
        return raw
    if re.search(r"/v\d+$", raw, re.IGNORECASE):
        return f"{raw}/models"
    return f"{raw}/v1/models"


def fetch_model_ids(base_url: str, api_key: str, timeout: int = 15) -> list[str]:
    request = Request(
        build_models_url(base_url),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
        },
    )
    try:
        with urlopen(request, timeout=timeout) as response:  # nosec B310 - user-configured local API
            payload = json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:300]
        raise RuntimeError(f"模型目录请求失败：HTTP {exc.code} {detail}") from exc
    except (URLError, TimeoutError, OSError) as exc:
        raise RuntimeError(f"无法连接 CLIProxyAPI：{exc}") from exc

    rows = payload.get("data") if isinstance(payload, dict) else []
    out: list[str] = []
    seen: set[str] = set()
    for row in rows if isinstance(rows, list) else []:
        model = _norm(row.get("id") if isinstance(row, dict) else row)
        key = model.lower()
        if model and key not in seen:
            seen.add(key)
            out.append(model)
    return sorted(out, key=str.lower)


def choose_model(models: list[str], requested: str, interactive: bool) -> str:
    requested = _norm(requested)
    if requested:
        if requested not in models:
            raise ValueError(f"模型 {requested!r} 不在 CLIProxyAPI /v1/models 目录中")
        return requested
    if not interactive:
        raise ValueError("非交互模式必须通过 --model 指定模型")
    print("可用模型：")
    for index, model in enumerate(models, start=1):
        print(f"  {index:>2}. {model}")
    raw = input("请选择工作流/默认聊天模型编号：").strip()
    try:
        index = int(raw)
    except ValueError as exc:
        raise ValueError("请输入有效的模型编号") from exc
    if index < 1 or index > len(models):
        raise ValueError("模型编号超出范围")
    return models[index - 1]


def configure_env(
    env_path: Path,
    example_path: Path,
    *,
    api_key: str,
    base_url: str,
    model: str,
    chat_models: list[str],
) -> None:
    if not env_path.exists() and example_path.exists():
        shutil.copyfile(example_path, env_path)
    all_chat_models = []
    for item in [model, *chat_models]:
        value = _norm(item)
        if value and value not in all_chat_models:
            all_chat_models.append(value)
    update_env_file(
        env_path,
        {
            "LLM_PROVIDER": "cliproxyapi",
            "LLM_API_KEY": api_key,
            "LLM_BASE_URL": base_url.rstrip("/"),
            "LLM_MODEL": model,
            "DPR_LOCAL_CHAT_MODELS": ",".join(all_chat_models),
            "DPR_LLM_MAX_OUTPUT_TOKENS": "16384",
            "DPR_LLM_STRUCTURED_FORMAT": "json_object",
            "SUMMARY_API_KEY": api_key,
            "SUMMARY_BASE_URL": base_url.rstrip("/"),
            "SUMMARY_MODEL": model,
            "DEEPSEEK_API_KEY": api_key,
            "DEEPSEEK_BASE_URL": base_url.rstrip("/"),
            "DEEPSEEK_MODEL": model,
            "LLM_PRIMARY_BASE_URL": base_url.rstrip("/"),
            "RERANK_PROFILE": "public-zwwen-rerank",
            "RERANK_PROVIDER": "public_zwwen",
            "RERANK_MODEL": "Qwen/Qwen3-Reranker-0.6B",
            "RERANK_API_BASE_URL": "https://zwwen.online/rerank",
            "PUBLIC_RERANK_API_BASE_URL": "https://zwwen.online/rerank",
        },
    )
    os.chmod(env_path, 0o600)


def main() -> int:
    parser = argparse.ArgumentParser(description="配置本地 Daily Paper Reader 使用 CLIProxyAPI")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--model", default="")
    parser.add_argument("--chat-model", action="append", default=[])
    parser.add_argument("--cliproxy-config", type=Path, default=DEFAULT_CONFIG_PATH)
    parser.add_argument("--env-file", type=Path, default=ROOT_DIR / ".env")
    parser.add_argument("--api-key-stdin", action="store_true")
    parser.add_argument("--no-config-key", action="store_true", help="不从 CLIProxyAPI 配置读取客户端密钥")
    args = parser.parse_args()

    api_key = ""
    if args.api_key_stdin:
        api_key = sys.stdin.readline().strip()
    elif not args.no_config_key:
        api_key = read_first_client_api_key(args.cliproxy_config.expanduser())
    if not api_key:
        if not sys.stdin.isatty():
            raise SystemExit("未找到客户端 API Key；请使用 --api-key-stdin 安全传入")
        api_key = getpass.getpass("CLIProxyAPI 客户端 API Key（输入隐藏）：").strip()
    if not api_key:
        raise SystemExit("客户端 API Key 不能为空")

    models = fetch_model_ids(args.base_url, api_key)
    if not models:
        raise SystemExit("CLIProxyAPI 模型目录为空")
    model = choose_model(models, args.model, interactive=sys.stdin.isatty())
    invalid_chat = [item for item in args.chat_model if item not in models]
    if invalid_chat:
        raise SystemExit(f"聊天模型不在目录中：{', '.join(invalid_chat)}")
    configure_env(
        args.env_file.expanduser(),
        ROOT_DIR / ".env.example",
        api_key=api_key,
        base_url=args.base_url,
        model=model,
        chat_models=args.chat_model,
    )
    print(f"已配置 CLIProxyAPI：base={args.base_url.rstrip('/')} model={model}")
    print(f"模型目录共 {len(models)} 个；密钥已写入 {args.env_file}（0600，Git 忽略）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
