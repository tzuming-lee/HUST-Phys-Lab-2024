
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
plt.rcParams['font.family']='Source Han Serif'
# Data for t and R_x (resistance)
t_values = [28.1, 31.1, 34.1, 37.1, 40.1, 43.1, 46.1, 49.1, 52.1, 55.1]
R_values = [56.18, 56.66, 57.3, 57.94, 58.58, 59.22, 59.86, 60.51, 61.15, 61.79]

# Define the resistance model R(t) = R_0(1 + alpha * t)
def resistance_model(t, R_0, alpha):
    return R_0 * (1 + alpha * t)

# Perform curve fitting to find R_0 and alpha
params, covariance = curve_fit(resistance_model, t_values, R_values)
R_0, alpha = params

# Convert t_values to a numpy array for element-wise operations
t_values_np = np.array(t_values)

# Calculate fitted R_x values using the model
fitted_model_R_values = resistance_model(t_values_np, R_0, alpha)

# Plotting the data and fitted curve
plt.figure(figsize=(8, 6))

# Plot the original data
plt.plot(t_values, R_values, 'bo', label='原始数据')

# Plot the fitted curve
plt.plot(t_values, fitted_model_R_values, 'r-', label='拟合曲线')

# Label the axes with units and add the title
plt.title('铜电阻温度特性曲线')
plt.xlabel('t (°C)')
plt.ylabel('$R_x$ (Ω)')
plt.grid(True)
plt.legend()

# Display the equation in the plot
equation_text = f'$R_x(t) = {R_0:.4f}(1 + {alpha:.4f}t)$'
plt.text(30, 60.5, equation_text, fontsize=12, color='black')

# Save the plot as a PNG file
plt.savefig('铜电阻温度特性曲线.png')

# Show the plot
plt.show()
