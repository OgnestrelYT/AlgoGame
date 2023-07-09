import pygame
from game_map import GameMap

class Blit:
    def __init__(self):
        self.gamm = GameMap()
        self.font_small = pygame.font.Font('data/fonts/font.otf', 50)

    def blit(self, disp, bonuseMessage, levelMessage, game_map, player, x_pl, y_pl, tim):
        self.bonuseMessage = self.font_small.render(str(bonuseMessage), True, (0, 0, 0))
        pygame.draw.rect(disp, (72, 61, 139), pygame.Rect(3, 85, 640, 740), 7, 3)
        disp.blit(levelMessage, (515, 1025))
        self.gamm.game_map(game_map, disp)
        disp.blit(player, (x_pl * 90 + 660, y_pl * 90))
        pygame.display.update()
        pygame.time.delay(tim)