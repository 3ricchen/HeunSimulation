import multiprocessing as mp
from main import runpass
import numpy as np
import os

#Runs the runpass function, with a starting guess value of st.
def funct(st):
    Mset, B = runpass(passes = 20, setBstart = st, setSpeed = .01, setEpsilon = 0.125, setDelta = 0.50)
    # Mset, B = runpass(passes=passes, setBstart=complex(real / res, imag / res), setSpeed=speed, setEpsilon = 0.125, setDelta=0.50)
    
    f = open('Output/' + str(st.real) + '_' + str(st.imag) + '.txt','w')
    
    f.write("[" + str(B.real) + "," + str(B.imag) + "]")
    
    print('JUST FINISHED' + str(st.real) + '_' + str(st.imag))
    f.close()

# funct(complex(0,0))

size = 5
res = 4
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



#runParallel(-1, 'eigvalsH(.5,.5,.375)', 10, 4, setEpsilon = 0.375, setDelta = 0.5)

convert('eigvalsH(.5,.5,.375)',-1,10,4)


#get_data(-1, name_mod="TESTING",res=4, size=4)