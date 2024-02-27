import pandas as pd
import numpy as np
from main import newrunpass, runpass, boltzmannRunpass
import multiprocessing as mp
import time

# eigs = pd.read_csv('EigData/eiglist0.125.csv', header = None)
# eigs = eigs.to_numpy()

# eigs = []
# for i in range(-5,5):
#     for j in range(-5,5):
#         eigs.append(i + j * 1j)
# for i in eigs:
#     MSet,B = newrunpass(passes=30, setBstart= complex(i), setSpeed=0.0005, setEpsilon = 0.125, setDelta=0.50) # Computes the eigenvalue and writes it to the file
#     print(B)
#     print(complex(i))
starttime = time.time()
#MSet, B = boltzmannRunpass(passes=-1, setBstart= 20, setSpeed=0.001, setGamma = 0.5, setEpsilon = 0.75, setDelta=0.25)
MSet,B = newrunpass(passes=-1, setBstart= 5 - 1j, setSpeed=0.001, setGamma = 0.5, setEpsilon = 0.25, setDelta=0.75) # Computes the eigenvalue and writes it to the file
#MSet,B = runpass(passes=30, setBstart= 5-1j, setSpeed=0.0001, setEpsilon = 0.25, setDelta=0.75) # Computes the eigenvalue and writes it to the file


endtime = time.time()

lP = np.exp(-np.pi * 1j * 0.5)
lQ = np.exp(-np.pi * 1j * 0.75)
lR = np.exp(-np.pi * 1j * 0.25)

P = MSet[0]
Q = MSet[1]
R = MSet[2]

p = np.trace(P/lP)
q = np.trace(Q/lQ)
r = np.trace(R/lR)

tau = np.trace(P*Q/(lP*lQ))
sigma = np.trace(P*R/(lP*lR))
rho = np.trace(Q*R/(lQ*lR))

a = tau**2 + q**2 + p **2 - 2 * p * tau * q - 4
b = sigma**2 + r**2 + p**2 - 2*p*sigma*r - 4
c = Q[0,1] * R[1,0] + Q[1,0] * R[0,1]


print('ABC TIME!!')
print(a)
print(b)
print(c)

print('\n')


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

print('TOTAL TIME:')
print(endtime - starttime)