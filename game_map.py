import pygame


class GameMap():
    def __init__(self):
        self.grass = pygame.image.load('data/gfx/grass.png')
        self.stone = pygame.image.load('data/gfx/stone.png')
        self.top_left_riv = pygame.image.load('data/gfx/top_left.png')
        self.top_right_riv = pygame.image.load('data/gfx/top_right.png')
        self.bottom_left_riv = pygame.image.load('data/gfx/bottom_left.png')
        self.bottom_right_riv = pygame.image.load('data/gfx/bottom_right.png')
        self.vert_riv = pygame.image.load('data/gfx/vert.png')
        self.goriz_riv = pygame.image.load('data/gfx/goriz.png')
        self.finish = pygame.image.load('data/gfx/finish.png')
        self.tree = pygame.image.load('data/gfx/tree.png')
        self.bonuse = pygame.image.load('data/gfx/bonuse.png')

    def game_map(self, game_map, DISPLAY):
        y = 0
        for layer in game_map:
            x = 0
            for tile in layer:
                if tile == '01':  # Grass
                    DISPLAY.blit(self.grass, (x * 90 + 660, y * 90))
                if tile == '02':  # Stone
                    DISPLAY.blit(self.stone, (x * 90 + 660, y * 90))
                if tile == '03':  # Tree
                    DISPLAY.blit(self.tree, (x * 90 + 660, y * 90))
                if tile == '04':  # Bonuse
                    DISPLAY.blit(self.bonuse, (x * 90 + 660, y * 90))
                if tile == '05':  # Finish
                    DISPLAY.blit(self.finish, (x * 90 + 660, y * 90))
                if tile == '06':  # Gor river
                    DISPLAY.blit(self.goriz_riv, (x * 90 + 660, y * 90))
                if tile == '07':  # Vert river
                    DISPLAY.blit(self.vert_riv, (x * 90 + 660, y * 90))
                if tile == '08':  # Top left river
                    DISPLAY.blit(self.top_left_riv, (x * 90 + 660, y * 90))
                if tile == '09':  # Top right river
                    DISPLAY.blit(self.top_right_riv, (x * 90 + 660, y * 90))
                if tile == '10':  # Bottom left river
                    DISPLAY.blit(self.bottom_left_riv, (x * 90 + 660, y * 90))
                if tile == '11':  # Bottom right river
                    DISPLAY.blit(self.bottom_right_riv, (x * 90 + 660, y * 90))
                x += 1
            y += 1
