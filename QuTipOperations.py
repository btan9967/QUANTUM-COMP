import numpy as np
import qutip as qt
import matplotlib
matplotlib.use('TkAgg') 

sx = qt.sigmax()
sy = qt.sigmay()
sz = qt.sigmaz()

print("Pauli X matrix:")
print(sx)
print("Pauli Y matrix:")
print(sy)
print("Pauli Z matrix:")
print(sz)

psi1 = qt.basis(2, 0)  # |↑⟩ state
expect_sz_psi1 = qt.expect(sz, psi1)
print(f"Expectation value of S_z for |ψ1⟩: {expect_sz_psi1}")

psi2 = (qt.basis(2, 0) + qt.basis(2, 1)).unit()  # Normalized state
expect_sz_psi2 = qt.expect(sz, psi2)
print(f"Expectation value of S_z for |ψ2⟩: {expect_sz_psi2}")

delta_sz_psi1 = np.sqrt(qt.variance(sz, psi1))
delta_sz_psi2 = np.sqrt(qt.variance(sz, psi2))

print(f"Uncertainty in S_z for |ψ1⟩: {delta_sz_psi1}")
print(f"Uncertainty in S_z for |ψ2⟩: {delta_sz_psi2}")

b = qt.Bloch()
b.add_states([psi1, psi2])
b.add_annotation(psi1, text='|ψ1⟩ (Spin up)', color='red')
b.show()

input("Press Enter to continue...")