import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    cp=0
    for i in range(len(Y)):
        cp +=-Y[i] * np.log(P[i]) -(1-Y[i])*np.log(1-P[i])
        
    return cp
