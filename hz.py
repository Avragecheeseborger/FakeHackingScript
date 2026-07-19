import pygame
import random
import sys

running = True
# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (150, 0, 150)
LIGHT_BLUE = (0, 150, 255)
ORANGE = (255, 150, 0)

# Set up the display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
pygame.display.set_caption("app")
font = pygame.font.Font(None, 40)
font1 = pygame.font.Font(None, 50)
textsurf = font.render("", True, GREEN, BLACK)
hax = False
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hax = not hax  # Toggle the hax variable
            if event.key == pygame.K_ESCAPE:
                running = False  # Exit the loop and close the application
    
    screen.fill(BLACK)
    x, y = 10, 10
    line = 0
    col = 0
    linetext = ""
    text = "".join(chr(random.randint(32, 126)) for _ in range(2500))
    place = 0
    if not hax:
        len = random.randint(20, 100)
        for char in text:
            place += 1
            linetext += char
            textsurf = font.render(f"{linetext}", True, GREEN, BLACK)
            trect = textsurf.get_rect()
            trect.topleft = (x + col * 18, y + line * 30)
            linetext = ""
            screen.blit(textsurf, trect)
            col += 1
            if col >= len:
                col = 0
                if random.randint(0, 20) == 0:
                    line += 1
                line += 1
                len = random.randint(20, 100)
    else:
        textsurf = font1.render(f"ACCESS GRANTED", True, GREEN, BLACK)
        trect = textsurf.get_rect()
        trect.center = (width//2 + line * 20, height//2)
        screen.blit(textsurf, trect)
    pygame.display.flip()
    clock.tick(20)

pygame.quit()
sys.exit()
