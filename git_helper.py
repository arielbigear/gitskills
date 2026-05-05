"""Git helper utilities."""

import subprocess
import sys
from datetime import datetime


def run(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip(), result.returncode


def current_branch():
    out, _ = run(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    return out


def list_stale_branches(days=30):
    # TODO: list branches whose last commit is older than `days` days
    pass


def summarize_log(n=10):
    """Print a compact summary of the last n commits."""
    out, code = run(["git", "log", f"-{n}", "--oneline", "--decorate"])
    if code != 0:
        print("Not a git repository.", file=sys.stderr)
        return
    print(out)


def uncommitted_changes():
    out, _ = run(["git", "status", "--porcelain"])
    return bool(out)


def branch_ahead_behind(branch="HEAD", remote="origin"):
    # TODO: return (ahead, behind) commit counts relative to the tracking remote
    pass


if __name__ == "__main__":
    print(f"Branch: {current_branch()}")
    print(f"Uncommitted changes: {uncommitted_changes()}")
    summarize_log()
