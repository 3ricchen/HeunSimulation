import pandas as pd
import numpy as np
from main import newrunpass, runpass
import multiprocessing as mp

# eigs = pd.read_csv('EigData/eiglist0.125.csv', header = None)
# eigs = eigs.to_numpy()
eigs = []
for i in range(-5,5):
    for j in range(-5,5):
        eigs.append(i + j * 1j)
# for i in eigs:
#     MSet,B = newrunpass(passes=30, setBstart= complex(i), setSpeed=0.0005, setEpsilon = 0.125, setDelta=0.50) # Computes the eigenvalue and writes it to the file
#     print(B)
#     print(complex(i))
MSet,B = newrunpass(passes=-1, setBstart= 7, setSpeed=0.001, setGamma = 0.5, setEpsilon = 0.125, setDelta=0.50) # Computes the eigenvalue and writes it to the file
#MSet,B = runpass(passes=30, setBstart= 5-1j, setSpeed=0.0001, setEpsilon = 0.125, setDelta=0.50) # Computes the eigenvalue and writes it to the file

P = MSet[0]
Q = MSet[1]
R = MSet[2]

lP = np.exp(-np.pi * 1j * 0.5)
lQ = np.exp(-np.pi * 1j * 0.5)
lR = np.exp(-np.pi * 1j * 0.125)
print('MATRICES')
print(P)
print(Q)
print(R)
print('B')
print(B)
print(np.linalg.det(P))
print(np.linalg.det(Q))
print(np.linalg.det(R))

print(P*R)
#print(np.linalg.eigvals(R))
print(np.trace(P*R)/(lP*lR))
print(np.trace(Q*R)/(lQ*lR))
print(np.trace(P*Q)/(lP*lQ))