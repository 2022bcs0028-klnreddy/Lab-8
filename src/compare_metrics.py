import json
import sys

with open("metrics.json") as f:
    new_metrics = json.load(f)

try:
    with open("prev_metrics.json") as f:
        old_metrics = json.load(f)
except:
    old_metrics = {"accuracy": 0}

improved = new_metrics["accuracy"] > old_metrics["accuracy"]

print(f"Improved: {improved}")

with open("prev_metrics.json", "w") as f:
    json.dump(new_metrics, f)

if improved:
    print("::set-output name=improved::true")
else:
    print("::set-output name=improved::false")