import numpy as np
import matplotlib.pyplot as plt
from qutip import *

# Parameters
omega_0 = 1.0  # Energy separation between |0> and |1>
omega = 1.0  # Frequency of the external field
Omega = np.pi  # Rabi frequency for a pi-pulse
t_list = np.linspace(0, np.pi/Omega, 500)  # Time list

# Operators
H1 = (Omega / 2) * (sigmax() + sigmay())

# Initial state
psi0 = basis(2, 0)  # |0>

# Time-dependent Hamiltonian (for sesolve)
H_t = [[H1, 'cos(w * t)']]
args = {'w': omega - omega_0}

# sesolve
result_se = sesolve(H_t, psi0, t_list, [sigmax(), sigmay(), sigmaz()], args=args)

# mcsolve
result_mc = mcsolve(H_t, psi0, t_list, [], [sigmax(), sigmay(), sigmaz()], args=args, ntraj=200)

# mesolve (no collapse operators for a closed system)
result_me = mesolve(H_t, psi0, t_list, [], [sigmax(), sigmay(), sigmaz()], args=args)

# Check the shape of the Monte Carlo results
print("Shape of Monte Carlo results:", np.array(result_mc.expect[0]).shape)

# Plotting
plt.figure()
plt.title("Time Evolution of Bloch Vector Components")
plt.plot(t_list, result_se.expect[0], label='X (sesolve)')
plt.plot(t_list, result_se.expect[1], label='Y (sesolve)')
plt.plot(t_list, result_se.expect[2], label='Z (sesolve)')
plt.plot(t_list, result_me.expect[0], ':', label='X (mesolve)')
plt.plot(t_list, result_me.expect[1], ':', label='Y (mesolve)')
plt.plot(t_list, result_me.expect[2], ':', label='Z (mesolve)')
plt.xlabel('Time')
plt.ylabel('Expectation values')
plt.legend()
plt.show()
