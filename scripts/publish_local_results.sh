#!/bin/zsh
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

PYTHON_BIN="${DPR_LOCAL_VENV:-$ROOT_DIR/.venv}/bin/python"
read_env_value() {
  [[ -x "$PYTHON_BIN" ]] || return 0
  "$PYTHON_BIN" - "$ROOT_DIR" "$1" <<'PY'
import sys
from pathlib import Path

root = Path(sys.argv[1])
sys.path.insert(0, str(root / "src"))
from local_env import read_env_file

print(read_env_file(root / ".env").get(sys.argv[2], ""), end="")
PY
}
for env_key in DPR_LOCAL_PUBLISH DPR_LOCAL_PUBLISH_BRANCH DPR_LOCAL_PUBLISH_CONFIG; do
  if [[ -z "${(P)env_key:-}" ]]; then
    export "$env_key=$(read_env_value "$env_key")"
  fi
done

if [[ "${DPR_LOCAL_PUBLISH:-0}" != "1" ]]; then
  print "[local-publish] DPR_LOCAL_PUBLISH 未启用，跳过。"
  exit 0
fi

branch="${DPR_LOCAL_PUBLISH_BRANCH:-$(git branch --show-current)}"
if [[ -z "$branch" ]]; then
  print -u2 "[local-publish] 当前不在分支上，请设置 DPR_LOCAL_PUBLISH_BRANCH。"
  exit 1
fi

unrelated=()
while IFS= read -r line; do
  [[ -z "$line" ]] && continue
  changed_path="${line:3}"
  case "$changed_path" in
    docs/*|archive/*|config.yaml) ;;
    *) unrelated+=("$changed_path") ;;
  esac
done < <(git status --porcelain)
if (( ${#unrelated[@]} > 0 )); then
  print -u2 "[local-publish] 检测到非运行产物改动，拒绝自动提交："
  printf '  %s\n' "${unrelated[@]}" >&2
  exit 1
fi

paths=(docs)
for state_path in archive/arxiv_seen.json archive/crawl_state.json archive/carryover.json; do
  [[ -e "$state_path" ]] && paths+=("$state_path")
done
for recommend_dir in archive/*/recommend(N/); do
  paths+=("$recommend_dir")
done
if [[ "${DPR_LOCAL_PUBLISH_CONFIG:-0}" == "1" ]]; then
  paths+=(config.yaml)
fi

git add -- "${paths[@]}"
git add -u -- docs archive

invalid_staged=()
while IFS= read -r staged_path; do
  [[ -z "$staged_path" ]] && continue
  case "$staged_path" in
    docs/*|archive/arxiv_seen.json|archive/crawl_state.json|archive/carryover.json|archive/*/recommend/*) ;;
    config.yaml)
      [[ "${DPR_LOCAL_PUBLISH_CONFIG:-0}" == "1" ]] || invalid_staged+=("$staged_path")
      ;;
    *) invalid_staged+=("$staged_path") ;;
  esac
done < <(git diff --cached --name-only)
if (( ${#invalid_staged[@]} > 0 )); then
  print -u2 "[local-publish] 暂存区包含未授权路径，已停止："
  printf '  %s\n' "${invalid_staged[@]}" >&2
  git restore --staged -- "${invalid_staged[@]}"
  exit 1
fi

if git diff --cached --quiet; then
  print "[local-publish] 没有需要发布的生成结果。"
  exit 0
fi

git commit -m "[chore] local daily pipeline

Co-Authored-By: xixi <3495302215@qq.com>"
git fetch origin "$branch"
git rebase "origin/$branch"
git push origin "HEAD:$branch"
print "[local-publish] 已推送到 origin/$branch"
