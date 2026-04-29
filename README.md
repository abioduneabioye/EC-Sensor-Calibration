# EC Sensor Calibration Workflow

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)
![Made with](https://img.shields.io/badge/Made%20with-Data%20Science-orange)

This project presents a systematic calibration of a lab-developed electrical conductivity (EC) sensor using sodium chloride (NaCl) solutions across a logarithmic concentration range. A commercial EC meter (VWR Symphony SB80PC) is used as the reference instrument to evaluate sensor accuracy, bias, and performance.

---

## Objective

To calibrate a lab-developed EC sensor by comparing its measurements against a commercial conductivity meter across a controlled NaCl concentration range.

---

## Equipment

- Lab-developed EC sensor  
- VWR Symphony SB80PC commercial conductivity meter  
- Mettler Toledo XS104 analytical balance (±0.0001 g resolution)  
- SCILOGEX MS-H380-Pro magnetic stirrer/hot plate  
- NaCl salt (non-iodized)  
- Deionized (DI) or distilled water  
- 8 sample bottles (500 mL each)  
- Temperature probe  
- Water bath setup (for temperature control)  

---

## Sample Preparation

Each solution is prepared using **500 mL DI water**, with varying NaCl mass to create a logarithmic concentration range.

| Bottle | NaCl Mass (g) | Concentration (g/L) | log10(Conc) | Expected EC (µS/cm)* |
|:------:|--------------:|--------------------:|------------:|--------------------:|
| B1     | 0.000         | 0.00                | —           | ~0–10              |
| B2     | 0.005         | 0.01                | -2.00       | ~20–30             |
| B3     | 0.015         | 0.03                | -1.52       | ~60–80             |
| B4     | 0.050         | 0.10                | -1.00       | ~200–300           |
| B5     | 0.150         | 0.30                | -0.52       | ~600–800           |
| B6     | 0.500         | 1.00                | 0.00        | ~2000              |
| B7     | 1.500         | 3.00                | 0.48        | ~5000–6000         |
| B8     | 5.000         | 10.00               | 1.00        | ~15000–20000       |

> *Expected EC values are approximate and depend on temperature and solution conditions.

---

## Mass Measurement and Transfer Accuracy

- NaCl is weighed using a **tared weighing boat (or weighing paper)** on an analytical balance.  
- At low masses (e.g., 0.005 g), relative uncertainty increases and is estimated.  
- To minimize transfer loss:
  - Salt is transferred carefully using a spatula  
  - The weighing container is rinsed with DI water (spray bottle) to recover residual salt  
- After transfer, the solution is brought to a **fixed final volume of 500 mL**

> This ensures mass conservation and maintains concentration accuracy within approximately **≤1% uncertainty**, making solution preparation a minor source of error.

---

## Temperature Control

Electrical conductivity is temperature-dependent; therefore, maintaining **20°C** is essential.

- Solutions are placed in a **well-mixed water bath**  
- If a dedicated bath is unavailable, an improvised bath will be used  
- Temperature is continuously monitored using a thermometer  
- Measurements are taken only after thermal equilibrium is reached  

---

## Measurement Procedure

For each concentration:

1. Gently mix solution using a magnetic stirrer  
2. Transfer approximately **50 mL** into a clean beaker or flask  
3. Measure EC using the **commercial EC meter (reference)**  
4. Measure EC using the **lab-developed sensor**  
5. Record temperature  
6. Repeat measurements for **3 trials**

Between measurements:

- Probes are rinsed with DI water  
- Probes are dried to avoid dilution  
- Measurements are conducted from **low → high concentration** to minimize contamination  

---

## Trials and Data Collection

Each concentration is measured in **triplicate (3 trials)**:

- Each trial is recorded as a separate row in the dataset  
- Final calibration uses **averaged values** to reduce noise  
---

## Results

### Calibration Curve

![Calibration Curve](results/figures/calibration_curve.png)

### EC vs Logarithmic Concentration

![EC vs Concentration](results/figures/ec_vs_concentration_log.png)

### Calibration Error

![Calibration Error](results/figures/error_plot.png)

> The calibration model maps the lab sensor EC output to the commercial meter readings using regression analysis to quantify accuracy, bias, and error.

---

## Repository Structure

```text
ec-sensor-calibration/
│
├── README.md
├── requirements.txt
├── EC_calibration.ipynb  
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│   ├── calibrate_ec_sensor.py
│   └── plot_results.py
│
├── results/
│   ├── figures/
│   └── calibration_summary.csv
│
├── docs/
│   └── calibration_protocol.md
│
└── LICENSE
## How to Run

To reproduce the calibration results and plots:

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run calibration

```bash
python scripts/calibrate_ec_sensor.py
```

### 3. Generate plots

```bash
python scripts/plot_results.py
```

---

## Expected Outputs

* `results/calibration_summary.csv`  
* `results/figures/calibration_curve.png`  
* `results/figures/ec_vs_concentration_log.png`  
* `results/figures/error_plot.png`  

---

## Notes

* The commercial EC meter is used as the **reference (ground truth)**  
* NaCl solutions provide controlled variation in ionic concentration  
* Temperature and mixing conditions are controlled for accuracy  
* Low-speed stirring is used to ensure uniformity and minimize air bubbles  
