import math
import cmath
from turtle import *
import numpy as np

radius = .02
time = 0
speed = .0005
deltax = complex(0,0)

d2y = complex(0,0) # y''
dy = complex(0,0) # y'
y = complex(1,0)


x = complex(radius,0)
a = complex(3,0) #
gamma = complex(1/2,0)
delta = complex(1/2,0)
epsilon = complex(1/2,0)
alpha = complex(1/4,0)
beta = complex(1/4,0)
q = complex(0, 0)
center = 0

#turtle = Turtle()

#Common point that all paths go through:
p = complex(1,1)
def update_d2Y():
    global d2y
    d2y = -(gamma/x+delta/(x-1)+epsilon/(x-a))*dy - ((alpha*beta*x-q)/(x*(x-1)*(x-a)))*y

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
        x += ((center + radius) - p) * speed
    elif time >= 1 and time < 2:
        x = radius * cmath.exp(time * complex(0, math.pi * 2)) + center
    elif time >= 2:
        x += (p - (center + radius)) * speed
    deltax = x - last_x
    #turtle.goto(x.real*100, x.imag*100)


def update():
    update_x()
    update_d2Y()
    update_dY()
    update_Y()
def simulate():
    global x, time, d2y, dy, y
    print("started")
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

#Record around 0
x = complex(radius,0) + 0
center = 0
M0 = simulate()
print(M0)
#Record around 1
center = 1
x = complex(radius,0)+ 1
M1 = simulate()
print(M1)
#Record around a
center = a
x = complex(radius,0) + a
Ma = simulate()
print(Ma)


M = M0 * M1 * Ma
print(np.linalg.eigvals(M))
print(np.trace(M))

print(np.linalg.eigvals(M0))
print(np.linalg.eigvals(M1))
print(np.linalg.eigvals(Ma))


#Tx.goto(100*x.real, 100*x.imag)
        #Ty.goto(25*y.real, 25*y.imag)
        #Tdy.goto(25*dy.real, 25*dy.imag)
        #Td2y.goto(5*d2y.real, 5*d2y.imag)
print('Done')

def runpass():
    # Update M0, M1, and Ma (M1, M2, and M3)
    # Compute the trace of M1M2 and M2M3

    pass