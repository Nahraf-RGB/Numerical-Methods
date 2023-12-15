import numpy as np
import matplotlib.pyplot as plt

# Define number of grid points
N = 10
# Setting initial conditions
T_init = 30

T = np.full(N, T_init)

T[0] = 500  # Left Hand Side Temperature of Rod
T[-1] = 300  # Right Hand Side Temperature of Rod

# Setting error
Init_Error = 1
Tolerance = 0.000001

# Iteration counter
itr = 0

x_values = np.linspace(0, 1, N)  # Assuming the rod spans from 0 to 1

while Init_Error > Tolerance:
    T_old = T.copy()
    for i in range(1, N - 1):
        # Discretized 1D Diffusion equation in 2nd order
        T[i] = 0.5 * (T[i + 1] + T[i - 1])

    itr += 1

    print("Iteration:", itr)

    Init_Error = np.linalg.norm(T - T_old)

# Plotting the temperature distribution versus position
plt.plot(x_values, T, marker='o')
plt.xlabel('Position along the rod')
plt.ylabel('Temperature')
plt.title('Temperature Distribution in the Rod')
plt.grid(True)
plt.show()
