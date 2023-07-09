import pygame
from game_map import GameMap


class Cor:
    def __init__(self):
        self.synt_er = True
        self.x_pl_pr = 0
        self.y_pl_pr = 0
        self.x_pl = 0
        self.y_pl = 0
        self.conf = ""
        self.flag_st = False
        self.flag_bon = False
        self.bon_count = 0
        self.dey = []
        self.bon_m = []
        self.zap = True
        self.gamm = GameMap()

    def synt_check(self, inp):
        inp.lower()
        a = inp.split("\n")
        for line in a:
            if line == "вниз":
                self.synt_er = True
            elif line == "вверх":
                self.synt_er = True
            elif line == "влево":
                self.synt_er = True
            elif line == "вправо":
                self.synt_er = True
            else:
                self.synt_er = False

    def start(self, inp, game_map, disp, pl, levelMessage, bonuseMessage):
        player = pygame.transform.rotate(pl, 0)
        inp.lower()
        a = inp.split("\n")
        disp.blit(player, (self.x_pl * 90 + 660, self.y_pl * 90))
        self.conf = ""
        for line in a:
            self.check_st(game_map, self.x_pl, self.y_pl)
            if self.flag_bon:
                self.bon_count += 1
            if self.synt_er == False:
                self.conf = "Syntax error"
                break
            elif self.flag_st:
                self.conf = "Stolknovenie"
                break
            else:
                if line == "вниз":
                    self.dey.append("вниз")
                    self.y_pl += 1
                    player = pygame.transform.rotate(pl, -90)
                elif line == "вверх":
                    self.y_pl -= 1
                    player = pygame.transform.rotate(pl, +90)
                elif line == "влево":
                    self.x_pl -= 1
                    player = pygame.transform.flip(pl, True, False)
                elif line == "вправо":
                    self.x_pl += 1
                    player = pygame.transform.rotate(pl, 0)
                disp.blit(bonuseMessage, (5, 1040))
                disp.blit(levelMessage, (550, 1040))
                self.gamm.game_map(game_map, disp)
                disp.blit(player, (self.x_pl * 90 + 660, self.y_pl * 90))
                pygame.display.update()
                pygame.time.delay(500)


    def pl(self, game_map):
        y = 0
        for layer in game_map:
            x = 0
            for tile in layer:
                if tile == "00":
                    self.x_pl += 1
                    if self.x_pl > 13:
                        self.y_pl += 1
                        self.x_pl = 0
                x += 1
            y += 1

    def check_st(self, game_map, x, y):
         if game_map[y][x] == "01":
             print(game_map[y][x])
             print("///////////01")
             self.flag_st = False
         elif game_map[y][x] == "04":
             print(game_map[y][x])
             print(11111111111111111111111111111111111111111111111111111111111111111111111111111111)
             self.flag_st = False
         elif game_map[y][x] == "05":
             print(game_map[y][x])
             print(11111111111111111111111111111111111111111111111111111111111111111111111111111111)
             self.flag_st = False
         elif game_map[y][x] == "xx":
             print("predeli")
             self.flag_st = True
         else:
             print(21874286587469376567548978695768957)
             self.flag_st = True

         if game_map[y][x] == "04":
             print(self.bon_m)
             self.bon_m.append(str(x) + " " + str(y))
             print("Bonuse")
             self.flag_bon = True
         else:
             self.flag_bon = False
