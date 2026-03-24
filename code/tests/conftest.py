import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "code" / "src"
SCENARIO_DATA_DIR = ROOT / "data" / "scenarios" / "synthetic_firefighter_radio_controlled_v1"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
