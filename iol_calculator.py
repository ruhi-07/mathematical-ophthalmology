def calculate_srk_iol_power(a_constant: float, axial_length: float, corneal_power: float) -> float:
    """
    Calculates the required Intraocular Lens (IOL) power using the standard SRK Formula.
    Formula: P = A - 2.5 * L - 0.9 * K
    """
    # Exact clinical regression equation
    iol_power = a_constant - (2.5 * axial_length) - (0.9 * corneal_power)
    return round(iol_power, 2)

# --- Test Case: Standard Clinical Scenario ---
# A patient with average axial length and standard corneal curvature
lens_constant = 118.5
patient_axial_length = 23.5
patient_corneal_power = 43.0

required_power = calculate_srk_iol_power(lens_constant, patient_axial_length, patient_corneal_power)

print("--- Ophthalmic Biometry Calculation ---")
print(f"Lens Constant (A): {lens_constant}")
print(f"Axial Length (L): {patient_axial_length} mm")
print(f"Corneal Power (K): {patient_corneal_power} D")
print("---------------------------------------")
print(f"Recommended Lens Power: {required_power} Diopters")
