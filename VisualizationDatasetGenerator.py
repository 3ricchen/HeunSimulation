# Gathers the data for the visualization program
# Intended to only be needed to run once
# Run before the graphical component.
# Set the name of the output file beforehand. Be careful not to overwrite an existing data file
# This program takes most of a day to run. For lower speeds, more passes, and higher resolution,
# (to get more accurate data), budget time accordingly. I personally leave my computer open and plugged in overnight and
# adjusted my computer sleep settings to keep it running.

from main import findClosest, runpass

# Gathering data: Stored in a 201x201 array

data = []
for real in range(-50, 51):
    print("row:" + str(real))
    row = []
    for imag in range(-50, 51):
        print("col:" + str(imag))
        row.append(findClosest(runpass(passes=30, setBstart=complex(real/5, imag/5), setSpeed=.001)[1]))
    data.append(row)

data_out = open("eigenvaluedata3.csv", "w")
for row in data:
    for item in row[:-1]:
        data_out.write(str(item[0]))
        data_out.write(",")
    data_out.write(str(row[-1][0]))
    data_out.write("\n")

data_out.close()
