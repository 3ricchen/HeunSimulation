import pandas as pd
import numpy as np
from main import newrunpass, runpass, testrunpass
import multiprocessing as mp


eigs = pd.read_csv('EigData/eiglist0.125.csv', header = None)
eigs = eigs.to_numpy()
res = []
for k in eigs:
    eig = complex(k)
    ap = [eig, testrunpass(setBstart = eig, setSpeed = 0.001, setDelta = 0.5, setEpsilon = 0.125)]
    res.append(ap)
print(res)