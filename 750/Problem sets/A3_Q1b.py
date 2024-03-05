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



