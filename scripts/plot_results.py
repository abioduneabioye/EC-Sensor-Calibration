import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Load processed calibration summary
df = pd.read_csv("results/calibration_summary.csv")

os.makedirs("results/figures", exist_ok=True)

# --- Calibration Curve: Adj_Ratio vs Commercial EC ---
plt.figure()
plt.scatter(df["adj_ratio"], df["commercial_ec_uS_cm"], label="Commercial EC")
plt.scatter(df["adj_ratio"], df["predicted_ec_uS_cm"], label="Model Predicted EC")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Smart Rock Adj_Ratio (I/V Ratio)")
plt.ylabel("EC (µS/cm)")
plt.title("Smart Rock Calibration vs Commercial EC Meter")
plt.legend()
plt.grid(True, which="both")
plt.savefig("results/figures/calibration_curve.png", dpi=300, bbox_inches="tight")

# --- EC vs Concentration ---
df_log = df[df["concentration_g_L"] > 0].copy()

plt.figure()
plt.scatter(df_log["concentration_g_L"], df_log["commercial_ec_uS_cm"], label="Commercial EC")
plt.scatter(df_log["concentration_g_L"], df_log["predicted_ec_uS_cm"], label="Model Predicted EC")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("NaCl Concentration (g/L)")
plt.ylabel("EC (µS/cm)")
plt.title("EC Response Across Logarithmic NaCl Range")
plt.legend()
plt.grid(True, which="both")
plt.savefig("results/figures/ec_vs_concentration_log.png", dpi=300, bbox_inches="tight")

# --- Error Plot ---
plt.figure()
plt.axhline(0, linestyle="--")
plt.scatter(df["commercial_ec_uS_cm"], df["error_uS_cm"])
plt.xscale("log")
plt.xlabel("Commercial EC (µS/cm)")
plt.ylabel("Prediction Error (µS/cm)")
plt.title("Calibration Error")
plt.grid(True, which="both")
plt.savefig("results/figures/error_plot.png", dpi=300, bbox_inches="tight")

print("Plots saved to results/figures/")
