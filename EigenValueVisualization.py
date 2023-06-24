# Creates a visualization of the areas of convergence to the different eigenvalues
# This program requires pygame, a graphics module for python. Install using pip install pygame

import pygame, main, math, cmath

pygame.init()
flag = True

def sqrt(real, imag):
    cval = cmath.sqrt(complex(real, imag))
    return cval.real, cval.imag

def eigvis(filename, res=10, half=100, axis=True):
    '''
    eigvis
    =====================
    Used on a dataset given by VisualizationDatasetGenerator.py to create and display a variety of possible figures.

    Parameters:
    -----------
    filename: the name of the data file (relative path, no ending '.csv')
    res: The resolution of the image/data file
    half: Half the width of the data file
    axis: Do we draw axies

    Outputs:
    --------
    Draws an image on the screen and saves it to filename + hsvaE.png
    '''
    data = []
    data_in = open("./" + filename + ".csv", "r").read()
    data_lines = data_in.splitlines()
    for line in data_lines:  # Reads in all of the eigenvalue data from the file (this is kinda a botched csv since there are
        # lists as elements requiring bracket layers to parse)
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
                sqt = sqrt(float(cord[0]), float(cord[1]))
                print("sqt")
                sqtpix = sqrt(x-len(data)//2,len(data)//2-y)
                #real_pix = x*width//len(data)
                #real_eig = (float(cord[0])*res+half)*width//len(data)
                #imag_eig = (-float(cord[1]) * res + half) * width // len(data)
                #imag_pix = (len(data)-1-y)*width//len(data)
                #mag = math.sqrt(float(cord[0])**2 + float(cord[1])**2)
                # Square Root Image Transform
                real_pix = sqtpix[0] * width // (2*math.sqrt(len(data))) + width//2
                imag_pix = (int(math.sqrt(len(data))) - 1 - sqtpix[1]) * width // (2*math.sqrt(len(data)))
                mreal_pix = -sqtpix[0] * width // (2*math.sqrt(len(data))) + width//2
                mimag_pix = (int(math.sqrt(len(data))) - 1 + sqtpix[1]) * width // (2*math.sqrt(len(data)))
                #real_eig = (sqt[0] * res + half) * width // len(data)
                #imag_eig = (-sqt[1] * res + half) * width // len(data)
                mag = math.sqrt(sqt[0] ** 2 + sqt[1] ** 2)
                normd = [float(cord[0])/mag, 0, float(cord[1])/mag]
                weight = 2*math.atan(mag/10)/math.pi
                # Uncomment this for a red/blue coloring
                #pygame.draw.rect(screen, (int(normd[0]*weight*127 + 127),weight*64,int(normd[2]*weight*127 + 127)), [real_pix, imag_pix, width//len(data), width//len(data)])
                color = pygame.Color(0)
                shift = lambda x: x + 360*(x<0)
                print("draw")
                color.hsla = (shift(int(cmath.polar(complex(float(cord[0]),float(cord[1])))[1]*180/math.pi)),70,int(weight*100),100)
                # Uncomment this for a HSV coloring
                # pygame.draw.rect(screen, color, [real_pix, imag_pix, width//len(data), width//len(data)])
                # pygame.draw.rect(screen, color, [mreal_pix, mimag_pix, width // len(data), width // len(data)])
                # Uncomment this to display the convergent values in white
                #pygame.draw.rect(screen, (255,255,255), [real_eig, imag_eig,width//len(data), width//len(data)])
                print("done")
            except: # Handles drawing invalid or corrupt data.
                # Uncomment this when producing either an HSV or red/blue image
                #pygame.draw.rect(screen, (0,0,0), [real_pix, imag_pix, width//len(data), width//len(data)])
                print("fail")
                pass
            y += 1
        x += 1
    # Uncomment this to compile the squareroots of the eigenvalues into a separate file.
    # cvals = open("eigrootlist" + filename[24:-2] + ".csv","w")
    x = 0
    for line in data:
        y = 0
        for cord in line:
            try:
                val = cmath.sqrt(complex(float(cord[0]), float(cord[1])))
                real_eig = (float(cord[0]) * res + half) * width // len(data)
                imag_eig = (-float(cord[1]) * res + half) * width // len(data)
                real_pix = x * width // len(data)
                imag_pix = (len(data) - 1 - y) * width // len(data)
                if abs(real_eig - real_pix) < width//(len(data)*.5) and abs(imag_eig - imag_pix) < width//(len(data)*.5):
                    # Uncomment this to draw grey circles at each of the eigenvalue positions
                    #pygame.draw.circle(screen, (31, 31, 31), [real_eig, imag_eig], 1*width // len(data))
                    # Uncomment this if compiling squareroots
                    # cvals.write(str(val.real) + "," + str(val.imag) + "\n")
                    # Uncomment this to draw the squareroots of the eigenvalues
                    pygame.draw.rect(screen, (0, 0, 0),
                                        [(5*float(val.real) * res + half) * width // len(data), (5*-float(val.imag) * res + half) * width // len(data), 1.5*width // len(data), 1.5*width // len(data)])
                    pass
            except:
                pass
            y += 1
        x += 1
    for m in range(-7,8):
        for n in range(-7,8):
            if m != 0 or n != 0:
                pass
                # Uncomment to draw Beauker's asymptotic approximations
                guess = main.makeEigenvalue(m,n)
                # For square predictions
                sqrt_pos = sqrt(guess.real, guess.imag)
                #pygame.draw.circle(screen, (235,30,20), [5*sqrt_pos[0]*res*width//len(data) + width//2,-5*sqrt_pos[1]*res*width//len(data) + width//2], (width//len(data))*3, width=width//(2*len(data)))
                # For normal predictions
                # pygame.draw.circle(screen, (235,30,20), [main.makeEigenvalue(m,n).real*res*width//len(data) + width//2,-main.makeEigenvalue(m,n).imag*res*width//len(data) + width//2], (width//len(data))*7, width=width//(2*len(data)))
    if axis:
        scaling = 5 # Set to 5 if only drawing the square roots of convergence values
        pygame.draw.line(screen,(0,0,255), start_pos=[width//2+width//len(data)//2,0], end_pos=[width//2+width//len(data)//2,width-1])
        pygame.draw.line(screen, (0, 0, 255), start_pos=[0,width // 2+width//len(data)//2], end_pos=[width - 1,width // 2+width//len(data)//2])
        font18 = pygame.font.Font(pygame.font.get_default_font(),30)
        screen.blit(font18.render(str(half/2/res/scaling)+"i",False,(0,0,255),None),[width//2+4,width//4-15])
        screen.blit(font18.render(str(-half /2/res/scaling), False, (0, 0, 255), None),
                    [width // 4 -20, width // 2 - 30])
        screen.blit(font18.render(str(-half /2/res/scaling)+"i", False, (0, 0, 255), None),
                    [width // 2 + 4, 3*width // 4 -15])
        screen.blit(font18.render(str(half /2/res/scaling), False, (0, 0, 255), None),
                    [3*width // 4 - 15, width // 2 - 30])
    pygame.display.update()

    pygame.image.save(screen, "./" + filename + "hslaE.png") # Change to edit the output filename

eigvis("Data/eigenvaluedata200_eigvalsH.5.5.625-1", half=200, res=4) # Produces the image for the Lame Equation
while flag:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            flag = False
pygame.quit()
