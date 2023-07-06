# Gathers the data for the visualization program
# Intended to only be needed to run once
# Run before the graphical component.
# Set the name of the output file beforehand. Be careful not to overwrite an existing data file
# This program takes most of a day to run. For lower speeds, more passes, and higher resolution,
# (to get more accurate data), budget time accordingly. I personally leave my computer open and plugged in overnight and
# adjusted my computer sleep settings to keep it running.

from main import runpass, testQuadTraces
import numpy as np


def get_data(a, name_mod = "", passes=20, res=4, speed=.01, size=200):
    '''
    get_data
    =================
    Produces a file containing convergence data for a sizexsize square around the origin

    Parameters:
    -----------
    a: The value of a to be used in the Heun Equation
    name_mod: An optional additional name modifier
    passes: The number of recursive passes of main.runpass per pixel
    res: pixels per unit in the resulting output dataset
    speed: speed used in main.runpass calls
    size: The number of pixels it extends from the origin in both directions

    Returns:
    ----------
    None
    '''
    data_out = open("./Data/eigenvaluedata"+str(size)+"_"+name_mod+str(a)+".csv", "w") # Opens the output file to write to
    #data_out = open("./Data/TestForQuadraticTraceThm.csv", "w")  # Opens the output file to write to
    for real in range(-44, -42):
        print(real) # Helpful for knowing how far along the program is
        for imag in range(-size, size+1):
            # Change setEpsilon and setDelta as you wish to experiment with different Heun Equations
            MSet, B = runpass(passes=passes, setBstart=complex(real / res, imag / res), setSpeed=speed, setEpsilon = 0.25, setDelta=0.75) # Computes the eigenvalue and writes it to the file
            #print(MSet)
            a,b,c = testQuadTraces(MSet[0], MSet[1], MSet[2])
            #print(str(a) + ' ' + str(b) + ' ' + str(c))
            if a>=0 and b>= 0 and c<= 0:
                testQuad = "TRUE"
            else:
                testQuad = "FALSE"
            #data_out.write("[" + str(a) + "," + str(b) + "," + str(c) + "," + testQuad + "]")
            data_out.write("[" + str(B.real) + "," + str(B.imag) + "]")
            if imag != size:
                data_out.write(",")
        data_out.write("\n")
    data_out.close()
# Most recent normal computer run
#get_data(-1, name_mod="eigvalsH(.5,.25,.75)TESTING",res=4, size=150)

gam = 0.5
eps = 0.5
delt = 0.125

MSet, B = runpass(passes=100, setBstart=complex(50 / 4, 150 / 4), setSpeed=0.001, setEpsilon = 0.5, setDelta=0.125)

P = MSet[0]
Q = MSet[1]
R = MSet[2]

lP = np.sqrt(np.linalg.det(P))
lQ = np.sqrt(np.linalg.det(Q))
lR = np.sqrt(np.linalg.det(R))

x = Q*R/(lQ*lR)
print(x[0,0] + x[1,1])





# What I want to try on a supercomputer:

# get_data(1, name_mod="super", passes=50, res=20, speed=.001, size=2000)

#LAST RUN WAS ON -44!! FOR 7/5/2023