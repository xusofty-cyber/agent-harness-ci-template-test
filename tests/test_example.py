#!/usr/bin/env python3
"""Minimal example check: the passing gate item's verification command."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from example import hello

assert hello() == "ok"
print("example ok")
