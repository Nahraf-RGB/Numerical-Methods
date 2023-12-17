import numpy as np
import matplotlib.pyplot as plt

# Number of Grid Points
N = 100

# Creating the Meshgrid
x = np.linspace(0, 1, N)
y = np.linspace(0, 1, N)


# Grid Size
dx = 1 / (N - 1)
dy = 1 / (N - 1)

# Setting Initial and Boundary Conditions
# Temperature In Degree Celsius
T_init = 30
T_left = 500
T_top = 30
T_bottom = 30
T_right = 30
colorinterpolation = 50
colorMap = plt.cm.jet

X, Y = np.meshgrid(x, y)


# Initialize temperature matrix
T = np.full((N, N), T_init)

# Setting Boundary Conditions
T[0:N, 0] = T_left
T[0, 1:N] = T_top
T[-1, 1:N] = T_bottom
T[0:N, -1] = T_right

# Setting error
Init_error = 1
Convergence = 0.00001

# Iteration
itr = 0

while Init_error > Convergence:
    T_old = T.copy()
    for i in range(1, N-1):
        for j in range(1, N-1):
            T[i, j] = 0.25 * (T[i + 1, j] + T[i - 1, j] + T[i, j + 1] + T[i, j - 1])

    itr += 1
    Init_error = np.linalg.norm(T - T_old)

# Plot updated temperature distribution with 'rainbow' colormap
plt.title('contour of temperature of 2d plot')
plt.contourf(X, Y, T,colorinterpolation,cmap = colorMap)

plt.colorbar()
plt.show()
print(T)
