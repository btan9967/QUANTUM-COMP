import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Read data from Excel
df = pd.read_excel('Rabi_Data.xlsx')
frequency = df.iloc[:, 0].values # Frequency in Hz
probability = df.iloc[:, 1].values # Probability of being in state 1

# Convert frequency to angular frequency
omega_d = 2 * np.pi * frequency

# Define the model function
def model_func(t, A, Omega, Delta, C):
    return A * (Omega ** 2 / (Omega ** 2 + Delta ** 2)) * np.sin(np.sqrt(Omega ** 2 + Delta ** 2) * t / 2) ** 2 + C

# Initial guess for [A, Omega, Delta, C]
initial_guess = [max(probability), 2 * np.pi * 5e6, 2 * np.pi * 1e6, min(probability)]

# Perform curve fitting
params, params_covariance = curve_fit(model_func, omega_d, probability, p0=initial_guess)

# Extract parameters
A, Omega, Delta, C = params

# Calculate uncertainties
params_std_dev = np.sqrt(np.diag(params_covariance))

# Convert to Hz for human readability
Omega_hz = Omega / (2 * np.pi)
Delta_hz = Delta / (2 * np.pi)

# Print results
print(f"Amplitude A = {A}")
print(f"Rabi Frequency Omega = {Omega} rad/s or {Omega_hz} Hz")
print(f"Detuning Delta = {Delta} rad/s or {Delta_hz} Hz")
print(f"Constant offset C = {C}")
print(f"Uncertainties: {params_std_dev}")

# Plot the data and the fit
plt.scatter(omega_d, probability, label='Data')
plt.plot(omega_d, model_func(omega_d, A, Omega, Delta, C), label='Fitted function')
plt.legend(loc='best')
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Probability')
plt.title('Rabi Spectroscopy')
plt.show()
