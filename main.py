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
a = complex(15,0) #
gamma = complex(1/2,0)
delta = complex(1/2,0)
epsilon = complex(1/2,0)
alpha = complex(1/4,0)
beta = complex(1/4,0)
q = complex(0, 0)
center = 0


velocity = 0
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

def update_x_circ():
    global x, deltax, time, center
    time = speed + time
    last_x = x
    if time <= 1:
        x = radius*cmath.exp(time*complex(0, math.pi * 2)) + center
    deltax = x - last_x
    turtle.goto(x.real, x.imag)

def update_x_line():
    global x, deltax, time, center, velocity
    time = speed + time
    last_x = x
    x = x + velocity
    deltax = x - last_x
    turtle.goto(x.real, x.imag)
def update():
    if time<1:
        update_x_circ()
    if time>=1 and time < 1.5:
        velocity = (p - (center + radius))/0.5
        update_x_line()
    if time >= 1.5:
        velocity = -(p-(center + radius))/0.5
        update_x_line()
    update_d2Y()
    update_dY()
    update_Y()
def simulate():
    global time, d2y, dy, y
    print("started")
    d2y = 0
    dy = complex(0, 0)  # y'
    y = complex(1, 0)
    time = 0
    while time < 2:
        update()
    a = y
    c = dy

    d2y = 0
    dy = complex(1, 0)  # y'
    y = complex(0, 0)
    time = 0
    while time < 2:
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

#Tx.goto(100*x.real, 100*x.imag)
        #Ty.goto(25*y.real, 25*y.imag)
        #Tdy.goto(25*dy.real, 25*dy.imag)
        #Td2y.goto(5*d2y.real, 5*d2y.imag)
print('Done')

def runpass():
    # Update M0, M1, and Ma (M1, M2, and M3)
    # Compute the trace of M1M2 and M2M3

    pass