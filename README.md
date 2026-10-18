<img width="919" height="508" alt="Screenshot 2026-10-18 14 04 44" src="https://github.com/user-attachments/assets/3b731140-fc64-45e4-9dff-343e58d97497" />
# Mathematical Ophthalmology: IOL Power Calculator

A biomedical engineering portfolio project demonstrating the mathematical modelling of human ocular biometry. This repository contains a Python implementation of clinical formulas used to calculate the required power of an **Intraocular Lens (IOL)** during cataract surgery.

## 🩺 The Clinical Context
During cataract surgery, a patient's natural cloudy lens is replaced with an artificial Intraocular Lens (IOL). Selecting the correct lens power is vital; a calculation error of just 1mm in ocular structural mapping can lead to severely blurred postoperative vision. 

## 🧮 The Mathematics
This project implements the foundational **SRK (Sanders-Retzlaff-Kraff) Formula**, a linear regression model that calculates the necessary lens power (P) based on physical measurements of the eye:

\[P = A - 2.5L - 0.9K\]

Where:
* **P**: Required IOL power in Diopters (D)
* **A**: The specific lens manufacturer's constant
* **L**: Axial Length of the eye (mm) from front to back
* **K**: Average Corneal Power (Diopters) representing curvature

## 🚀 How to Run the Code
The core equations are written in pure Python without external dependencies. 

1. Clone this repository or download `iol_calculator.py`.
2. Run the file using your terminal:
   ```bash
   python iol_calculator.py
   ```
