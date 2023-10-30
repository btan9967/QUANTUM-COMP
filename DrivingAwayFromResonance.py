import numpy as np
import matplotlib.pyplot as plt
from qutip import *

# Parameters
T = np.pi  # Duration of the pulse for a pi-pulse
Omega = np.pi / T  # Rabi frequency for a pi-pulse
delta_list = np.linspace(-2 * np.pi, 2 * np.pi, 500)  # Detuning frequencies
t_list = np.linspace(0, T, 500)  # Time list

# Initial state
psi0 = basis(2, 0)  # |0>

# Population in |1>
P1_list = []

for delta in delta_list:
    # Time-dependent Hamiltonian in the interaction picture
    H_t = [[(Omega / 2) * sigmax(), 'cos(delta * t)'], [(Omega / 2) * (-sigmay()), 'sin(delta * t)']]
    args = {'delta': delta}
    
    # Solve the Schrödinger equation
    result = mesolve(H_t, psi0, t_list, [], [sigmax(), sigmay(), sigmaz()], args=args)
    
    # Calculate the population in |1> at the final time
    P1 = abs((basis(2, 1).dag() * result.states[-1])[0, 0])**2
    P1_list.append(P1)

# Plotting
plt.figure()
plt.title("Population in |1> as a function of detuning (δ)")
plt.xlabel("Detuning (δ)")
plt.ylabel("Population in |1>")
plt.plot(delta_list, P1_list)
plt.axvline(x=0, color='r', linestyle='--', label="Resonance condition (δ=0)")
plt.legend()
plt.show()
