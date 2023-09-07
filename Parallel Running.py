import multiprocessing as mp
from main import runpass, newrunpass, testQuadTraces, testrunpass
import numpy as np
import os
import time

#Runs the runpass function, with a starting guess value of st.
def funct(st):
    # Mset, B = runpass(passes=passes, setBstart=complex(real / res, imag / res), setSpeed=speed, setEpsilon = 0.125, setDelta=0.50)
    if not os.path.isfile('Output/' + str(st.real) + '_' + str(st.imag) + '.txt'):
        Mset, B = runpass(passes = 20, setBstart = st, setSpeed = .001, setGamma = 0.5, setEpsilon = 0.5, setDelta = 0.5)
        f = open('Output/' + str(st.real) + '_' + str(st.imag) + '.txt','w')
        f.write("[" + str(B.real) + "," + str(B.imag) + "]")
        print('JUST FINISHED' + str(st.real) + '_' + str(st.imag))
        f.close()
    

# funct(complex(0,0))

def newfunct(st):
    if not os.path.isfile('Output/' + str(st.real) + '_' + str(st.imag) + '.txt'):
        Mset, B = newrunpass(passes = -1, setBstart = st, setSpeed = .001, setGamma = 0.5, setEpsilon = 0.5, setDelta = 0.5)
        f = open('Output/' + str(st.real) + '_' + str(st.imag) + '.txt','w')
        f.write("[" + str(B.real) + "," + str(B.imag) + "]")
        print('JUST FINISHED' + str(st.real) + '_' + str(st.imag))
        f.close()
    

def testfunct(st):
    quadtest = testrunpass(setBstart = st, setSpeed = 0.001, setEpsilon = 0.125, setDelta = 0.5)
    g = open('Output/' + str(st.real) + '_' + str(st.imag) + 'TESTQUAD.txt','w')
    g.write(str(quadtest))
    print('JUST FINISHED' + str(st.real) + '_' + str(st.imag) )
    g.close()

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

def newRunParallel(a, name_mod, size, res, num_cores = None, passes = 20, setEpsilon = 0.5, setDelta = 0.5):
    points = []
    for real in range(-size,size+1):
        for imag in range(-size,size+1):
            points.append(complex(real/res, imag/res))
            #points.append((complex(real/res, imag/res)*1.2)**2)
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
            p.map(newfunct,points)
    
    

    #Converts the txt files to a usable CSV file for EigenValueVisualization.
count = 0

def testParallel(a, name_mod, size, res, num_cores = None):
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
        with mp.Pool(cores) as p:
            p.map(testfunct,points)


#This function compiles all of the generated text files from the parallel function into 
def convert(name_mod,a,size,res):
    data_out = open("./Data/eigenvaluedata"+str(size)+"_"+name_mod+str(a)+".csv", "w") # Opens the output file to write to
    for imag in reversed(range(-size,size+1)):
        for real in range(-size,size+1):
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

def convertTrue(name_mod, a, size, res):
    data_out = open("./Data/eigenvaluedata"+str(size)+"_"+name_mod+str(a)+"TESTQUAD.csv", "w") # Opens the output file to write to
    for imag in reversed(range(-size,size+1)):
        for real in range(-size,size+1):
            print('Looking for: ' + 'Output/' + str(real/res) + '_' + str(imag/res) + '.txt')
            with open('Output/' + str(real/res) + '_' + str(imag/res) + 'TESTQUAD.txt', 'r') as f:
                l = f.readline()
                if l == 'True':
                    #This is a yellow-ish  color
                    l = '[500,500]'
                else:
                    #This is a blue-ish color
                    l = '[-500,-500]'
                data_out.write(l)
            f.close()
            if real != size:
                data_out.write(",")
        data_out.write("\n")
    data_out.close()
    for real in range(-size,size+1):
        for imag in range(-size,size+1):
            os.remove('Output/' + str(real/res) + '_' + str(imag/res) + 'TESTQUAD.txt')
    print("Data/eigenvaluedata"+str(size)+"_"+name_mod+str(a)+"TESTQUAD.csv")


######################################
# SET SIZE AND RESOLUTION PARAMETERS #
######################################
size = 12
res = 1
name = 'eigsLatticeNewAlg(.5,.5,.5)'

#newRunParallel(-1, name, size, res, setEpsilon = 0.5, setDelta = 0.5)

# while count < (2*size+1)**2:
#     count=0
#     l = os.listdir('Output')
#     for thing in l:
#         if os.path.isfile(thing):
#             count = count+1
#     time.sleep(60)

#testParallel(-1, name, size, res)
convert(name,-1, size, res)
#convertTrue(name, -1, size, res)

#get_data(-1, name_mod="TESTING",res=4, size=4)