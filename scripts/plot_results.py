import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
df = pd.read_csv("data/raw/ec_calibration_template.csv")

# Remove empty rows
df = df.dropna(subset=["commercial_ec_uS_cm", "lab_sensor_ec_uS_cm"])

# Create output folder if not exists
os.makedirs("results/figures", exist_ok=True)

# --- Calibration Curve ---
plt.figure()
plt.scatter(df["lab_sensor_ec_uS_cm"], df["commercial_ec_uS_cm"])
plt.xlabel("Lab Sensor EC (µS/cm)")
plt.ylabel("Commercial EC (µS/cm)")
plt.title("Calibration Curve")
plt.grid(True)
plt.savefig("results/figures/calibration_curve.png", dpi=300)

# --- EC vs Concentration ---
plt.figure()
plt.scatter(df["concentration_g_L"], df["commercial_ec_uS_cm"], label="Commercial")
plt.scatter(df["concentration_g_L"], df["lab_sensor_ec_uS_cm"], label="Lab Sensor")
plt.xscale("log")
plt.xlabel("Concentration (g/L)")
plt.ylabel("EC (µS/cm)")
plt.title("EC vs Log Concentration")
plt.legend()
plt.grid(True)
plt.savefig("results/figures/ec_vs_concentration_log.png", dpi=300)

# --- Error Plot ---
df["error"] = df["lab_sensor_ec_uS_cm"] - df["commercial_ec_uS_cm"]

plt.figure()
plt.scatter(df["concentration_g_L"], df["error"])
plt.xscale("log")
plt.xlabel("Concentration (g/L)")
plt.ylabel("Error (µS/cm)")
plt.title("Calibration Error")
plt.grid(True)
plt.savefig("results/figures/error_plot.png", dpi=300)

print("Plots saved to results/figures/")
