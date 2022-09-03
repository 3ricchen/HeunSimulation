# Helper functions for compiling, processing and refining lists actual eigenvalues.
# Used to collect the values for our tables

import statistics
from main import *

def investigate(eigenvalue, epsilon, delta):
    # Refines a potential eigenvalue to a more exact one by averaging the results of many convergences taken from similar locations
    investigating = eigenvalue
    print("Investigating: " + str(investigating))
    reals = []
    imags = []
    for i in range(-3, 5, 2):
        for j in range(-3, 5, 2):
            val = runpass(passes=30, setBstart=investigating + complex(i / 200, j / 200), setSpeed=.003, setEpsilon=epsilon, setDelta=delta)[1]
            print(val, end=",\n")
            reals.append(val.real)
            imags.append(val.imag)
    if max(statistics.stdev(reals), statistics.stdev(imags)) < .5: # Throws out wildly random and variable data
        return complex(statistics.mean(reals), statistics.mean(imags))
    return None

def compileEigenvalues(epsilon, delta=.5):
    # Runs through the refining process for all the possible eigenvalues for a particular epsilon (and delta)
    print("started")
    data = []
    vals = []
    loading_data = open("Data/eigenvaluedata200_eigvalsH"+str(delta)[1:]+".5"+str(epsilon)[1:]+"-1.csv").read() # [1:] to remove the leading 0
    for line in loading_data.splitlines():  # Reads in all of the eigenvalue data from the file (this is kinda a botched csv since there are
        # lists as elements requiring bracket layers to parse
        in_braket = False
        index = 0
        out = []
        piece = ""
        while index < len(line):
            if not in_braket:
                if line[index] == "[":
                    in_braket = True
                    piece = ""
            else:
                if line[index] == "]":
                    in_braket = False
                    out.append(piece.split(","))
                else:
                    piece += line[index]
            index += 1
        data.append(out)
    print("data loaded")
    x = 0
    for line in data:
        y = 0
        for cord in line:
            try:
                real_eig = float(cord[0])
                real_x = (x-200)/4
                imag_eig = float(cord[1])
                imag_y = (y-200)/4
                if abs(real_eig - real_x) < .5 and abs(imag_eig - imag_y) < .5:
                    print(str([real_x,imag_y]))
                    print(cord)
                    if not isThere(complex(real_eig,imag_eig), vals):
                        print("there")
                        next = investigate(complex(real_eig,imag_eig), epsilon, delta)
                        if next != None and not isThere(next, vals):
                            vals.append(next)
                            print("added")
                    else:
                        print("not there")
            except:
                print()
                print("fail")
                print(x)
                print(y)
                print(cord)
                print()
                pass
            y += 1
        x += 1
    file_out = open("Data/eiglist" + str(epsilon) + ".csv","w")
    for val in vals:
        file_out.write(str(val) + "\n")
    file_out.close()

def isThere(val, list): # Returns if an item is similar to another in a list
    for item in list:
        if abs(val.real- item.real) < 1 and abs(val.imag-item[1].imag) < 1:
            return True
    return False

compileEigenvalues(.5) # Compiles the eigenvalues for the Lame equation (epsilon = .5)