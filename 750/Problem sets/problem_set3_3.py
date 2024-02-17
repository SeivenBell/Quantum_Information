import numpy as np
import matplotlib.pyplot as plt


# Function to calculate energies for a qubit
def energies(Ec, Ej, n_g):
    H = np.zeros((2, 2))
    H[0, 1] = H[1, 0] = -Ej / 2
    H[0, 0] = 4 * Ec * (0 - n_g) ** 2
    H[1, 1] = 4 * Ec * (1 - n_g) ** 2
    return np.sort(np.linalg.eigvals(H))


# Function to compute energy bands
def compute_energy_bands(n_g_range, EC_EJ_ratio):
    energy_bands = []
    E_C = 1  # Normalize E_C for simplicity, adjust E_J accordingly

    for n_g in n_g_range:
        E_J = E_C / EC_EJ_ratio  # Calculate E_J based on the given EC/EJ ratio
        H = np.array(
            [
                [4 * E_C * (-1 - n_g) ** 2, -E_J / 2, 0],
                [-E_J / 2, 4 * E_C * (0 - n_g) ** 2, -E_J / 2],
                [0, -E_J / 2, 4 * E_C * (1 - n_g) ** 2],
            ]
        )
        energies = np.linalg.eigvalsh(H)
        energy_bands.append(energies)

    return np.array(energy_bands)


# Example: Calculate and plot energy bands
n_g_range = np.linspace(-1, 1, 200)
EC_EJ_ratios = [5, 1, 1 / 5]

# Plotting energy bands
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for idx, ratio in enumerate(EC_EJ_ratios):
    energy_bands = compute_energy_bands(n_g_range, ratio)
    for band in range(3):  # Plot the three lowest bands
        axes[idx].plot(n_g_range, energy_bands[:, band], label=f"Band {band+1}")
    axes[idx].set_xlabel("$n_g$")
    axes[idx].set_ylabel("Energy")
    axes[idx].set_title(f"$E_J/E_C = {1/ratio}$")
    axes[idx].legend()
    axes[idx].grid(True)

plt.tight_layout()
plt.show()
