# Gathers the data for the visualization program
# Intended to only be needed to run once
# Run before the graphical component.
# Set the name of the output file beforehand. Be careful not to overwrite an existing data file
# This program takes most of a day to run. For lower speeds, more passes, and higher resolution,
# (to get more accurate data), budget time accordingly. I personally leave my computer open and plugged in overnight and
# adjusted my computer sleep settings to keep it running.

from main import findClosest, runpass

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

def get_data(a): # Produces a file named "eigenvaluedata_%a"
    data_out = open("./Data/eigenvaluedata_"+str(a)+".csv", "w")
    for real in range(-100, 101):
        print("row:" + str(real))
        for imag in range(-100, 101):
            #print("col:" + str(imag))
            data_out.write(str(findClosest(runpass(passes=10, setBstart=complex(real / 10, imag / 10), setSpeed=.01)[1])[0]))
            if imag != 100:
                data_out.write(",")
        data_out.write("\n")
    data_out.close()

for a in range(-4,6): # Usually this is 5 and there is no if check, but my computer restarted so this was to keep already saved progress
    for b in range(-5,6):
        if a == -4 and b <= -4:
            pass
        else:
            print("setting a to " + str(complex(a,b)))
            get_data(complex(a,b))