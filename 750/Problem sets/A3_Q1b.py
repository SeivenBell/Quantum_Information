import numpy as np

# Redefine constants and recalculate
e = 1.602e-19  # elementary charge in Coulombs
amu = 1.660e-27  # atomic mass unit in kg
mass_Yb = 171 * amu  # mass of 171Yb+ in kg
f = 22e6  # frequency in Hz
Omega_m = 2 * np.pi * f  # angular frequency in rad/s
s_0 = 0.46e-3  # characteristic size parameter in meters

# RF oscillating electric field amplitudes as amplitude (half of the peak-to-peak value)
# Redefine the V0 values as they are the actual amplitude
V0_amplitude_min = 100  # in V (100 V amplitude)
V0_amplitude_max = 200  # in V (200 V amplitude)

# Recalculate |b_i| for both V0_amplitude_min and V0_amplitude_max using the correct s_0
bi_amplitude_min_corrected = abs(
    (-2 * e * V0_amplitude_min) / (Omega_m**2 * mass_Yb * s_0**2)
)
bi_amplitude_max_corrected = abs(
    (-2 * e * V0_amplitude_max) / (Omega_m**2 * mass_Yb * s_0**2)
)
# Output:

print(f"|b_i| for V0_amplitude_min: {bi_amplitude_min_corrected}")
print(f"|b_i| for V0_amplitude_max: {bi_amplitude_max_corrected}")


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define parameters
b = 0.027
a_range = np.linspace(0, b, int(b / 0.001) + 1)
y0 = [1, 0]  # Initial conditions y(0) = 1 and y'(0) = 0
t_range = [0, 100]  # Time range from 0 to 100
stable_a_values = []  # Initialize an empty list for storing stable 'a' values


# Mathieu equation derivative function
def mathieu_derivative(t, y, a, b):
    dydt = [y[1], -(a - 2 * b * np.cos(2 * t)) * y[0]]
    return dydt


# Main loop to test for stability across different 'a' values
for a in a_range:
    # Solve the Mathieu equation for 'a' and 'b' over the time range 't_range' with initial conditions 'y0'
    sol = solve_ivp(mathieu_derivative, t_range, y0, args=(a, b), max_step=0.1)

    # Check the maximum absolute value of the solution for y over its first component
    max_abs_y = np.max(np.abs(sol.y[0]))

    # If the maximum absolute value is less than or equal to 1.2 (to account for numerical error):
    if max_abs_y <= 1.2:
        stable_a_values.append(a)  # Add 'a' to the list of stable 'a' values

# Output the maximum and minimum of the stable 'a' values found
if stable_a_values:
    min_stable_a = min(stable_a_values)
    max_stable_a = max(stable_a_values)
    print(f"Stable 'a' values range from {min_stable_a} to {max_stable_a}.")
else:
    print("No stable 'a' values found.")
