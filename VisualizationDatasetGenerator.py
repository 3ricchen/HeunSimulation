# Gathers the data for the visualization program
# Intended to only be needed to run once
# Run before the graphical component.
# Set the name of the output file beforehand. Be careful not to overwrite an existing data file
# This program takes most of a day to run. For lower speeds, more passes, and higher resolution,
# (to get more accurate data), budget time accordingly. I personally leave my computer open and plugged in overnight and
# adjusted my computer sleep settings to keep it running.

from main import runpass


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
    for real in range(-size, size+1):
        print(real) # Helpful for knowing how far along the program is
        for imag in range(-size, size+1):
            # Change setEpsilon and setDelta as you wish to experiment with different Heun Equations
            eig = runpass(passes=passes, setBstart=complex(real / res, imag / res), setSpeed=speed, setEpsilon=.625, setDelta=None, seta=a) # Computes the eigenvalue and writes it to the file
            data_out.write("[" + str(eig[1].real) + "," + str(eig[1].imag) + "]")
            if imag != size:
                data_out.write(",")
        data_out.write("\n")
    data_out.close()
# Most recent normal computer run
get_data(-1, name_mod="eigvalsH(.5,.5,.625)",res=4, size=200)

# What I want to try on a supercomputer:

# get_data(1, name_mod="super", passes=50, res=20, speed=.001, size=2000)