import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la ventana
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Cuadrado en movimiento")

# Definir los colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Crear el cuadrado
cuadrado = pygame.Rect(100, 250, 50, 50)  # posición inicial (x, y), tamaño (ancho, alto)
velocidad = 5  # Velocidad del movimiento

# Variable de control para salir del bucle
cuadrado_moviéndose = True

# Bucle principal
while cuadrado_moviéndose:
    # Comprobar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            cuadrado_moviéndose = False

    # Mover el cuadrado de un lado a otro
    cuadrado.x += velocidad

    # Si el cuadrado llega al final de la pantalla, detener el movimiento
    if cuadrado.x >= ANCHO:
        cuadrado_moviéndose = False

    # Rellenar la pantalla con blanco
    pantalla.fill(BLANCO)

    # Dibujar el cuadrado en la pantalla
    pygame.draw.rect(pantalla, ROJO, cuadrado)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de fotogramas
    pygame.time.Clock().tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()