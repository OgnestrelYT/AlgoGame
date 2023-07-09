import time

class Cor:
    def __init__(self):
        self.synt_er = True
        self.x_pl_pr = 0
        self.y_pl_pr = 0
        self.x_pl = 0
        self.y_pl = 0
        self.conf = ""
        self.flag_st = False

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

    def start(self, inp, game_map):
        inp.lower()
        a = inp.split("\n")
        self.conf = ""
        for line in a:
            self.check_st(game_map, self.x_pl, self.y_pl)
            if self.synt_er == False:
                self.conf = "Syntax error"
                break
            elif self.flag_st:
                self.conf = "Stolknovenie"
                break
            else:
                if line == "вниз":
                    self.y_pl += 1
                elif line == "вверх":
                    self.y_pl -= 1
                elif line == "влево":
                    self.x_pl -= 1
                elif line == "вправо":
                    self.x_pl += 1

    def pl(self, game_map):
        y = 0
        for layer in game_map:
            x = 0
            for tile in layer:
                if tile == "0":
                    self.x_pl += 1
                    if self.x_pl > 13:
                        self.y_pl += 1
                        self.x_pl = 0
                x += 1
            y += 1

    def check_st(self, game_map, x, y):
         if game_map[y][x] == "2":
             print(11111111111111111111111111111111111111111111111111111111111111111111111111111111)
             self.flag_st = True
         else:
             self.flag_st = False
