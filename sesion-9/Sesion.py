# '''Importación de librerías'''
import pygame

# '''Configuración del juego'''
SCREENSIZE = 500
running = True
cabezaX = 50
cabezaY = 50
anchoDePixel = 10
altoDePixel = 10
vel = 10

serpiente = [(cabezaX,cabezaY)]

# '''Definición de la función principal del juego'''
def main():
    global SCREENSIZE
    global running
    global cabezaX
    global cabezaY
    global anchoDePixel
    global altoDePixel
    global serpiente
    global vel

    pygame.init()
    win = pygame.display.set_mode((SCREENSIZE,SCREENSIZE))
    pygame.display.set_caption("SnakeGame")
    # '''Ciclo de vida del juego'''
    while running: 
        pygame.time.delay(100)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            cabezaX += vel
        elif keys[pygame.K_LEFT]:
            cabezaX -= vel
        elif keys[pygame.K_UP]:
            cabezaY -= vel
        elif keys[pygame.K_DOWN]:
            cabezaY += vel

        win.fill((0,0,0))

        #for pixel in serpiente:
        pygame.draw.rect(win, (255,0,0), (cabezaX,cabezaY,anchoDePixel,altoDePixel))
        pygame.display.update()

    pygame.quit()
# '''Ejecutar el juego'''
main()