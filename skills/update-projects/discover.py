"""List accessible, enrolled github.com repositories without changing GitHub or disk."""

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urlencode


def github_api(endpoint):
    result = subprocess.run(
        ["gh", "api", "--hostname", "github.com", endpoint],
        capture_output=True, text=True, encoding="utf-8",
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "GitHub API call failed")
    return json.loads(result.stdout)


def discover_owner(owner, api):
    account = api(f"users/{owner}")
    qualifier = {"Organization": "org", "User": "user"}[account["type"]]
    query = f"{qualifier}:{owner} topic:igorlo-hub-managed archived:false"
    names = set()
    page = 1
    expected = None
    while True:
        params = urlencode({"q": query, "per_page": 100, "page": page})
        result = api("search/repositories?" + params)
        total = result["total_count"]
        if result["incomplete_results"] or total > 1000:
            raise ValueError("incomplete or truncated search")
        if expected is None:
            expected = total
        if expected != total:
            raise ValueError("membership changed during pagination")
        for repo in result["items"]:
            full_name = repo["full_name"]
            if (full_name.split("/")[0].casefold() != owner.casefold()
                    or repo["archived"] or "igorlo-hub-managed" not in repo["topics"]):
                raise ValueError("search returned stale repository metadata")
            names.add(full_name.casefold())
        if page * 100 >= total:
            break
        page += 1
    if len(names) != expected:
        raise ValueError("pagination returned missing or duplicate entries")
    return names


def discover(owners, previous, api):
    actor = api("user")["login"]
    found = set()
    errors = {}
    for owner in owners:
        try:
            found.update(discover_owner(owner, api))
        except (KeyError, OSError, ValueError, RuntimeError) as exc:
            errors[owner] = str(exc)
    return {
        "actor": actor, "owners": owners, "repositories": sorted(found),
        "previously_seen_missing": sorted(previous - found),
        "owner_errors": errors,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, help="last accepted private JSON snapshot")
    args = parser.parse_args()
    owners = sorted({s.strip().lower() for s in os.getenv("IGORLO_HUB_OWNERS", "").split(",")
                     if s.strip()})
    if not owners or any(not re.fullmatch(r"[a-z0-9][a-z0-9-]*", owner) for owner in owners):
        parser.error("set IGORLO_HUB_OWNERS to comma-separated GitHub owners")
    try:
        previous = set()
        if args.previous:
            names = json.loads(args.previous.read_text(encoding="utf-8-sig"))["repositories"]
            if not isinstance(names, list) or not all(isinstance(n, str) for n in names):
                raise ValueError("invalid previous snapshot")
            previous = {n.casefold() for n in names}
        report = discover(owners, previous, github_api)
    except (KeyError, OSError, ValueError, RuntimeError) as exc:
        sys.exit(f"Discovery failed: {exc}")
    print(json.dumps(report, indent=2))
    return 1 if report["owner_errors"] or report["previously_seen_missing"] else 0


if __name__ == "__main__":
    sys.exit(main())
