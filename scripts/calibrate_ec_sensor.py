import pandas as pd
import numpy as np
import os
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Load data
df = pd.read_csv("data/raw/ec_calibration_template.csv")

# Use only valid calibration samples
df_cal = df[
    (df["use_for_calibration"].str.lower() == "yes") &
    (df["adj_ratio"] > 0) &
    (df["commercial_ec_uS_cm"] > 0)
].copy()

# Average trials by sample
df_avg = df_cal.groupby(
    ["sample_id", "nacl_mass_g", "volume_ml", "concentration_g_L"],
    as_index=False
).mean(numeric_only=True)

# Log-log quadratic calibration
x = np.log10(df_avg["adj_ratio"])
y = np.log10(df_avg["commercial_ec_uS_cm"])

a, b, c = np.polyfit(x, y, 2)

df_avg["predicted_ec_uS_cm"] = 10 ** (a * x**2 + b * x + c)

# Error analysis
df_avg["error_uS_cm"] = df_avg["predicted_ec_uS_cm"] - df_avg["commercial_ec_uS_cm"]
df_avg["percent_error"] = (
    df_avg["error_uS_cm"] / df_avg["commercial_ec_uS_cm"]
) * 100

r2 = r2_score(df_avg["commercial_ec_uS_cm"], df_avg["predicted_ec_uS_cm"])
rmse = np.sqrt(mean_squared_error(df_avg["commercial_ec_uS_cm"], df_avg["predicted_ec_uS_cm"]))
mae = mean_absolute_error(df_avg["commercial_ec_uS_cm"], df_avg["predicted_ec_uS_cm"])

print("Log-Quadratic Calibration Equation:")
print(f"log10(EC) = {a:.6f}(log10(Ratio))^2 + {b:.6f}(log10(Ratio)) + {c:.6f}")

print("\nModel Performance:")
print(f"R²   = {r2:.4f}")
print(f"RMSE = {rmse:.4f} µS/cm")
print(f"MAE  = {mae:.4f} µS/cm")

# Save outputs
os.makedirs("results", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

df_avg.to_csv("results/calibration_summary.csv", index=False)
df_avg.to_csv("data/processed/calibration_averaged.csv", index=False)

print("\nCalibration complete.")
print("Results saved to results/calibration_summary.csv")
print("Averaged data saved to data/processed/calibration_averaged.csv")
