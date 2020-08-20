import pygame

ancho = 240
altura = 180

def main():
    x = 50
    y = 50
    velocidad = 1

    pygame.init()
    pygame.display.set_caption("test")

    pantalla = pygame.display.set_mode((ancho, altura))

    corriendo = True
    while corriendo:
        pygame.time.delay(100) # delay siempre presente en lo que se ejecuta cada acción

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # mientras no salga del juego, no se cierra
                corriendo = False

        teclas = pygame.key.get_pressed() # cual es la tecla que el usuario presiono

        # validar la dirección del movimiento del rectangulo segun la tecla presionada
        if teclas[pygame.K_LEFT]:
            x -= velocidad
        
        if teclas[pygame.K_RIGHT]:
            x += velocidad

        if teclas[pygame.K_UP]:
            y -= velocidad
        
        if teclas[pygame.K_DOWN]:
            y += velocidad


        pantalla.fill((0, 0, 0)) # limpia pantalla
        pygame.draw.rect(pantalla, (255, 0, 0), (x, y, 40, 60)) # dibuja el rectangulo
        pygame.display.update() # actualiza pantalla

main()