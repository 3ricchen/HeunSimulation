# Creates a visualization of the areas of convergence to the different eigenvalues
# This program requires pygame, a graphics module for python. Install using pip install pygame

import pygame

pygame.init()


data = []
data_in = open("eigenvaluedata2.csv", "r").read()
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
while width < 600: # Sets the pixel width to make the screen just larger than 600 pixels
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
            pygame.draw.rect(screen, (int(int(data[i][j][0]) * 12.7) + 128, int(int(data[i][j][1]) * 12.7) + 128, 0),
                             [((len(data) - 1) // 2 + i) * width // len(data),
                              ((len(data[i]) - 1) // 2 - j) * width // len(data[i]), width // len(data[i]),
                              width // len(data[i])])
pygame.display.update() # Shows the image for us
flag = True
pygame.image.save(screen, "Visualization2.png") # Also saves it to the folder. Change this filename to prevent overwriting.
while flag:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            flag = False
pygame.quit()
