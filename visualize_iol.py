import matplotlib.pyplot as plt
import numpy as np

def calculate_srk_iol_power(a_constant, axial_length, corneal_power):
    """Calculates IOL power using the SRK Formula: P = A - 2.5L - 0.9K"""
    return a_constant - (2.5 * axial_length) - (0.9 * corneal_power)

# 1. Generate clinical simulation data
# Axial Length range: 21.0mm (short eye/hyperopic) to 26.0mm (long eye/myopic)
axial_lengths = np.linspace(21.0, 26.0, 100)
a_constant = 118.5

# Standard clinical corneal curvatures to compare (Flat, Normal, Steep)
corneal_powers = {
    'Flat Cornea (40.0 D)': 40.0,
    'Normal Cornea (43.0 D)': 43.0,
    'Steep Cornea (46.0 D)': 46.0
}

# 2. Set up the plotting canvas
plt.figure(figsize=(10, 6))

# 3. Calculate and plot curves for each corneal profile
colors = ['#e67e22', '#2ecc71', '#2980b9']
for (label, K), color in zip(corneal_powers.items(), colors):
    iol_powers = calculate_srk_iol_power(a_constant, axial_lengths, K)
    plt.plot(axial_lengths, iol_powers, label=label, color=color, linewidth=2.5)

# 4. Stylize the chart for a professional look
plt.title('IOL Power Sensitivity Analysis (SRK Model)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Patient Axial Length (mm)', fontsize=12, fontweight='semibold')
plt.ylabel('Required Lens Power (Diopters)', fontsize=12, fontweight='semibold')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11, loc='upper right')

# Highlight standard baseline anatomical cross-section
plt.axvline(x=23.5, color='gray', linestyle=':', alpha=0.7)
plt.axhline(y=21.05, color='gray', linestyle=':', alpha=0.7)
plt.plot(23.5, 21.05, 'ro') # Red dot at standard average eye specs
plt.annotate(' Standard Eye Baseline', (23.5, 21.5), fontsize=10, color='darkred', weight='bold')

plt.tight_layout()

# Save the visualization locally so it can be uploaded to GitHub
plt.savefig('iol_sensitivity_plot.png', dpi=300)
print("Success! 'iol_sensitivity_plot.png' has been created.")
