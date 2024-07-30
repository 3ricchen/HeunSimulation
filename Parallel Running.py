import multiprocessing as mp
from main import runpass
import numpy as np
import os
import time

### MAKE SURE TO CHANGE THE PARAMETER VALUES HERE!!! ###
#Runs the runpass function, with a starting guess value of st.
def funct(st):
    # Have this on in case we're going to be repeating computations.
    if os.path.isfile('Output/' + str(st.real) + '_' + str(st.imag) + '.txt'):
        return
    Mset, B = runpass(passes = 20, setBstart = st, setSpeed = .001, setEpsilon = 0.875, setDelta = 0.50)
    # Mset, B = runpass(passes=passes, setBstart=complex(real / res, imag / res), setSpeed=speed, setEpsilon = 0.125, setDelta=0.50)
    
    with open('Output/' + str(st.real) + '_' + str(st.imag) + '.txt','w') as f:
    # with open('Output/hello.txt','w') as f:
        f.write("[" + str(B.real) + "," + str(B.imag) + "]")
        # f.write("Hello")
        print('JUST FINISHED ' + str(st.real) + '_' + str(st.imag))

# funct(complex(0,0))


def runParallel(a, name_mod, size, res, num_cores = None, passes = 20, setEpsilon = 0.5, setDelta = 0.5):
    points = []
    for real in range(-size,size+1):
        for imag in range(-size,size+1):
            points.append(complex(real/res, imag/res))
    processes = []
    if __name__ == '__main__':
        if num_cores == None:
            cores = mp.cpu_count()
        else:
            cores = num_cores
        # for i in range(len(points)):
        #     print(str(i) + '/' + str(len(points)))
        #     p = mp.Process(target = funct,args = [points[i]])
        #     p.start()
        # for process in processes:
        #     process.join()
        with mp.Pool(cores) as p:
            p.map(funct,points)
    
    

    #Converts the txt files to a usable CSV file for EigenValueVisualization.
    
count = 0

def convert(name_mod,a,size,res):
    data_out = open("./Data/eigenvaluedata"+str(size)+"_"+name_mod+str(a)+".csv", "w") # Opens the output file to write to
    for real in range(-size,size+1):
        for imag in range(-size,size+1):
            print('Looking for: ' + 'Output/' + str(real/res) + '_' + str(imag/res) + '.txt')
            with open('Output/' + str(real/res) + '_' + str(imag/res) + '.txt', 'r') as f:
                l = f.readline()
                print(l)
                data_out.write(l)
            f.close()
            if imag != size:
                data_out.write(",")
        data_out.write("\n")
    data_out.close()
    for real in range(-size,size+1):
        for imag in range(-size,size+1):
            os.remove('Output/' + str(real/res) + '_' + str(imag/res) + '.txt')



######################################
# SET SIZE AND RESOLUTION PARAMETERS #
######################################
size = 100
res = 4

runParallel(-1, 'eigvalsH(.5,.5,.875)', size, res, setEpsilon = 0.625, setDelta = 0.5)

# convert('FIXEDFINAL_eigvalsH(.5,.5,.875)',-1, size, res)


#get_data(-1, name_mod="TESTING",res=4, size=4)