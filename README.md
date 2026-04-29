# EC Sensor Calibration Workflow

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)
![Made with](https://img.shields.io/badge/Made%20with-Data%20Science-orange)

This project presents a systematic calibration of a lab-developed electrical conductivity (EC) sensor using sodium chloride (NaCl) solutions across a logarithmic concentration range. A commercial EC meter (VWR Symphony SB80PC) is used as the reference instrument to evaluate sensor accuracy and performance.

---

## Objective

To compare and calibrate the lab-developed EC sensor against a commercial conductivity meter across a logarithmic NaCl concentration range.

---

## Equipment

* Lab-developed EC sensor  
* VWR Symphony SB80PC commercial conductivity meter  
* Mettler Toledo XS104 analytical balance  
* SCILOGEX MS-H380-Pro magnetic stirrer/hot plate  
* NaCl salt (non-iodized)  
* DI or distilled water  
* 8 sample bottles (500 mL each)  

---

## Sample Preparation

Each bottle contains **500 mL of DI water**, with varying NaCl mass to achieve a logarithmic concentration range.

| Bottle | NaCl Mass (g) | Concentration (g/L) | log10(Conc) |
|:------:|--------------:|--------------------:|------------:|
| B1     | 0.000         | 0.00                | —           |
| B2     | 0.005         | 0.01                | -2.00       |
| B3     | 0.015         | 0.03                | -1.52       |
| B4     | 0.050         | 0.10                | -1.00       |
| B5     | 0.150         | 0.30                | -0.52       |
| B6     | 0.500         | 1.00                | 0.00        |
| B7     | 1.500         | 3.00                | 0.48        |
| B8     | 5.000         | 10.00               | 1.00        |

> All solutions were prepared using consistent volume (500 mL) and high-precision mass measurements.

---

## Workflow

1. Prepare NaCl solutions at specified concentrations  
2. Stir solutions gently to ensure homogeneity  
3. Measure EC using the **commercial EC meter (reference)**  
4. Measure EC using the **lab-developed sensor**  
5. Record temperature for each measurement  
6. Repeat measurements (recommended: 3 trials)  
7. Fit calibration model and evaluate performance  

> Measurements were conducted under controlled stirring conditions with consistent probe placement to ensure repeatability.

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
