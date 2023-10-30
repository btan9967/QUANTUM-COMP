import numpy as np
import matplotlib.pyplot as plt

# Constants
omega = 2 * np.pi * 1  # Angular frequency in rad/s
m = 2  # Mass in kg
t = np.linspace(0, 1, 500)  # Time from 0 to 1 second

# Initial conditions
initial_conditions = [
    {'x0': 1, 'v0': 0, 'label': 'Case i'},
    {'x0': 0, 'v0': 1, 'label': 'Case ii'},
    {'x0': 1, 'v0': 1, 'label': 'Case iii'}
]

# Create plots
fig, axs = plt.subplots(3, 2, figsize=(12, 18))

for i, ic in enumerate(initial_conditions):
    x0 = ic['x0']
    v0 = ic['v0']
    label = ic['label']

    # Calculate amplitude and phase from initial conditions
    A = np.sqrt(x0 ** 2 + (v0 / omega) ** 2)
    phi = np.arctan2(-v0, omega * x0)

    # Position and momentum as functions of time
    x_t = A * np.cos(omega * t + phi)
    p_t = m * (-A * omega * np.sin(omega * t + phi))

    # Plot position and momentum
    axs[i, 0].plot(t, x_t, label=f"{label}: x(t)")
    axs[i, 0].set_xlabel('Time (s)')
    axs[i, 0].set_ylabel('Position (m)')
    axs[i, 0].legend()

    axs[i, 1].plot(t, p_t, label=f"{label}: p(t)")
    axs[i, 1].set_xlabel('Time (s)')
    axs[i, 1].set_ylabel('Momentum (kg m/s)')
    axs[i, 1].legend()

    # Phase space plot (x, p)
    axs[i, 1].plot(x_t, p_t, label=f"{label}: Phase Space")
    axs[i, 1].set_xlabel('Position (m)')
    axs[i, 1].set_ylabel('Momentum (kg m/s)')
    axs[i, 1].legend()

plt.tight_layout()
plt.show()
