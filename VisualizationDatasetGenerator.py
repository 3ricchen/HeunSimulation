# Gathers the data for the visualization program
# Intended to only be needed to run once
# Run before the graphical component.
# Set the name of the output file beforehand. Be careful not to overwrite an existing data file
# This program takes most of a day to run. For lower speeds, more passes, and higher resolution,
# (to get more accurate data), budget time accordingly. I personally leave my computer open and plugged in overnight and
# adjusted my computer sleep settings to keep it running.

from main import runpass

# Gathering data: Stored in a 201x201 array

#data = []
#for real in range(-100, 101):
#    print("row:" + str(real))
#    row = []
#    for imag in range(-100, 101):
#        print("col:" + str(imag))
#        row.append(findClosest(runpass(passes=10, setBstart=complex(real/10, imag/10), setSpeed=.01)[1]))
#    data.append(row)

#data_out = open("eigenvaluedata4.csv", "w")
#for row in data:
#    for item in row[:-1]:
#        data_out.write(str(item[0]))
#        data_out.write(",")
#    data_out.write(str(row[-1][0]))
#    data_out.write("\n")

#data_out.close()

def get_data(a, name_mod = "", passes=20, res=4, speed=.01, size=200): # Produces a file named "eigenvaluedata_%a"
    data_out = open("./Data/eigenvaluedata"+str(size)+"_"+name_mod+str(a)+".csv", "w")
    for real in range(-size, size+1):
        print(real)
        #print("row:" + str(real))
        for imag in range(-size, size+1):
            #print("col:" + str(imag))
            eig = runpass(passes=passes, setBstart=complex(real / res, imag / res), setSpeed=speed)
            data_out.write("[" + str(eig[1].real) + "," + str(eig[1].imag) + "]")
            if imag != size:
                data_out.write(",")
        data_out.write("\n")
    data_out.close()

#for a in range(-4,6): # Usually this is 5 and there is no if check, but my computer restarted so this was to keep already saved progress
#    for b in range(-5,6):
#        if a == -4 and b <= -4:
#            pass
#        else:
#            print("setting a to " + str(complex(a,b)))
#            get_data(complex(a,b))

# Most recent normal computer run
get_data(-1, name_mod="eigvalsH(.5,.5,.625)",res=4, size=200)

# What I want to try on a supercomputer:

# get_data(1, name_mod="super", passes=50, res=20, speed=.001, size=2000)