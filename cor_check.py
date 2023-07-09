class Cor:
    def __init__(self):
        self.flag = True
        self.x_pl_pr = 0
        self.y_pl_pr = 0
        self.x_pl = 0
        self.y_pl = 0
        self.conf = ""
        self.flag_st = False

    def update(self, inp):
        inp.lower()
        a = inp.split("\n")
        for line in a:
            if line == "вниз":
                self.flag = True
            elif line == "вверх":
                self.flag = True
            elif line == "влево":
                self.flag = True
            elif line == "вправо":
                self.flag = True
            else:
                self.flag = False

    def start(self, inp, game_map):
        inp.lower()
        a = inp.split("\n")
        self.conf = ""
        for line in a:
            self.check_st(game_map, self.x_pl, self.y_pl)
            if self.flag == False:
                self.conf = "Syntax error"
                break
            else:
                if self.flag_st:
                    self.flag = False
                    self.conf = "stolknovenie"
                    break
                elif line == "вниз":
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
             self.flag_st = True
         else:
             self.flag_st = False
