import pygame, random
import sys

rojo = (255,0,0)
azul = (0,0,255)
verde = (144,238,144)
gold = (255,215,0)
azul_oscuro = (72,61,139)
carmesí = (220,20,60)
gris_claro = (169, 169, 169)
rojo_claro = (205, 92, 92)
negro = (0,0,0)
blanco = (255,255,255)
gris = (128, 128, 128)


pygame.init()

ventana = pygame.display.set_mode((600,600))
pygame.display.set_caption("No mates al pollito")
clock = pygame.time.Clock()

ventana.fill(verde)

pygame.draw.rect(ventana, gold, (50, 490, 120, 100))
pygame.draw.rect(ventana, azul_oscuro, (240, 450, 110, 140))
pygame.draw.rect(ventana, carmesí, (430, 460, 110, 130))
pygame.draw.rect(ventana, gris_claro, (475, 540, 25, 50))
pygame.draw.rect(ventana, rojo_claro, (285, 550, 25, 40))
pygame.draw.rect(ventana, negro, (95, 545, 30, 45))
pygame.draw.rect(ventana, gris_claro, (0, 150, 600, 250))
pygame.draw.rect(ventana, gris, (0, 110, 600, 40))
pygame.draw.rect(ventana, gris, (0, 400, 600, 40))
pygame.draw.rect(ventana, gold, (0, 270, 600, 20))
pygame.draw.line(ventana, blanco, (0, 210), (600,210), 4)
pygame.draw.line(ventana, blanco, (0, 350), (600,350), 4)

class Pollito(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(gold)
        self.rect = self.image.get_rect()
        self.rect.center = (600 // 2, 600 // 2)

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:  self.rect.x -= 5
        if teclas[pygame.K_RIGHT]: self.rect.x += 5
        if teclas[pygame.K_UP]:    self.rect.y -= 5
        if teclas[pygame.K_DOWN]:  self.rect.y += 5

        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > 600: self.rect.right = 600
        if self.rect.top < 0: self.rect.top = 0
        if self.rect.bottom > 600: self.rect.bottom = 600



class Carro:
    def __init__(self, color, velocidad, y_pos):
        # La posición en X empieza fuera de la pantalla, a la izquierda (fuera de la pantalla)
        self.rect = pygame.Rect(-60, y_pos, 60, 30)  # Posición en Y fija
        self.color = color
        self.velocidad = velocidad
    
    def mover(self):
        # Mover el carro de izquierda a derecha
        self.rect.x += self.velocidad
        # Si el carro sale de la pantalla, lo ponemos de vuelta al inicio (a la izquierda)
        if self.rect.x > 600:
            self.rect.x = -60  # Ponerlo fuera de la pantalla en el lado izquierdo

    def dibujar(self, pantalla):
        # Dibujar el carro en la pantalla
        pygame.draw.rect(pantalla, self.color, self.rect)

# Crear una lista de carros para la primera línea (Y = 100) y la segunda línea (Y = 300)
carros_linea1 = []
carros_linea2 = []

# Crear carros para la línea 1 (a Y = 100)
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

pollito = (Pollito)
carro = (Carro)

sprites = pygame.sprite.Group()
sprites.add(carro)
sprites.add(pollito)

vidas = 3
fuente = pygame.font.SysFont(None, 36)
jugando = True



while 1:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    for carro in carros_linea1:
        carro.mover()
        carro.dibujar(ventana)

    for carro in carros_linea2:
        carro.mover()
        carro.dibujar(ventana)

    if pygame.sprite.collide_rect(Carro, Pollito):
        vidas -=3

    
    pygame.display.flip()
    pygame.time.Clock().tick(60)
    