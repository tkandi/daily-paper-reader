#!/bin/zsh
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
VENV_DIR="${DPR_LOCAL_VENV:-$ROOT_DIR/.venv}"
PYTHON_BIN="$VENV_DIR/bin/python"
RUNS_DIR="$ROOT_DIR/.local-runs/scheduled"
LOCK_DIR="$RUNS_DIR/.daily.lock"
TIMESTAMP="$(date '+%Y%m%d-%H%M%S')"
LOG_FILE="$RUNS_DIR/daily-$TIMESTAMP.log"

mkdir -p "$RUNS_DIR"
if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  print "[local-daily] 已有日报任务运行中，跳过本次触发。"
  exit 0
fi
trap 'rmdir "$LOCK_DIR" 2>/dev/null || true' EXIT INT TERM

if [[ ! -x "$PYTHON_BIN" ]]; then
  print -u2 "[local-daily] 找不到本地 Python：$PYTHON_BIN"
  print -u2 "[local-daily] 请先运行 scripts/bootstrap_local.sh --prepare-only"
  exit 1
fi

read_env_value() {
  "$PYTHON_BIN" - "$ROOT_DIR" "$1" <<'PY'
import sys
from pathlib import Path

root = Path(sys.argv[1])
sys.path.insert(0, str(root / "src"))
from local_env import read_env_file

print(read_env_file(root / ".env").get(sys.argv[2], ""), end="")
PY
}

for env_key in \
  DPR_LOCAL_RUN_ENRICH \
  DPR_LOCAL_FETCH_DAYS \
  DPR_LOCAL_FETCH_MODE \
  DPR_LOCAL_PROFILE_TAG \
  DPR_LOCAL_PUBLISH \
  DPR_LOCAL_PUBLISH_BRANCH \
  DPR_LOCAL_PUBLISH_CONFIG; do
  if [[ -z "${(P)env_key:-}" ]]; then
    export "$env_key=$(read_env_value "$env_key")"
  fi
done
export DPR_DOTENV_PATH="${DPR_DOTENV_PATH:-$ROOT_DIR/.env}"
export PYTHONPATH="$ROOT_DIR/src${PYTHONPATH:+:$PYTHONPATH}"

args=()
if [[ "${DPR_LOCAL_RUN_ENRICH:-0}" == "1" ]]; then
  args+=(--run-enrich)
fi
if [[ -n "${DPR_LOCAL_FETCH_DAYS:-}" ]]; then
  args+=(--fetch-days "$DPR_LOCAL_FETCH_DAYS")
fi
if [[ -n "${DPR_LOCAL_FETCH_MODE:-}" ]]; then
  args+=(--fetch-mode "$DPR_LOCAL_FETCH_MODE")
fi
if [[ -n "${DPR_LOCAL_PROFILE_TAG:-}" ]]; then
  args+=(--profile-tag "$DPR_LOCAL_PROFILE_TAG")
fi

print "[local-daily] started_at=$(date -u '+%Y-%m-%dT%H:%M:%SZ')" | tee "$LOG_FILE"
print "[local-daily] root=$ROOT_DIR" | tee -a "$LOG_FILE"
print "[local-daily] command=$PYTHON_BIN src/main.py ${args[*]:-}" | tee -a "$LOG_FILE"

cd "$ROOT_DIR"
"$PYTHON_BIN" src/main.py "${args[@]}" 2>&1 | tee -a "$LOG_FILE"

if [[ "${DPR_LOCAL_PUBLISH:-0}" == "1" ]]; then
  print "[local-daily] pipeline succeeded; publishing generated results" | tee -a "$LOG_FILE"
  "$ROOT_DIR/scripts/publish_local_results.sh" 2>&1 | tee -a "$LOG_FILE"
else
  print "[local-daily] pipeline succeeded; publish disabled (DPR_LOCAL_PUBLISH=0)" | tee -a "$LOG_FILE"
fi

print "[local-daily] completed_at=$(date -u '+%Y-%m-%dT%H:%M:%SZ')" | tee -a "$LOG_FILE"
