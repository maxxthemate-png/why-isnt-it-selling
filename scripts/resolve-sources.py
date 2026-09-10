#!/usr/bin/env python3
"""Resolve evidence cluster IDs to their tactic and source URL.

Build tool. It ships no data of its own: you point it at a run_data JSON file and
it prints a markdown table. Used to regenerate the Backing lines on pattern cards.

    python3 scripts/resolve-sources.py --run-data /path/to/run_data.json \
        --ids cl_0146,cl_0378,cl_0039

Omit --ids to dump every cluster that has a resolvable URL.
"""
import argparse
import json
import sys


def load_clusters(path):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    # clusters is a flat array sorted by rank, not a map. Index it ourselves.
    return {c["cluster_id"]: c for c in data.get("clusters", [])}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--run-data", required=True, help="path to a run_data JSON file")
    ap.add_argument("--ids", help="comma-separated cluster IDs, e.g. cl_0146,cl_0378")
    ap.add_argument("--width", type=int, default=110, help="truncate tactic text")
    args = ap.parse_args()

    clusters = load_clusters(args.run_data)
    if args.ids:
        wanted = [i.strip() for i in args.ids.split(",") if i.strip()]
    else:
        wanted = sorted(k for k, v in clusters.items() if v.get("source_url"))

    missing, blank = [], []
    print("| id | tactic | source |")
    print("|---|---|---|")
    for cid in wanted:
        c = clusters.get(cid)
        if c is None:
            missing.append(cid)
            continue
        url = c.get("source_url") or ""
        if not url:
            blank.append(cid)
        # the tactic field is representative_tactic, not tactic
        tactic = (c.get("representative_tactic") or "").replace("|", "\\|")
        if len(tactic) > args.width:
            tactic = tactic[: args.width - 1].rstrip() + "…"
        print(f"| {cid} | {tactic} | {url or '(EMPTY, backfill from all_cards.json)'} |")

    if missing:
        print(f"\n> not found: {', '.join(missing)}", file=sys.stderr)
    if blank:
        print(
            f"\n> no URL on: {', '.join(blank)}. These sit in the cl_1275-cl_1372 "
            "block from one failed dedup batch and backfill via member_card_ids "
            "against data/processed/dedup_batches/all_cards.json.",
            file=sys.stderr,
        )
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
