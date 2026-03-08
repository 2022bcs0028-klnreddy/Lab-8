import pandas as pd
import json
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Project root
ROOT = Path(__file__).resolve().parent.parent

# Paths
DATA_PATH = ROOT / "data" / "housing.csv"
METRICS_PATH = ROOT / "metrics.json"
MODEL_PATH = ROOT / "model.pkl"

# Load dataset
df = pd.read_csv(DATA_PATH)

# Handle missing values
df = df.fillna(df.mean(numeric_only=True))

# Convert categorical column to numeric
df = pd.get_dummies(df, columns=["ocean_proximity"])

# Features and target
X = df.drop("median_house_value", axis=1)
y = df["median_house_value"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
pred = model.predict(X_test)

# Metrics
rmse = mean_squared_error(y_test, pred) ** 0.5
r2 = r2_score(y_test, pred)

metrics = {
    "dataset_size": int(len(df)),
    "rmse": float(rmse),
    "r2": float(r2)
}

# Save metrics
with open(METRICS_PATH, "w") as f:
    json.dump(metrics, f, indent=4)

# Save model (useful for Docker deployment)
joblib.dump(model, MODEL_PATH)

print("Training complete")
print(metrics)