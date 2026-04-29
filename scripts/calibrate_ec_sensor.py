import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Load data
df = pd.read_csv("data/raw/ec_calibration_template.csv")

# Remove rows without measurements
df = df.dropna(subset=["commercial_ec_uS_cm", "lab_sensor_ec_uS_cm"])

# Prepare data
X = df[["lab_sensor_ec_uS_cm"]]
y = df["commercial_ec_uS_cm"]

# Fit model
model = LinearRegression()
model.fit(X, y)

# Predict corrected EC
df["lab_sensor_corrected_ec"] = model.predict(X)

# Calculate error
df["error"] = df["lab_sensor_corrected_ec"] - df["commercial_ec_uS_cm"]
df["percent_error"] = (df["error"] / df["commercial_ec_uS_cm"]) * 100

# Metrics
r2 = r2_score(y, df["lab_sensor_corrected_ec"])
rmse = np.sqrt(mean_squared_error(y, df["lab_sensor_corrected_ec"]))
mae = mean_absolute_error(y, df["lab_sensor_corrected_ec"])

print("Calibration Equation:")
print(f"EC = {model.coef_[0]:.4f} * Sensor + {model.intercept_:.4f}")

print("\nModel Performance:")
print(f"R²   = {r2:.4f}")
print(f"RMSE = {rmse:.4f}")
print(f"MAE  = {mae:.4f}")

# Save results
os.makedirs("results", exist_ok=True)
df.to_csv("results/calibration_summary.csv", index=False)

print("\nCalibration complete. Results saved to results/calibration_summary.csv")
