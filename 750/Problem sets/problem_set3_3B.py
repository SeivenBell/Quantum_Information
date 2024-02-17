import numpy as np
import matplotlib.pyplot as plt


def compute_energy_bands(n_g_range, EC_EJ_ratio):
    energy_bands = []
    E_C = 1  # Normalize E_C for simplicity, adjust E_J accordingly

    for n_g in n_g_range:
        E_J = E_C / EC_EJ_ratio  # Calculate E_J based on the given EC/EJ ratio

        # Construct the 3x3 Hamiltonian matrix for the given n_g
        H = np.array(
            [
                [4 * E_C * (-1 - n_g) ** 2, -E_J / 2, 0],
                [-E_J / 2, 4 * E_C * (0 - n_g) ** 2, -E_J / 2],
                [0, -E_J / 2, 4 * E_C * (1 - n_g) ** 2],
            ]
        )

        # Diagonalize the Hamiltonian to find the eigenvalues (energy levels)
        energies = np.linalg.eigvalsh(H)

        # Append the energy levels
        energy_bands.append(energies)

    return np.array(energy_bands)


# n_g range from -1 to 1
n_g_range = np.linspace(-1, 1, 200)

# Ratios of EC/EJ to explore
EC_EJ_ratios = [5, 1, 1 / 5]

# Plotting
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
