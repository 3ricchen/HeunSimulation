import math
import cmath
from turtle import *
import numpy as np
import scipy
import matplotlib.pyplot as plt

radius = .4
time = 0
speed = .00005
deltax = complex(0,0)

d2y = complex(0,0) # y''
dy = complex(0,0) # y'
y = complex(1,0)


x = complex(radius,0)
a = complex(-1,0) #
gamma = complex(1/2,0)
delta = complex(1/2,0)
epsilon = 0.332537823601
alpha = (gamma+delta+epsilon-1)/2
beta = alpha
B = complex(11,8) # q = B/4
center = 0
#turtle = Turtle()
#screen = turtle.getscreen()
#screen.tracer(20)

bees = []

#Common point that all paths go through:
p = complex(1,1)
def update_d2Y():
    global d2y
    d2y = -(gamma/x+delta/(x-1)+epsilon/(x-a))*dy - ((alpha*beta*x-B/4)/(x*(x-1)*(x-a)))*y

def update_dY():
    global dy
    dy += deltax*d2y

def update_Y():
    global y
    y += deltax*dy

def update_x():
    global x, deltax, time, center
    time = speed + time
    last_x = x
    if time < 1:
        x = x + ((center + radius) - p) * speed
    elif time >= 1 and time < 2:
        x = radius * cmath.exp(time * complex(0, math.pi * 2)) + center
    elif time >= 2:
        x = x + (p - (center + radius)) * speed
    deltax = x - last_x
   # turtle.goto(x.real*100, x.imag*100)


def update():
    update_x()
    update_d2Y()
    update_dY()
    update_Y()
def simulate():
    global x, time, d2y, dy, y
    #print("started")
    d2y = 0
    dy = complex(0, 0)  # y'
    y = complex(1, 0)
    time = 0
    x = p
    while time < 3:
        update()
    a = y
    c = dy

    d2y = 0
    dy = complex(1, 0)  # y'
    y = complex(0, 0)
    time = 0
    x = p
    while time < 3:
        update()
    b = y
    d = dy

    return np.matrix([[a,c],[b,d]])

def findMatrices():
    global center, x
    #Record around 0
    x = complex(radius,0) + 0
    center = 0
    M0 = simulate()
    #print(M0)
    #Record around 1
    center = 1
    x = complex(radius,0)+ 1
    M1 = simulate()
    #print(M1)
    #Record around a
    center = a
    x = complex(radius,0) + a
    Ma = simulate()
    #print(Ma)
    return M0, M1, Ma

#M0, M1, Ma = findMatrices()
#M = M0 * M1 * Ma
#print(np.linalg.eigvals(M))
#print(np.trace(M))

#print(np.linalg.eigvals(M0))
#print(np.linalg.eigvals(M1))
#print(np.linalg.eigvals(Ma))

def findTraces(M0, M1, Ma):
    t01 = np.trace(M0 * M1)
    t1a = np.trace(M1 * Ma)
    return t01, t1a



#Tx.goto(100*x.real, 100*x.imag)
        #Ty.goto(25*y.real, 25*y.imag)
        #Tdy.goto(25*dy.real, 25*dy.imag)
        #Td2y.goto(5*d2y.real, 5*d2y.imag)
#print('Done')


def runpass(passes = 50, Bdelta = .0001, setBstart = None, setSpeed = None, seta = None):
    global B, bees, speed, a
    if setBstart != None: # To allow external control of setting the B parameter
        B = setBstart
    if setSpeed != None: # To allow external control of setting the B parameter
        speed = setSpeed
    if seta != None:
        a = seta
    bees.append([B.real, B.imag])
    #print("Matrices")
    B0 = B
    B1 = B + Bdelta
    B = B0
    Mset0 = findMatrices()
    B = B1
    Mset1 = findMatrices()
    #print(str(Mset0[0]) + "\n" + str(Mset0[1]) + "\n" + str(Mset0[2]))
    #print(str(Mset1[0]) + "\n" + str(Mset1[1]) + "\n" + str(Mset1[2]))
    Tset0 = findTraces(Mset0[0],Mset0[1],Mset0[2]) # [t12(B0), t23(B0)]
    Tset1 = findTraces(Mset1[0], Mset1[1], Mset1[2]) # [t12(B1), t23(B1)]
    #print("Traces")
    #print(Tset1[1])
    #print(Tset0[1])
    dt12 = (Tset1[0] - Tset0[0])/(Bdelta)
    dt23 = (Tset1[1] - Tset0[1])/(Bdelta)
    lambdas = list(map(getLambda,Mset0))
    b_x = (dt23.conjugate()*((Tset0[0]/(lambdas[0]*lambdas[1])).imag)/(lambdas[1]*lambdas[2]) - dt12.conjugate()*((Tset0[1]/(lambdas[1]*lambdas[2])).imag)/(lambdas[0]*lambdas[1]))/((dt12.conjugate()*dt23/(lambdas[0].conjugate()*lambdas[1]*lambdas[1].conjugate()*lambdas[2])).imag)
    #print(dt12)
    #print(dt23)
    #print("X:")
    #print(b_x)
    B = B0 + b_x*.3
    #print(B)
    passes -= 1
    if passes == 0:
        return Mset0,B
    else:
        return runpass(passes = passes)

def makeEigenvalue(m, n):
    return 1.43554 * (complex(m,n) ** 2) + 0.114237 * complex(m,n) / complex(m,-n)

def findClosest(b):
    closest = [None, None]
    dist = float("inf")
    for n in range(-10,11):
        for m in range(-10, 11):
            if (m,n) != (0,0) and abs(makeEigenvalue(m,n) - b) < dist:
                closest = [m, n]
                dist = abs(makeEigenvalue(m,n)-b)
    return closest, dist

def getLambda(mat):
    det = np.linalg.det(mat)
    return cmath.sqrt(det)


#results = runpass()[0]
#print(results[0])
#print(results[1])
#print(results[2])
#print(B)
#print(findClosest(B))

#plt.plot(bees)
#plt.show()

#B^T\circxA * vec(X) = Vec (C)
#A = A*
#B = A
#C = X

#(A^T\circxA*)-I * vec(X) = 0
def complexToReal(mat):
    return np.array(
        [[mat[0:0].real, -mat[0:0].imag, mat[0:1].real, -mat[0:1].imag],
         [mat[0:0].imag, mat[0:0].real, mat[0:1].imag, mat[0:1].real],
         [mat[1:0].real, -mat[1:0].imag, mat[1:1].real, -mat[1:1].imag],
         [mat[1:0].imag, mat[1:0].real, mat[1:1].imag, -mat[1:1].real]])

def isHermit(mat, zero = 10**-10): # Does the matrix live in a small shack in the wilderness?
    return np.linalg.norm(mat - mat.transpose()) < zero

def constructErrorMat(basis):
    mat = []
    for m in basis:
        mat.append(np.reshape(m-m.transpose().conjugate(),(1,4)))

def solve(P,Q,R):
    x_basis = scipy.null_space(np.concatenate([np.kron(P.transpose(), P.transpose().conjugate())-np.identity(2),
                                               np.kron(Q.transpose(), Q.transpose().conjugate())-np.identity(2),
                                               np.kron(R.transpose(), R.transpose().conjugate())-np.identity(2)], axis=0), np.array([0]*12))
    out_basis = []
    for x in x_basis:
        if isHermit(complexToReal(np.reshape(x,2,2))):
            out_basis.append(x)
