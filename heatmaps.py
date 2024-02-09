import math
import cmath
#from turtle import *
import numpy as np
import scipy
import matplotlib.pyplot as plt
import multiprocessing as mp
from main import getEnergyGradient, getNewEnergy
import os

gamma = 0.5
delta = 0.5
epsilon = 0.5

points = []
size = 50
res = 4
for real in range(-size,size+1):
    for imag in range(-size,size+1):
        points.append(complex(real/res, imag/res))

def mapfunct(st): #GETS THE GRADIENT
    if not os.path.isfile('Output/' + str(st.real) + '_' + str(st.imag) + '.txt'):
        energy = getEnergyGradient(st, setEpsilon = epsilon, setDelta = delta, setGamma = gamma)
        f = open('Output/' + str(st.real) + '_' + str(st.imag) + '.txt','w')
        f.write("[" + str(energy) + "]")
        print('JUST FINISHED' + str(st.real) + '_' + str(st.imag))
        f.close()

def energfunct(st): #GETS THE ENERGY
    if not os.path.isfile('Output/' + str(st.real) + '_' + str(st.imag) + '.txt'):
        t1, t2, t3 = getNewEnergy(st, setEpsilon = epsilon, setDelta = delta, setGamma = gamma)
        f = open('Output/' + str(st.real) + '_' + str(st.imag) + '.txt','w')
        f.write("[" + str(t1) + ', ' + str(t2) + ', ' + str(t3) + "]")
        print('JUST FINISHED' + str(st.real) + '_' + str(st.imag))
        f.close()

def getGradientMap(size, res, num_cores = None, setGamma = 0.5, setEpsilon = 0.5, setDelta = 0.5):
    global gamma, delta, epsilon
    points = []
    if setGamma != None:
        gamma = setGamma
    if setEpsilon != None:
        epsilon = setEpsilon
    if setDelta != None:
        delta = setDelta
    
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
            p.map(mapfunct,points)

def getEnergyMap(size, res, num_cores = None, setGamma = 0.5, setEpsilon = 0.5, setDelta = 0.5):
    global gamma,delta,epsilon
    points = []
    if setGamma != None:
        gamma = setGamma
    if setEpsilon != None:
        epsilon = setEpsilon
    if setDelta != None:
        delta = setDelta
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
            p.map(energfunct,points)
def convert(size, res, name_mod):
    data_out = open("./Data/ENERGYDATA"+str(size)+"_"+name_mod+".csv", "w") # Opens the output file to write to
    for imag in reversed(range(-size,size+1)):
        for real in range(0,size+1):
            print('Looking for: ' + 'Output/' + str(real/res) + '_' + str(imag/res) + '.txt')
            with open('Output/' + str(real/res) + '_' + str(imag/res) + '.txt', 'r') as f:
                l = f.readline()
                print(l)
                data_out.write(l)
            f.close()
            if real != size:
                data_out.write(",")
        data_out.write("\n")
    data_out.close()
    for imag in reversed(range(-size,size+1)):
        for real in range(-size,size+1):
            os.remove('Output/' + str(real/res) + '_' + str(imag/res) + '.txt')

getEnergyMap(250,10)
#convert(100,4,'FULLENERGY(.5,.5,.5)VALUES')