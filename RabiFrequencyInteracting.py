import numpy as np
import matplotlib.pyplot as plt
from qutip import *

# Parameters
T = 1.0  # Duration of the pulse
omega_list = np.linspace(0.5 * np.pi, 2 * np.pi, 500)  # Rabi frequencies

# Initial state
psi0 = basis(2, 0)  # |0>

# Population in |1>
P1_list = []

for omega in omega_list:
    U = (-1j * omega * T / 2 * sigmax()).expm()  # Time evolution operator
    P1 = abs((basis(2, 1).dag() * U * psi0)[0, 0])**2  # Population in |1>
    P1_list.append(P1)

# Plotting
plt.figure()
plt.title("Population in |1> as a function of Ω")
plt.xlabel("Ω")
plt.ylabel("P1")
plt.plot(omega_list, P1_list)
plt.axvline(x=np.pi, color='r', linestyle='--', label="π-pulse condition")
plt.legend()
plt.show()
