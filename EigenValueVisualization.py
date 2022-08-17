# Creates a visualization of the areas of convergence to the different eigenvalues
# This program requires pygame, a graphics module for python. Install using pip install pygame

import pygame, main, math, cmath

pygame.init()



def vis(a):
    data = []
    eigencounts = [[0 for i in range(21)] for j in range(21)]
    data_in = open("./Data/eigenvaluedata_" + str(a) + ".csv", "r").read()
    data_lines = data_in.splitlines()
    for line in data_lines: # Reads in all of the eigenvalue data from the file (this is kinda a botched csv since there are
        # lists as elements requiring bracket layers to parse
        in_braket = False
        index = 0
        out = []
        piece = ""
        while index < len(line):
            if not in_braket:
                if line[index] == "[":
                    in_braket = True
                    piece = ""
            else:
                if line[index] == "]":
                    in_braket = False
                    out.append(piece.split(","))
                else:
                    piece += line[index]
            index += 1
        data.append(out)
    width = 0
    while width < 810: # Sets the pixel width to make the screen just larger than 600 pixels
        width += len(data)
    screen = pygame.display.set_mode((width, width))
    screen.fill((0, 0, 0))

    for i in range(-(len(data) - 1) // 2, (len(data) + 1) // 2):
        for j in range(-(len(data[i]) - 1) // 2, (len(data[i]) + 1) // 2):
            # print(str([((len(data)-1)//2 + i)*606//len(data), ((len(data[i])-1)//2 - j)*606//len(data[i]), 606//len(data[i]), 606//len(data[i])]))
            print(data[i][j])
            if data[i][j][0] == "None" or data[i][j][1] == "None": # Fills with blue to handle an error from the eigenvalue
                # data being missing (only happens once)
                pygame.draw.rect(screen, (0, 0, 255),
                                 [((len(data) - 1) // 2 + i) * width // len(data),
                                  ((len(data[i]) - 1) // 2 - j) * width // len(data[i]), width // len(data[i]),
                                  width // len(data[i])])
            else: # Otherwise colors with red and green based on the m/n values eigenvalues.
                eigencounts[int(data[i][j][0])+10][int(data[i][j][1])+10] += 1
                pygame.draw.rect(screen, (int(int(data[i][j][0]) * 12.7) + 128, int(int(data[i][j][1]) * 12.7) + 128, 0),
                                 [((len(data) - 1) // 2 + i) * width // len(data),
                                  ((len(data[i]) - 1) // 2 - j) * width // len(data[i]), width // len(data[i]),
                                  width // len(data[i])])
    for m in range(-10, 11):
        for n in range(-10, 11):
            if m == n == 0:
                pass
            elif eigencounts[m+10][n+10] > 30:
                pygame.draw.rect(screen, (0,0,0), [int((10*main.makeEigenvalue(m,n).real + (len(data)-1)//2)*width//len(data)), int((10*main.makeEigenvalue(m,n).imag + (len(data[0])-1)//2)*width//len(data[0])), 3*width//len(data), 3*width//len(data[0])])

    pygame.display.update() # Shows the image for us

    pygame.image.save(screen, "./Visualizations/Visualization_"+str(a)+".png") # Also saves it to the folder. Change this filename to prevent overwriting.
flag = True

# vis will generate the image for a
# Adjust this loop for the different target a values
#for a in range(-5,6):
#    vis(a)

def eigvis(filename, res=10, half=100):
    data = []
    data_in = open("./" + filename + ".csv", "r").read()
    data_lines = data_in.splitlines()
    for line in data_lines:  # Reads in all of the eigenvalue data from the file (this is kinda a botched csv since there are
        # lists as elements requiring bracket layers to parse
        in_braket = False
        index = 0
        out = []
        piece = ""
        while index < len(line):
            if not in_braket:
                if line[index] == "[":
                    in_braket = True
                    piece = ""
            else:
                if line[index] == "]":
                    in_braket = False
                    out.append(piece.split(","))
                else:
                    piece += line[index]
            index += 1
        data.append(out)
    width = 0
    while width < 810:  # Sets the pixel width to make the screen just larger than 600 pixels
        width += len(data)
    screen = pygame.display.set_mode((width, width))
    screen.fill((255, 255, 255))
    x = 0
    for line in data:
        y = 0
        for cord in line:
            try:
                real_pix = x*width//len(data)
                real_eig = (float(cord[0])*res+half)*width//len(data)
                imag_eig = (-float(cord[1]) * res + half) * width // len(data)
                imag_pix = (len(data)-1-y)*width//len(data)
                mag = math.sqrt(float(cord[0])**2 + float(cord[1])**2)
                normd = [float(cord[0])/mag, 0, float(cord[1])/mag]
                weight = 2*math.atan(mag/10)/math.pi
                #pygame.draw.rect(screen, (int(normd[0]*weight*127 + 127),weight*64,int(normd[2]*weight*127 + 127)), [real_pix, imag_pix, width//len(data), width//len(data)])
                color = pygame.Color(0)
                shift = lambda x: x + 360*(x<0)
                color.hsva = (shift(int(cmath.polar(complex(float(cord[0]),float(cord[1])))[1]*180/math.pi)),70,int(weight*100),100)
                #print(color.hsva)
                pygame.draw.rect(screen, color, [real_pix, imag_pix, width//len(data), width//len(data)])
                #pygame.draw.rect(screen, (255,255,255), [real_eig, imag_eig,width//len(data), width//len(data)])
            except:
                pygame.draw.rect(screen, (0,0,0), [real_pix, imag_pix, width//len(data), width//len(data)])
                print(cord)
            y += 1
        x += 1
    x = 0
    for line in data:
        y = 0
        for cord in line:
            try:
                real_eig = (float(cord[0]) * res + 100) * width // len(data)
                imag_eig = (-float(cord[1]) * res + 100) * width // len(data)
                #pygame.draw.rect(screen, (255, 255, 255),
                 #                   [real_eig, imag_eig, width // len(data), width // len(data)])
            except:
                pass
            y += 1
        x += 1
    for m in range(-7,8):
        for n in range(-7,8):
            if m != 0 or n != 0:
                pass
                #pygame.draw.circle(screen, (255,255,0), [main.makeEigenvalue(m,n).real*res*width//len(data) + width//2,-main.makeEigenvalue(m,n).imag*res*width//len(data) + width//2], (width//len(data))*7, width=width//(2*len(data)))
    pygame.display.update()
    pygame.image.save(screen, "./" + filename + "hsva.png")

eigvis("Data/eigenvaluedata10_eigvalsH(.5,.5,.332~ish)-1", half=200, res=4)
while flag:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            flag = False
pygame.quit()
