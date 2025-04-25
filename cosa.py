
import pygame
import random
import sys

pygame.init()

ANCHO, ALTO = 640, 480
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Atrapa la moneda")

AZUL = (0, 0, 255)
DORADO = (255, 215, 0)
BLANCO = (255, 255, 255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
carmesí = (220,20,60)

class Pollito(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(DORADO)
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2, ALTO // 2)

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:  self.rect.x -= 5
        if teclas[pygame.K_RIGHT]: self.rect.x += 5
        if teclas[pygame.K_UP]:    self.rect.y -= 5
        if teclas[pygame.K_DOWN]:  self.rect.y += 5

        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > ANCHO: self.rect.right = ANCHO
        if self.rect.top < 0: self.rect.top = 0
        if self.rect.bottom > ALTO: self.rect.bottom = ALTO


class Carro(pygame.sprite.Sprite):
    def __init__(self, color, velocidad, y_pos):
        # La posición en X empieza fuera de la pantalla, a la izquierda (fuera de la pantalla)
        self.rect = pygame.Rect(-60, y_pos, 60, 30)  # Posición en Y fija
        self.color = (carmesí)
        self.velocidad = (velocidad)

    def mover(self):
        # Mover el carro de izquierda a derecha
        self.rect.x += self.velocidad
        # Si el carro sale de la pantalla, lo ponemos de vuelta al inicio (a la izquierda)
        if self.rect.x > 600:
            self.rect.x = -60  # Ponerlo fuera de la pantalla en el lado izquierdo

    for _ in range(5):  # Crear 5 carros en la primera línea
        color = random.choice([rojo, azul, gold, carmesí])
        velocidad = random.randint(2, 6)  # Velocidades aleatorias entre 2 y 6
        carro = Carro(color, velocidad, 100)
        carros_linea1.append(carro)

    # Crear carros para la línea 2 (a Y = 300)
    for _ in range(5):  # Crear 5 carros en la segunda línea
        color = random.choice([rojo, azul, gold, carmesí])
        velocidad = random.randint(2, 6)  # Velocidades aleatorias entre 2 y 6
        carro = Carro(color, velocidad, 300)
        carros_linea2.append(carro)


# Crear carros para la línea 2 (a Y = 300)
for _ in range(5):  # Crear 5 carros en la segunda línea
    color = random.choice([rojo, azul, gold, carmesí])
    velocidad = random.randint(2, 6)  # Velocidades aleatorias entre 2 y 6
    carro = Carro(color, velocidad, 300)
    carros_linea2.append(carro)

    

pollito = Pollito()
carro = Carro()

sprites = pygame.sprite.Group()
sprites.add(pollito)
sprites.add(carro)

vidas = 3
fuente = pygame.font.SysFont(None, 36)

tiempo = 30  # 30 segundos
fuente_tiempo = pygame.font.SysFont(None, 48)

reloj = pygame.time.Clock()
jugando = True

while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Actualizar sprites
    sprites.update()

    # Comprobar colisión
    if pygame.sprite.collide_rect(pollito, carro):
        vidas -= 1
        carro.nueva_posicion()

    tiempo -= 1 / 60  # 1/60 por cada frame (60 FPS)
    if tiempo <= 0:
        jugando = False  # Terminar el juego cuando el tiempo se acaba

    # Dibujar todo
    pantalla.fill(BLANCO)
    sprites.draw(pantalla)

    # Mostrar puntuación
    texto = fuente.render(f"Puntos: {puntos}", True, NEGRO)
    pantalla.blit(texto, (10, 10))

    pygame.display.flip()
    reloj.tick(60)

pantalla.fill(BLANCO)
texto_final = fuente.render(f"¡Juego Terminado! Puntos: {puntos}", True, NEGRO)
pantalla.blit(texto_final, (ANCHO // 2 - 150, ALTO // 2 - 20))
pygame.display.flip()

pygame.time.wait(3000)

pygame.quit()
sys.exit()