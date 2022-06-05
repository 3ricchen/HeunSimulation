import math
import cmath
import turtle

radius = .2
time = 0
speed = .0001
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
q = complex(2, 0)

def update_d2Y():
    global d2y
    d2y = -(gamma/x+delta/(x-1)+epsilon/(x-a))*dy - (alpha*beta*x-q)/((x*(x-1)*(x-a)))*y

def update_dY():
    global dy
    dy += deltax*d2y

def update_Y():
    global y
    y += deltax*dy

def update_x():
    global x, deltax, time
    time += speed
    last_x = x
    x = radius*cmath.exp(time*complex(0, math.pi * 2))
    deltax = x - last_x


def update():
    update_x()
    update_d2Y()
    update_dY()
    update_Y()


Ty = turtle.Turtle()
screen = Ty.getscreen()
screen.tracer(n = 2000)
Ty.penup()
Ty.goto(100*y.real, 100*y.imag)
Ty.pendown()


Tdy = turtle.Turtle()
Tdy.pencolor("red")
Tdy.penup()
Tdy.goto(100*dy.real, 100*dy.imag)
Tdy.pendown()


Td2y = turtle.Turtle()
Td2y.pencolor("green")
Td2y.penup()
Td2y.goto(5*d2y.real, 5*d2y.imag)
Td2y.pendown()


Tx = turtle.Turtle()
Tx.pencolor("blue")
Tx.penup()
Tx.goto(100*x.real, 100*x.imag)
Tx.pendown()


Tx.speed(1000)
Ty.speed(1000)
Tdy.speed(1000)
Td2y.speed(1000)

print('Norm:')
print((y)*(y.conjugate()) + (dy) * (dy.conjugate()))


while time < 1:
    Tx.goto(100*x.real, 100*x.imag)
    Ty.goto(25*y.real, 25*y.imag)
    Tdy.goto(25*dy.real, 25*dy.imag)
    Td2y.goto(5*d2y.real, 5*d2y.imag)
    update()
print("X")
print(x)
print('Norm:')
print((y)*(y.conjugate()) + (dy) * (dy.conjugate()))
print('Y Value:')
print(y)
print('dY Value:')
print(dy)
input()