import pygame
import random

# Inicializar Pygame
pygame.init()

# Tamaño de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("El Pollito Cruza la Calle")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Configuración del pollito
pollito_width = 40
pollito_height = 40
pollito_x = WIDTH // 2 - pollito_width // 2
pollito_y = HEIGHT - pollito_height - 10
pollito_speed = 5

# Configuración de los carros
car_width = 60
car_height = 30
car_speed = 5
cars = []

# Reloj para controlar la tasa de cuadros por segundo (FPS)
clock = pygame.time.Clock()

# Función para dibujar el pollito
def draw_pollito(x, y):
    pygame.draw.rect(screen, YELLOW, (x, y, pollito_width, pollito_height))

# Función para dibujar los carros
def draw_car(x, y):
    pygame.draw.rect(screen, RED, (x, y, car_width, car_height))

# Función para mover los carros
def move_cars(cars):
    for car in cars:
        car['y'] += car['speed']
        if car['y'] > HEIGHT:
            car['y'] = -car_height
            car['x'] = random.randint(0, WIDTH - car_width)
            car['speed'] = random.choice([3, 4, 5])

# Función principal del juego
def game():
    global pollito_x, pollito_y
    running = True
    while running:
        screen.fill(WHITE)
        
        # Detectar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Mover el pollito con las teclas de dirección
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and pollito_x > 0:
            pollito_x -= pollito_speed
        if keys[pygame.K_RIGHT] and pollito_x < WIDTH - pollito_width:
            pollito_x += pollito_speed
        if keys[pygame.K_UP] and pollito_y > 0:
            pollito_y -= pollito_speed
        if keys[pygame.K_DOWN] and pollito_y < HEIGHT - pollito_height:
            pollito_y += pollito_speed
        
        # Generar carros de manera aleatoria en las dos vías
        if random.randint(1, 30) == 1:
            car_lane = random.choice([1, 2])
            if car_lane == 1:  # Carriles de izquierda a derecha
                cars.append({
                    'x': random.randint(0, WIDTH - car_width),
                    'y': -car_height,
                    'speed': random.choice([3, 4, 5])
                })
            else:  # Carriles de derecha a izquierda
                cars.append({
                    'x': random.randint(0, WIDTH - car_width),
                    'y': -car_height,
                    'speed': -random.choice([3, 4, 5])
                })
        
        # Dibujar los carros y moverlos
        move_cars(cars)
        for car in cars:
            draw_car(car['x'], car['y'])
        
        # Dibujar el pollito
        draw_pollito(pollito_x, pollito_y)
        
        # Verificar colisiones (si el pollito toca un carro)
        for car in cars:
            if car['x'] < pollito_x + pollito_width and car['x'] + car_width > pollito_x and car['y'] < pollito_y + pollito_height and car['y'] + car_height > pollito_y:
                print("¡Game Over! El pollito fue atropellado.")
                running = False

        # Actualizar la pantalla
        pygame.display.update()
        
        # Limitar los cuadros por segundo
        clock.tick(60)

    pygame.quit()

# Iniciar el juego
game()