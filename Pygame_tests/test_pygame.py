import pygame#this module only run if in the python version 3.10.2 not in the 11.0...

pygame.init()

WIDTH = 500
HEIGHT = 500

#THIS IS FOR THE SCREEN
screen =  pygame.display.set_mode((WIDTH,HEIGHT))

run = True


#THIS IS FOR THE INITIALATION OF THE GAME AND THIS ONE
#MUST BE A LOOP 


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #DRAWING

    pygame.draw.rect(screen,(255,0,0),(400,400,50,50))
    pygame.display.update()