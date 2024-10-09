# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Experimental data for 1H: ν (MHz) and B₀ (mT)
nu_H = np.array([10.00, 10.30, 10.60, 10.90, 11.20, 11.50])  # MHz
B0_H = np.array([236.8, 243.9, 249.4, 256.9, 264.4, 270.8])  # mT

# Experimental data for 19F: ν (MHz) and B₀ (mT)
nu_F = np.array([10.00, 10.30, 10.60, 10.90, 11.20, 11.50])  # MHz
B0_F = np.array([250.1, 256.5, 266.6, 273.1, 280.2, 287.4])  # mT

# Use your provided γ/2π values
gamma_over_2pi_H = 0.04238  # MHz/mT for 1H
gamma_over_2pi_F = 0.03996  # MHz/mT for 19F

# Define the linear fit function for plotting
def linear_fit(B0, gamma_over_2pi):
    return gamma_over_2pi * B0

# Plot and save the graph for 1H
plt.figure(figsize=(6, 5))
plt.scatter(B0_H, nu_H, color="blue", label="Experimental data")
plt.plot(B0_H, linear_fit(B0_H, gamma_over_2pi_H), color="red",
         label=f"Fit: γ/2π = {gamma_over_2pi_H:.5f} MHz/mT")
plt.xlabel('B₀ (mT)')
plt.ylabel('ν (MHz)')
plt.title(r'$^1$H NMR: ν vs B₀')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("1H_nmr_plot.png")  # Save the plot for 1H
plt.show()

# Plot and save the graph for 19F
plt.figure(figsize=(6, 5))
plt.scatter(B0_F, nu_F, color="blue", label="Experimental data")
plt.plot(B0_F, linear_fit(B0_F, gamma_over_2pi_F), color="red",
         label=f"Fit: γ/2π = {gamma_over_2pi_F:.5f} MHz/mT")
plt.xlabel('B₀ (mT)')
plt.ylabel('ν (MHz)')
plt.title(r'$^{19}$F NMR: ν vs B₀')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("19F_nmr_plot.png")  # Save the plot for 19F
plt.show()

# Constants in SI units
M_proton = 1.67262192369e-27      # kg (proton mass)
e_charge = 1.602176634e-19        # C (elementary charge)
hbar = 1.054571817e-34            # J·s (reduced Planck constant)
pi = np.pi

# Calculate the nuclear magneton μ_N
mu_N = (e_charge * hbar) / (2 * M_proton)  # J/T

# Step 2: Convert γ/2π from MHz/mT to Hz/T
gamma_over_2pi_H_SI = gamma_over_2pi_H * 1e9  # Hz/T
gamma_over_2pi_F_SI = gamma_over_2pi_F * 1e9  # Hz/T

# Step 3: Calculate γ in rad·s⁻¹·T⁻¹
gamma_H = gamma_over_2pi_H_SI * 2 * pi        # rad·s⁻¹·T⁻¹
gamma_F = gamma_over_2pi_F_SI * 2 * pi        # rad·s⁻¹·T⁻¹

# Step 5: Compute the g-factor using g = (γ * ħ) / μ_N
g_factor_H = (gamma_H * hbar) / mu_N
g_factor_F = (gamma_F * hbar) / mu_N

# Accepted g-factors (from NIST)
accepted_g_factor_H = 5.5856946893
accepted_g_factor_F = 5.257733

# Calculate the percentage error for both g-factors
error_percentage_H = abs((g_factor_H - accepted_g_factor_H) / accepted_g_factor_H) * 100
error_percentage_F = abs((g_factor_F - accepted_g_factor_F) / accepted_g_factor_F) * 100

# Output the results
print(f"1H: γ/2π = {gamma_over_2pi_H:.5f} MHz/mT, g = {g_factor_H:.4f}, Error = {error_percentage_H:.4f}%")
print(f"19F: γ/2π = {gamma_over_2pi_F:.5f} MHz/mT, g = {g_factor_F:.4f}, Error = {error_percentage_F:.4f}%")
