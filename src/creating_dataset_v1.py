import pandas as pd
import os

# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Load original dataset
df = pd.read_csv("housing.csv")

# Take first 5000 rows
df_v1 = df.head(5000)

# Save Dataset Version 1
df_v1.to_csv("data/housing.csv", index=False)

print("Dataset Version 1 created successfully!")
print("Rows:", len(df_v1))