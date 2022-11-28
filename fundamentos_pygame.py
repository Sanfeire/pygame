import pygame
from sys import exit


pygame.init()

#especificaciones de la pantalla en general
screen = pygame.display.set_mode((800,400))
screen.fill('black')


pygame.display.set_caption('JUEGO DEMO') # definición del título de la ventana
clock = pygame.time.Clock() # creamos un reloj para el control de los frame rates

#declaramos una nueva superficie desde una imagen
fondo = pygame.image.load('fondo.png') 
suelo = pygame.image.load('suelo.png') 
objeto = pygame.image.load('pirola.png')


objeto_x = 750

while True:
    for event in pygame.event.get(): # si ocurre un evento de pygame
        if event.type == pygame.QUIT: # y el evento de pygame es que se cierre la ventana
            pygame.quit() # se sale del juego
            exit()

    screen.blit(fondo,(0,0)) # especificamos la posición del suelo en x=0 e y=330
    screen.blit(suelo,(0,0))

    objeto_x -= 3  # velocidad con la que se mueve el objeto

    if objeto_x == -150:
        objeto_x = 750

    screen.blit(objeto,(objeto_x,160))


    pygame.display.update()
    clock.tick(60) # indica que el bucle while sólo se puede ejecutar a 60 frames por segundo