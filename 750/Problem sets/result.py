import numpy as np


def energies(Ec, Ej, n_g):
    """
    Calculate the eigenvalues of the Hamiltonian for given Ec, Ej, and n_g.
    """
    H = np.zeros((2, 2))
    H[0, 1] = H[1, 0] = -Ej / 2
    H[0, 0] = 4 * Ec * (0 - n_g) ** 2
    H[1, 1] = 4 * Ec * (1 - n_g) ** 2
    return np.sort(np.linalg.eigvals(H))


# Defining Variables
n_g = 1 / 2
ratio = np.arange(0.01, 100.01, 0.01)

# Setting constants
Ej = 8e-23  # Joules
h_bar = (1 / (2 * np.pi)) * 6.626070e-34  # Joule seconds

# Calculate Ec values
Ec = ratio * Ej

# Target difference in energy
target_diff = 8e10 * h_bar

# Initialize arrays for storing energy differences and eigenvalues
E_diff = np.zeros(len(ratio))
values = np.zeros((2, len(ratio)))

# Calculate energy differences for each ratio
for i, ec in enumerate(Ec):
    eigvals = energies(ec, Ej, n_g)
    values[:, i] = eigvals
    E_diff[i] = eigvals[1] - eigvals[0]

# Find the index of the minimum difference from the target
idx = np.argmin(np.abs(E_diff - target_diff))

# Extract desired values
desired_Ec = Ec[idx]
desired_ratio = ratio[idx]
split_Hz = E_diff[idx] / h_bar

# Output the results
print(
    f"Ej: {Ej}, Ec: {desired_Ec}, Ratio: {desired_ratio}, Resulting Freq = {split_Hz} Hz"
)
print(f"E1 = {values[1, idx]}, E0 = {values[0, idx]}")
