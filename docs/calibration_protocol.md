# EC Sensor Calibration Protocol

## 1. Objective

To calibrate a lab-developed electrical conductivity (EC) sensor using sodium chloride (NaCl) solutions and compare its performance against a commercial EC meter (VWR Symphony SB80PC).

---

## 2. Materials and Equipment

- Lab-developed EC sensor  
- Commercial EC meter (VWR Symphony SB80PC)  
- Analytical balance (Mettler Toledo XS104)  
- Magnetic stirrer (SCILOGEX MS-H380-Pro)  
- Non-iodized NaCl salt  
- Deionized (DI) or distilled water  
- 8 sample bottles (500 mL each)  
- Temperature probe (optional)

---

## 3. Solution Preparation

Each solution is prepared using **500 mL of DI water**.

| Bottle | NaCl Mass (g) | Concentration (g/L) |
|--------|--------------:|--------------------:|
| B1     | 0.000         | 0.00                |
| B2     | 0.005         | 0.01                |
| B3     | 0.015         | 0.03                |
| B4     | 0.050         | 0.10                |
| B5     | 0.150         | 0.30                |
| B6     | 0.500         | 1.00                |
| B7     | 1.500         | 3.00                |
| B8     | 5.000         | 10.00               |

**Procedure:**
1. Weigh NaCl using an analytical balance  
2. Add NaCl to 500 mL DI water  
3. Stir until fully dissolved  
4. Label each bottle accordingly  

---

## 4. Measurement Procedure

For each solution:

1. Place solution on magnetic stirrer (low speed)  
2. Maintain temperature at approximately **20°C**  
3. Measure EC using the **commercial meter (reference)**  
4. Measure EC using the **lab-developed sensor**  
5. Record temperature and readings  
6. Repeat measurements (recommended: 3 trials)

---

## 5. Data Recording

Record data in:

```text
data/raw/ec_calibration_template.csv
