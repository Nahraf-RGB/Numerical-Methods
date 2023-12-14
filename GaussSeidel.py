import numpy as np

A = np.array([[12, 3, -5], [1, 5, 3], [3, 7, 13]])
b = np.array([1, 28, 76])
B = b.reshape(3, 1)

conv = 0.0001

x = np.zeros_like(b, dtype=float).reshape(3, 1)  # Initialize x to zeros

init = 1

itr = 0

while init > conv:
    x_old = x.copy()
    for i in range(0,A.shape[0]):
        sum = 0
        for j in range(0,A.shape[0]):
            if j != i:
                sum += A[i][j] * x[j]

        x[i] = (B[i] - sum) / A[i][i]

    itr += 1
    print("Iteration:", itr)

    init = np.linalg.norm(x - x_old)

print("Final Solution:")
print(x)
