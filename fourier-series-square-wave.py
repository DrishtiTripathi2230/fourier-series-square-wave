import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square
from scipy.integrate import quad

# Define the function f(x)
def f(x):
    return square(x)  # Square wave function

# Define x values
x = np.linspace(-np.pi, np.pi, 1000)  # Use linspace for better accuracy
y = f(x)  # Original function values

n = 50  # Number of terms in Fourier series
fourier_sum = np.zeros_like(x)  # Initialize as an array

# Coefficients lists
an = []
bn = []

# Compute Fourier coefficients
for i in range(n):
    f1 = lambda x: f(x) * np.cos(i * x)
    f2 = lambda x: f(x) * np.sin(i * x)

    a_n = (1.0 / np.pi) * quad(f1, -np.pi, np.pi)[0]
    b_n = (1.0 / np.pi) * quad(f2, -np.pi, np.pi)[0]

    an.append(a_n)
    bn.append(b_n)

# Construct Fourier series approximation
for i in range(n):
    if i == 0:
        fourier_sum += an[i] / 2  # a0/2 term
    else:
        fourier_sum += an[i] * np.cos(i * x) + bn[i] * np.sin(i * x)

# Plot results
plt.title("Fourier Series Approximation of a Square Wave")
plt.xlabel("x")
plt.ylabel("y=f(x)")

# Original function
plt.plot(x, y, 'r-.', label="Original Square Wave", linewidth=2)

# Fourier series approximation
plt.plot(x, fourier_sum, "g--", label=f"Fourier Approximation (n={n})", linewidth=2)

plt.legend()
plt.grid()
plt.show()
