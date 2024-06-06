
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

# Define the initial positions of the cars
cars = [
    {"x": 100, "y": 100, "color": (255, 0, 0)},
    {"x": 200, "y": 300, "color": (0, 255, 0)},
    {"x": 300, "y": 200, "color": (0, 0, 255)},
    {"x": 400, "y": 100, "color": (255, 255, 0)},
    {"x": 500, "y": 300, "color": (255, 0, 255)}
]

# Define the velocity of the cars
velocity = 0.1

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the positions of the cars
    for car in cars:
        car["x"] += velocity
        if car["x"] > WINDOW_WIDTH - CAR_WIDTH:
            car["x"] = 0

    # Clear the window
    window.fill((0, 0, 0))

    # Draw the cars
    for car in cars:
        pygame.draw.rect(window, car["color"], (car["x"], car["y"], CAR_WIDTH, CAR_HEIGHT))

    # Draw the lanes
    pygame.draw.line(window, (255, 255, 255), (0, WINDOW_HEIGHT // 2), (WINDOW_WIDTH, WINDOW_HEIGHT // 2), 10)
    pygame.draw.line(window, (255, 255, 255), (0, WINDOW_HEIGHT // 6), (WINDOW_WIDTH, WINDOW_HEIGHT // 6), 10)
   

    # Update the display
    pygame.display.flip()

