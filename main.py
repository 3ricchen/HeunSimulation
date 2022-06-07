import math
import cmath
import turtle
import numpy as np

radius = .02
time = 0
speed = .00005
deltax = complex(0,0)

d2y = complex(0,0) # y''
dy = complex(0,0) # y'
y = complex(1,0)


x = complex(radius,0)
a = complex(2,0) #
gamma = complex(1/2,0)
delta = complex(1/2,0)
epsilon = complex(1/2,0)
alpha = complex(1/4,0)
beta = complex(1/4,0)
q = complex(0, 0)

def update_d2Y():
    global d2y
    d2y = -(gamma/x+delta/(x-1)+epsilon/(x-a))*dy - ((alpha*beta*x-q)/(x*(x-1)*(x-a)))*y

def update_dY():
    global dy
    dy += deltax*d2y

def update_Y():
    global y
    y += deltax*dy

def update_x(center):
    global x, deltax, time
    time = speed + time
    last_x = x
    x = radius*cmath.exp(time*complex(0, math.pi * 2)) + center
    deltax = x - last_x


def update(center):
    update_x(center)
    update_d2Y()
    update_dY()
    update_Y()




def simulate(center):
    global time, dy, y
    print("started")
    dy = complex(0, 0)  # y'
    y = complex(1, 0)
    time = 0
    while time < 1:
        update(center)
    a = y
    c = dy

    dy = complex(1, 0)  # y'
    y = complex(0, 0)
    time = 0
    while time < 1:
        update(center)
    b = y
    d = dy

    return np.matrix([[a,c],[b,d]])

#Record around 0
x = complex(radius,0) + 0
M0 = simulate(0)
print(M0)
print(M0*M0)
#Record around 1
x = complex(radius,0)+ 1
M1 = simulate(1)
print(M1*M1)
#Record around a
x = complex(radius,0) + a
Ma = simulate(a)
print(Ma*Ma)

M = M1*M0*Ma
print()
print(M)
print(np.trace(M0))
print(np.trace(M1))
print(np.trace(Ma))
print(np.trace(M))
print(np.trace((M)**2))
print(np.linalg.eig(M1*M0))
print(np.linalg.det(M))
#Tx.goto(100*x.real, 100*x.imag)
        #Ty.goto(25*y.real, 25*y.imag)
        #Tdy.goto(25*dy.real, 25*dy.imag)
        #Td2y.goto(5*d2y.real, 5*d2y.imag)
print('Done')

def runpass():
    # Update M0, M1, and Ma (M1, M2, and M3)
    # Compute the trace of M1M2 and M2M3

    pass