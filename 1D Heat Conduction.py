#BASIC 1D HEAT CONDUCTION PROBLEM

import numpy as np

#define number of grid points
N = 10
#setting initial conditions
T_init = 30

T = np.full(N, T_init)

T[0] = 500 # Left Hand Side Temperature of Rod
T[-1] = 300 # Right Hand Side Temperature of Rod

#setting error

Init_Error = 1
Tolerance = 0.000001

#iteration counter

itr = 0

while Init_Error > Tolerance:
    T_old = T.copy()
    for i in range(1,N-1):
        
        # discretized 1D Diffusion equation in 2nd order
        T[i] = 0.5*(T[i+1]+T[i-1])
        
    itr+=1
    
    print("Iteration:", itr)

    Init_Error = np.linalg.norm(T - T_old)
    
print('Temperature Distribution : ')
print(T)
        
    
    


