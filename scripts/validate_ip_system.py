#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEX = re.compile(r"^#[0-9A-F]{6}$")
RATIO = re.compile(r"^[0-9]+(?:\.[0-9]+)?:[0-9]+(?:\.[0-9]+)?$")


def fail(message: str) -> None:
    print(f"IP system validation failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def load(relative: str) -> dict:
    path = ROOT / relative
    if not path.exists():
        fail(f"missing {relative}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        fail(f"invalid JSON in {relative}: {error}")
    if data.get("schema_version") != 1:
        fail(f"{relative} must use schema_version 1")
    return data


identity = load("design-system/identity-rules.json")
assets = load("design-system/asset-types.json")
compositions = load("design-system/compositions.json")
evals = load("evals/evals.json")

anchor_policy = identity.get("identity_anchor_policy", {})
if anchor_policy.get("minimum_anchors_per_asset", 0) < 3:
    fail("identity requires at least three anchors per asset")
if identity.get("variation_budget", {}).get("identity_changes") != 0:
    fail("identity changes must be zero")

asset_items = assets.get("asset_types", [])
asset_ids = {item.get("id") for item in asset_items}
if len(asset_ids) != len(asset_items) or not asset_ids:
    fail("asset type ids must be unique and non-empty")
for item in asset_items:
    if not item.get("default_dimensions") or not item.get("required_signals") or not item.get("forbidden_signals"):
        fail(f"{item.get('id', '?')} needs dimensions, required signals, and forbidden signals")
    if not item.get("ratios") or any(not RATIO.fullmatch(ratio) for ratio in item["ratios"]):
        fail(f"{item.get('id', '?')} has invalid ratios")
    area = item.get("character_area_percent", [])
    if len(area) != 2 or not 0 < area[0] <= area[1] <= 100:
        fail(f"{item.get('id', '?')} has invalid character area")

composition_items = compositions.get("compositions", [])
composition_ids = {item.get("id") for item in composition_items}
if len(composition_ids) != len(composition_items) or not composition_ids:
    fail("composition ids must be unique and non-empty")
for item in composition_items:
    if not item.get("asset_types") or not set(item["asset_types"]).issubset(asset_ids):
        fail(f"{item.get('id', '?')} references unknown asset types")
    if item.get("focal_event_count") != 1:
        fail(f"{item.get('id', '?')} must define one focal event")

eval_items = evals.get("evals", [])
if len(eval_items) < 8:
    fail("at least eight eval cases are required")
eval_ids = [item.get("id") for item in eval_items]
if len(eval_ids) != len(set(eval_ids)):
    fail("eval ids must be unique")
for item in eval_items:
    assertions = item.get("assertions", {})
    if not item.get("prompt") or not assertions.get("must_not"):
        fail(f"eval {item.get('id', '?')} needs prompt and negative assertions")

print(f"Validated IP asset system: {len(asset_items)} asset types, {len(composition_items)} compositions, {len(eval_items)} eval cases.")
