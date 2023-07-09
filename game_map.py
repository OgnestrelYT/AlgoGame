import pygame


class GameMap():
    def __init__(self):
        self.grass = pygame.image.load('data/gfx/grass.png')

        self.stone_cor_left_top = pygame.image.load('data/gfx/stone_cor_left_top.png')
        self.stone_cor_right_top = pygame.image.load('data/gfx/stone_cor_right_top.png')
        self.stone_cor_left_bottom = pygame.image.load('data/gfx/stone_cor_left_bottom.png')
        self.stone_cor_right_bottom = pygame.image.load('data/gfx/stone_cor_right_bottom.png')
        self.stone_sr_top = pygame.image.load('data/gfx/stone_sr_top.png')
        self.stone_sr_bottom = pygame.image.load('data/gfx/stone_sr_bottom.png')
        self.stone_sr_left = pygame.image.load('data/gfx/stone_sr_left.png')
        self.stone_sr_right = pygame.image.load('data/gfx/stone_sr_right.png')
        self.stone_all = pygame.image.load('data/gfx/stone_all.png')
        self.stone_vogn_left_top = pygame.image.load('data/gfx/stone_vogn_left_top.png')
        self.stone_vogn_right_top = pygame.image.load('data/gfx/stone_vogn_right_top.png')
        self.stone_vogn_left_bottom = pygame.image.load('data/gfx/stone_vogn_left_bottom.png')
        self.stone_vogn_right_bottom = pygame.image.load('data/gfx/stone_vogn_right_bottom.png')
        self.stone_center = pygame.image.load('data/gfx/stone.png')

        self.top_left_riv = pygame.image.load('data/gfx/river_left_top.png')
        self.top_right_riv = pygame.image.load('data/gfx/river_right_top.png')
        self.bottom_left_riv = pygame.image.load('data/gfx/river_left_buttom.png')
        self.bottom_right_riv = pygame.image.load('data/gfx/river_right_buttom.png')
        self.vert_riv = pygame.image.load('data/gfx/vert.png')
        self.goriz_riv = pygame.image.load('data/gfx/goriz.png')
        self.finish_hor = pygame.image.load('data/gfx/finish_hor.png')
        self.finish_vert = pygame.image.load('data/gfx/finish_vert.png')
        self.tree = pygame.image.load('data/gfx/tree.png')
        self.bonuse = pygame.image.load('data/gfx/bonuse.png')
        self.vert_most = pygame.image.load("data/gfx/bridge_vert.png")
        self.goriz_most = pygame.image.load("data/gfx/bridge_hor.png")

    def game_map(self, game_map, DISPLAY):
        y = 0
        for layer in game_map:
            x = 0
            for tile in layer:
                if tile == '01':  # Grass
                    DISPLAY.blit(self.grass, (x * 90 + 660, y * 90))

                elif tile == '20':  # Stone
                    DISPLAY.blit(self.stone_cor_left_top, (x * 90 + 660, y * 90))
                elif tile == '21':  # Stone
                    DISPLAY.blit(self.stone_cor_right_top, (x * 90 + 660, y * 90))
                elif tile == '22':  # Stone
                    DISPLAY.blit(self.stone_cor_left_bottom, (x * 90 + 660, y * 90))
                elif tile == '23':  # Stone
                    DISPLAY.blit(self.stone_cor_right_bottom, (x * 90 + 660, y * 90))
                elif tile == '24':  # Stone
                    DISPLAY.blit(self.stone_sr_top, (x * 90 + 660, y * 90))
                elif tile == '25':  # Stone
                    DISPLAY.blit(self.stone_sr_bottom, (x * 90 + 660, y * 90))
                elif tile == '26':  # Stone
                    DISPLAY.blit(self.stone_sr_left, (x * 90 + 660, y * 90))
                elif tile == '27':  # Stone
                    DISPLAY.blit(self.stone_sr_right, (x * 90 + 660, y * 90))
                elif tile == '28':  # Stone
                    DISPLAY.blit(self.stone_all, (x * 90 + 660, y * 90))
                elif tile == '29':  # Stone
                    DISPLAY.blit(self.stone_vogn_left_top, (x * 90 + 660, y * 90))
                elif tile == '30':  # Stone
                    DISPLAY.blit(self.stone_vogn_right_top, (x * 90 + 660, y * 90))
                elif tile == '31':  # Stone
                    DISPLAY.blit(self.stone_vogn_left_bottom, (x * 90 + 660, y * 90))
                elif tile == '32':  # Stone
                    DISPLAY.blit(self.stone_vogn_right_bottom, (x * 90 + 660, y * 90))
                elif tile == '33':  # Stone
                    DISPLAY.blit(self.stone_center, (x * 90 + 660, y * 90))

                elif tile == '03':  # Tree
                    DISPLAY.blit(self.tree, (x * 90 + 660, y * 90))
                elif tile == '04':  # Bonuse
                    DISPLAY.blit(self.bonuse, (x * 90 + 660, y * 90))
                elif tile == '51':  # Finish vert
                    DISPLAY.blit(self.finish_vert, (x * 90 + 660, y * 90))
                elif tile == '52':  # Finish hor
                    DISPLAY.blit(self.finish_hor, (x * 90 + 660, y * 90))
                elif tile == '06':  # Gor river
                    DISPLAY.blit(self.goriz_riv, (x * 90 + 660, y * 90))
                elif tile == '07':  # Vert river
                    DISPLAY.blit(self.vert_riv, (x * 90 + 660, y * 90))
                elif tile == '08':  # Top left river
                    DISPLAY.blit(self.top_left_riv, (x * 90 + 660, y * 90))
                elif tile == '09':  # Top right river
                    DISPLAY.blit(self.top_right_riv, (x * 90 + 660, y * 90))
                elif tile == '10':  # Bottom left river
                    DISPLAY.blit(self.bottom_left_riv, (x * 90 + 660, y * 90))
                elif tile == '11':  # Bottom right river
                    DISPLAY.blit(self.bottom_right_riv, (x * 90 + 660, y * 90))
                elif tile == '12':  #
                    DISPLAY.blit(self.vert_most, (x * 90 + 660, y * 90))
                elif tile == '13':  #
                    DISPLAY.blit(self.goriz_most, (x * 90 + 660, y * 90))
                x += 1
            y += 1
