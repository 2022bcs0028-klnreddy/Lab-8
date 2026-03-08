import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

new_metrics_path = ROOT / "metrics.json"
old_metrics_path = ROOT / "prev_metrics.json"

with open(new_metrics_path) as f:
    new_metrics = json.load(f)

try:
    with open(old_metrics_path) as f:
        old_metrics = json.load(f)
except FileNotFoundError:
    old_metrics = {"r2": -1}

improved = new_metrics["r2"] > old_metrics["r2"]

print(f"New R2: {new_metrics['r2']}")
print(f"Old R2: {old_metrics['r2']}")
print(f"Improved: {improved}")

with open(old_metrics_path, "w") as f:
    json.dump(new_metrics, f, indent=4)

if improved:
    print("::set-output name=improved::true")
else:
    print("::set-output name=improved::false")