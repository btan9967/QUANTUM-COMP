import numpy as np
import matplotlib.pyplot as plt
from qutip import *

# Parameters
omega_0 = 1.0  # Energy separation between |0> and |1>
omega = 1.0  # Frequency of the external field
Delta_t = 1.0  # Time width for the pulse
A = np.pi / Delta_t  # Amplitude for a pi-pulse
t_list = np.linspace(-5 * Delta_t, 5 * Delta_t, 500)  # Time list

# Operators
H1 = (sigmax() + sigmay()) / 2

# Time-dependent Hamiltonian (for sesolve)
H_t = [[H1, lambda t, args: (A / np.cosh(t / Delta_t))**2 * np.cos((omega - omega_0) * t)]]
args = {'Delta_t': Delta_t}

# Initial state
psi0 = basis(2, 0)  # |0>

# sesolve
result_se = sesolve(H_t, psi0, t_list, [sigmax(), sigmay(), sigmaz()], args=args)

# Plotting
plt.figure()
plt.title("Time Evolution of Bloch Vector Components")
plt.plot(t_list, result_se.expect[0], label='X (sesolve)')
plt.plot(t_list, result_se.expect[1], label='Y (sesolve)')
plt.plot(t_list, result_se.expect[2], label='Z (sesolve)')
plt.xlabel('Time')
plt.ylabel('Expectation values')
plt.legend()
plt.show()
