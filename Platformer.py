import pygame,sys
from Settings import *

pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPS = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.fill("Black")

    pygame.display.update()
    FPS.tick(60)

for row_index,row in enumerate(layout):
    for col_index,cel in enumerate(row):
        x = col_index * tile_size
        y = row_index * tile_size

        if cell == "X":
            tile = Tile((x,y), tile_size)
            self.tiles.add(tile)