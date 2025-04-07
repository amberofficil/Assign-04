import pygame
import time

pygame.init()

CANVA_WIDTH = 400
CANVA_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

BLUE = (0, 0, 225)
WHITE = (225, 225, 225)
PINK = (225, 182, 193)

# Screen set karo
screen = pygame.display.set_mode((CANVA_WIDTH, CANVA_HEIGHT))
pygame.display.set_caption("Enter effect in pygame")

# Grid banani hai
gride = []
for row in range(0, CANVA_HEIGHT, CELL_SIZE):
    for col in range(0, CANVA_WIDTH, CELL_SIZE):
        rect = pygame.Rect(col, row, CELL_SIZE, CELL_SIZE)
        gride.append(rect)

# Eraser set karo
eraser = pygame.Rect(200, 200, ERASER_SIZE, ERASER_SIZE)

# Game loop chalao
running = True
while running:
    screen.fill(WHITE)

    # Mouse ka position lo
    mouse_x, mouse_y = pygame.mouse.get_pos()
    eraser.topleft = (mouse_x, mouse_y)

    # Grid ko draw karo aur collision check karo
    new_gride = []
    for rect in gride:
        if not eraser.colliderect(rect):
            pygame.draw.rect(screen, BLUE, rect)
            new_gride.append(rect)

    gride = new_gride

    # Eraser ko draw karo
    pygame.draw.rect(screen, PINK, eraser)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    time.sleep(0.05)

pygame.quit()

