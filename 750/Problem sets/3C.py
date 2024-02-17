import numpy as np
import scipy.constants as sc
from scipy.linalg import eigh

# Constants
hbar = sc.hbar  # Reduced Planck's constant in J*s
target_frequency = 8e9  # Target qubit splitting in Hz (8 GHz)
target_energy = hbar * target_frequency  # Target qubit splitting in Joules

# Initialization
n_g = 1 / 2
ratio = np.arange(0, 10, 1e-2)  # Coarser step for initial search
Ec = 1e-10  # Small non-zero value for Ec to avoid division by zero
Ej = ratio / Ec


# Function to compute the energy levels of the Hamiltonian
def energies(Ec, Ej, n_g):
    H = np.array(
        [[4 * Ec * (0 - n_g) ** 2, -Ej / 2], [-Ej / 2, 4 * Ec * (1 - n_g) ** 2]]
    )
    vals, _ = np.linalg.eigh(H)
    return vals


# Compute energies and energy differences for all Ej values
values = np.array([energies(Ec, ej, n_g) for ej in Ej])
E_diff = hbar * (values[:, 1] - values[:, 0])

# Find the Ej that gives a qubit splitting closest to the target
diff = np.abs(E_diff - target_energy)
idx = np.argmin(diff)

# Desired values
desired_Ej = Ej[idx]
desired_ratio = ratio[idx]
split_Hz = E_diff[idx] / hbar

# Output
output = {
    "Ec": Ec,
    "Ej": desired_Ej,
    "Resulting Freq (Hz)": split_Hz,
    "E1": values[idx, 1],
    "E0": values[idx, 0],
    "Desired Ratio Ec/Ej": desired_ratio,
}

print(output)
