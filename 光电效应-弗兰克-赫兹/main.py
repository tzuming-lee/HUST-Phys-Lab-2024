import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# --- Photoelectric Effect Plot: Stopping Voltage vs Frequency ---
# Data for wavelengths, frequencies, and stopping voltages
frequencies = np.array([8.214, 7.408, 6.879, 5.490, 5.196]) * 1e14  # in Hz
stopping_voltages = np.array([-1.7145, -1.3820, -1.1455, -0.59825, -0.4910])  # in V

# Plotting frequency vs stopping voltage
plt.figure(figsize=(8, 6))
plt.scatter(frequencies, stopping_voltages, color='b', label='Experimental Data')
coefficients = np.polyfit(frequencies, stopping_voltages, 1)
fit_line = np.polyval(coefficients, frequencies)
plt.plot(frequencies, fit_line, color='r', label=f'Fit: y = {coefficients[0]:.2e}x + {coefficients[1]:.2f}')
plt.title('Stopping Voltage vs Frequency')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Stopping Voltage (V)')
plt.legend()
plt.grid(True)
plt.savefig('stopping_voltage_vs_frequency.png')
plt.show()

# --- Photoelectric Effect Plot: I-U Curves ---
# Voltage and current data for two conditions: 436nm and 546nm
voltage_ranges = np.array([-4, -3.5, -3, -2.5, -2, -1.5, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 
                           17.5, 19, 20.5, 22, 23.5, 25, 26.5, 28, 29.5, 30])
current_436nm = np.array([-3.3, -3.3, -3.2, -3.2, -3.0, -2.5, 10.5, 136, 301, 858, 1520, 2150, 2580, 
                          3090, 3430, 3680, 3910, 4170, 4380, 4590, 4820, 5050, 5290, 5510, 5810, 
                          6080, 6320, 6540, 6740, 6940, 7110, 7260, 7440, 7530]) * 1e-13  # in A
current_546nm = np.array([-2.8, -2.8, -2.7, -2.7, -2.7, -2.6, -2.5, 10.8, 196, 704, 1450, 1950, 2300, 
                          2530, 2700, 2820, 2980, 3170, 3340, 3510, 3660, 3800, 3920, 4040, 4180, 
                          4310, 4440, 4560, 4670, 4770, 4860, 4930, 4990, 5030]) * 1e-13  # in A

# Plotting I-U curves
plt.figure(figsize=(8, 6))
plt.plot(voltage_ranges, current_436nm, marker='o', linestyle='-', color='b', label='436nm')
plt.plot(voltage_ranges, current_546nm, marker='o', linestyle='-', color='r', label='546nm')
plt.title('I-U Curves for 436nm and 546nm')
plt.xlabel('Voltage (V)')
plt.ylabel('Current ($10^{-13}$ A)')
plt.grid(True)
plt.legend()
plt.savefig('IU_curves.png')
plt.show()

# --- Photoelectric Effect Plot: Im-P Curves with Linear Fits ---
aperture_diameters = np.array([2, 4, 8])  # in mm
current_436nm_im_p = np.array([7.267, 29.767, 104.267])  # in 10^-10 A
current_546nm_im_p = np.array([1.2, 4.9, 18.2])  # in 10^-10 A
relative_light_intensity = aperture_diameters**2

# Linear fits
coeff_436nm = np.polyfit(relative_light_intensity, current_436nm_im_p, 1)
fit_line_436nm = np.polyval(coeff_436nm, relative_light_intensity)

coeff_546nm = np.polyfit(relative_light_intensity, current_546nm_im_p, 1)
fit_line_546nm = np.polyval(coeff_546nm, relative_light_intensity)

# Plotting Im-P curves for both wavelengths with linear fits
plt.figure(figsize=(8, 6))
plt.plot(relative_light_intensity, current_436nm_im_p, marker='o', linestyle='-', color='b', label='436nm Data')
plt.plot(relative_light_intensity, fit_line_436nm, linestyle='--', color='b', 
         label=f'436nm Fit: y={coeff_436nm[0]:.2f}x + {coeff_436nm[1]:.2f}')
plt.plot(relative_light_intensity, current_546nm_im_p, marker='o', linestyle='-', color='r', label='546nm Data')
plt.plot(relative_light_intensity, fit_line_546nm, linestyle='--', color='r', 
         label=f'546nm Fit: y={coeff_546nm[0]:.2f}x + {coeff_546nm[1]:.2f}')
plt.title('Im-P Curves with Linear Fits for Different Wavelengths')
plt.xlabel('Relative Light Intensity ($\Phi^2$)')
plt.ylabel('Current (10$^{-10}$ A)')
plt.grid(True)
plt.legend()
plt.savefig('Im_P_curves_with_fits.png')
plt.show()

# --- Ip-VG2K Curve ---
VG2K = np.concatenate([np.arange(0, 5, 1), np.arange(4.5, 60.5, 0.5)])
Ip = np.array([0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 18, 21, 24, 26, 27, 
               27, 26, 26, 27, 31, 37, 42, 46, 47, 45, 42, 40, 41, 45, 54, 63, 70, 72, 69, 63, 58, 58, 63, 73, 
               85, 95, 100, 98, 90, 83, 80, 83, 92, 104, 117, 126, 128, 122, 113, 106, 105, 110, 121, 134, 146, 
               153, 154, 147, 138, 131, 131, 137, 148, 161, 173, 180, 180, 174, 165, 158, 158, 165, 176, 189, 
               199, 206, 207, 203, 195, 189, 188, 194, 204, 216, 226, 233, 235, 232, 226, 221, 220, 225, 233, 
               244, 253, 261, 264, 263])
VG2K_final = np.concatenate([VG2K, [59.5, 60.0]])
Ip_final = np.concatenate([Ip, [264, 263]])

# Plotting the Ip-VG2K curve
plt.figure(figsize=(10, 6))
plt.plot(VG2K_final, Ip_final, marker='o', linestyle='-', color='b', label='Ip vs VG2K')
plt.title('Ip-VG2K Curve')
plt.xlabel('VG2K (V)')
plt.ylabel('Plate Current (Ip)')
plt.grid(True)
plt.legend()
plt.savefig('Ip_VG2K_curve.png')
plt.show()
