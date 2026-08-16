from __future__ import annotations

import re
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "init.qti.display_boot.sh"

OPLUS_CANOE_PROPERTIES = {
    "vendor.display.enable_brightness_drm_prop": "0",
    "vendor.display.enable_inline_writeback": "0",
    "vendor.display.enable_spec_fence": "0",
    "vendor.display.libscale_version_override": "10",
}


def test_canoe_preserves_oplus_runtime_display_policy() -> None:
    script = SCRIPT.read_text(encoding="utf-8")
    start = script.index('    "canoe"|"hamoa")')
    end = script.index('    "seraph")', start)
    canoe_branch = script[start:end]
    properties = dict(re.findall(r"setprop\s+(\S+)\s+(\S+)", canoe_branch))

    assert {
        key: properties.get(key) for key in OPLUS_CANOE_PROPERTIES
    } == OPLUS_CANOE_PROPERTIES
