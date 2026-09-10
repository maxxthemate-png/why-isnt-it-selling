#!/usr/bin/env python3
"""Merge a 14-day GitHub traffic window into a cumulative ledger.

The traffic API only ever returns a rolling 14-day window, so overwriting the
ledger each night would cap the cumulative count at 14 days forever. The gate
this feeds needs a cumulative total across 8 weeks, so we union by date string:
each date is stored once, and a later reading for the same date wins (the window
is still filling in for recent days).

    python3 scripts/merge-traffic.py --ledger stats/ledger.json \
        --clones clones.json --views views.json --stars 42
"""
import argparse
import json
import os
from datetime import datetime, timezone


def read_json(path, default):
    if not path or not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as fh:
        try:
            return json.load(fh)
        except json.JSONDecodeError:
            return default


def merge_series(existing, incoming):
    """Union daily buckets by timestamp. Later reading of a date wins."""
    by_date = {row["timestamp"]: row for row in existing}
    for row in incoming:
        ts = row.get("timestamp")
        if not ts:
            continue
        by_date[ts] = {
            "timestamp": ts,
            "count": int(row.get("count", 0)),
            "uniques": int(row.get("uniques", 0)),
        }
    return [by_date[k] for k in sorted(by_date)]


def badge(label, message, color="blue"):
    return {"schemaVersion": 1, "label": label, "message": message, "color": color}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ledger", default="stats/ledger.json")
    ap.add_argument("--clones")
    ap.add_argument("--views")
    ap.add_argument("--stars", type=int)
    ap.add_argument("--out-dir", default="stats")
    args = ap.parse_args()

    ledger = read_json(args.ledger, {})
    ledger.setdefault("clones", [])
    ledger.setdefault("views", [])

    ledger["clones"] = merge_series(ledger["clones"], read_json(args.clones, {}).get("clones", []))
    ledger["views"] = merge_series(ledger["views"], read_json(args.views, {}).get("views", []))

    if args.stars is not None:
        ledger["stars"] = args.stars
    ledger["updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    total_unique_cloners = sum(r["uniques"] for r in ledger["clones"])
    total_unique_viewers = sum(r["uniques"] for r in ledger["views"])
    ledger["totals"] = {
        "unique_cloners": total_unique_cloners,
        "unique_viewers": total_unique_viewers,
        "days_recorded": len(ledger["clones"]),
    }

    os.makedirs(args.out_dir, exist_ok=True)
    with open(args.ledger, "w", encoding="utf-8") as fh:
        json.dump(ledger, fh, indent=2, sort_keys=True)
        fh.write("\n")

    badges = {
        "badge-cloners.json": badge("installs", str(total_unique_cloners), "1f6feb"),
        "badge-stars.json": badge("stars", str(ledger.get("stars", 0)), "8957e5"),
    }
    for name, body in badges.items():
        with open(os.path.join(args.out_dir, name), "w", encoding="utf-8") as fh:
            json.dump(body, fh, indent=2)
            fh.write("\n")

    print(f"cloners={total_unique_cloners} viewers={total_unique_viewers} "
          f"days={len(ledger['clones'])} stars={ledger.get('stars', 0)}")


if __name__ == "__main__":
    main()
