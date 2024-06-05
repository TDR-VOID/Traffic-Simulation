import pygame

# Initialize the game engine
pygame.init()

# Set the dimensions of the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the caption of the game window
pygame.display.set_caption("Traffic Simulation")

# Define the dimensions of the car
CAR_WIDTH = 50
CAR_HEIGHT = 20

# Define the initial position of the car
car_x = 100
car_y = WINDOW_HEIGHT // 2

# Define the velocity of the car
velocity = 0.1

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the position of the car
    car_x += velocity
    if car_x > WINDOW_WIDTH - CAR_WIDTH:
        car_x = 0

    # Clear the window
    window.fill((0, 0, 0))

    # Draw the car
    pygame.draw.rect(window, (255, 0, 0), (car_x, car_y, CAR_WIDTH, CAR_HEIGHT))

    # Update the display
    pygame.display.flip()
