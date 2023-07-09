import sys

import pygame
from blit import Blit


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
        self.flag_col = False
        self.flag_finish = False
        self.bon_count = 0
        self.dey = []
        self.bon_m = []
        self.zap = True
        self.blit = Blit()
        self.font = pygame.font.Font('data/fonts/finish.ttf', 60)
        self.font_sm = pygame.font.Font('data/fonts/finish.ttf', 30)
        self.finish = self.font.render("Ты прошёл этот уровень!", True, (0, 0, 0))
        self.bon_count_s = self.font_sm.render("Ты набрал " + str(self.bon_count) + " из 3 звёздочек", True, (0, 0, 0))
        self.direction = "вправо"
        self.vraz_list = ["20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "03", "06",
                     "07", "08", "09", "10", "11"]
        self.finish_list = ["51", "52"]

    def synt_check(self, inp):
        inp.lower()
        inp = inp[:-1]
        a = inp.split("\n")
        for line in a:
            b = line.split(" ")
            if len(line) > 0:
                if line == "вниз":
                    self.synt_er = True
                elif line == "вверх":
                    self.synt_er = True
                elif line == "влево":
                    self.synt_er = True
                elif line == "вправо":
                    self.synt_er = True
                elif len(b) > 3:
                    if (b[0] == "повторять") and ((int(b[1]) > 0) and (int(b[1])) < 20) and \
                            ((b[2] == "раз") or (b[2] == "раза")) and \
                            ((b[3] == "вниз") or (b[3] == "вверх") or \
                            (b[3] == "влево") or (b[3] == "вправо")):
                        self.synt_er = True
                    else:
                        self.synt_er = False
                        break
                else:
                    self.synt_er = False
                    break
            else:
                self.synt_er = True
                break

    def start(self, inp, game_map, disp, pl, levelMessage, bonuseMessage):
        inp = inp[:-1]
        self.flag_finish = False
        self.bon_count = 0
        player = pygame.transform.rotate(pl, 0)
        inp.lower()
        a = inp.split("\n")
        disp.blit(player, (self.x_pl * 90 + 660, self.y_pl * 90))
        self.conf = ""
        for line in a:
            b = line.split(" ")
            self.check_st(game_map, self.x_pl, self.y_pl)
            if self.flag_bon:
                self.bon_count += 1
            if self.flag_col:
                self.conf = "Slishkom mnogo"
                break
            if self.synt_er == False:
                self.conf = "Ошибка синтаксиса"
                break
            elif self.flag_st:
                break
            else:
                self.blit.blit(disp, self.bon_count, levelMessage, game_map, player, self.x_pl, self.y_pl, 250)
                if line == "вниз":
                    self.y_pl += 1
                    player = pygame.transform.rotate(pl, -90)
                    self.direction = "вниз"
                elif line == "вверх":
                    self.y_pl -= 1
                    player = pygame.transform.rotate(pl, +90)
                    self.direction = "вверх"
                elif line == "влево":
                    self.x_pl -= 1
                    player = pygame.transform.flip(pl, True, False)
                    self.direction = "влево"
                elif line == "вправо":
                    self.x_pl += 1
                    player = pygame.transform.rotate(pl, 0)
                    self.direction = "вправо"
                elif len(b) > 3:
                    if (b[0] == "повторять") and ((b[2] == "раз") or (b[2] == "раза")):
                        i = int(b[1])
                        for l in range(i):
                            if b[3] == "вниз":
                                self.y_pl += 1
                                player = pygame.transform.rotate(pl, -90)
                                self.direction = "вниз"
                            elif b[3] == "вверх":
                                self.y_pl -= 1
                                player = pygame.transform.rotate(pl, +90)
                                self.direction = "вверх"
                            elif b[3] == "влево":
                                self.x_pl -= 1
                                player = pygame.transform.flip(pl, True, False)
                                self.direction = "влево"
                            elif b[3] == "вправо":
                                self.x_pl += 1
                                player = pygame.transform.rotate(pl, 0)
                                self.direction = "вправо"
                            self.check_st(game_map, self.x_pl, self.y_pl)
                            self.blit.blit(disp, self.bon_count, levelMessage, game_map, player, self.x_pl, self.y_pl, 500)


                if line == "вниз":
                    player = pygame.transform.rotate(pl, -90)
                elif line == "вверх":
                    player = pygame.transform.rotate(pl, +90)
                elif line == "влево":
                    player = pygame.transform.flip(pl, True, False)
                elif line == "вправо":
                    player = pygame.transform.rotate(pl, 0)

                self.blit.blit(disp, self.bon_count, levelMessage, game_map, player, self.x_pl, self.y_pl, 250)
        self.check_st(game_map, self.x_pl, self.y_pl)
        if self.flag_finish:
            cl = False
            while self.flag_finish:
                self.bon_count_s = self.font_sm.render("Ты набрал " + str(self.bon_count) + " из 3 звёздочек", True,
                                                      (0, 0, 0))
                disp.blit(self.finish, (disp.get_width() / 2 - self.finish.get_width() / 2,
                                        disp.get_height() / 2 - self.finish.get_height() / 2))
                disp.blit(self.bon_count_s, (disp.get_width() / 2 - self.bon_count_s.get_width() / 2,
                                            disp.get_height() / 2 - self.bon_count_s.get_height() / 2 + 100))

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        cl = True
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            cl = True

                pygame.display.update()
                pygame.time.delay(10)

                if cl:
                    self.flag_finish = False


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
         if game_map[y][x] in self.vraz_list:
             self.flag_st = True
             self.conf = "Столкновение"
         else:
             self.flag_st = False

         if game_map[y][x] == "04":
             game_map[y][x] = "01"
             self.bon_count += 1
         else:
             self.flag_bon = False

         if game_map[y][x] in self.finish_list:
             self.flag_finish = True
         else:
             self.flag_finish = False

#עשדשגכניחדגנכנבסצמנזהחעוטרעון׳טקעכיחגדה