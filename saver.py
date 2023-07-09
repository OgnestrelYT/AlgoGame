
class Saver:
    def __init__(self):
        self.lvl_file = ""
        self.from_file_end = ""
        self.from_file = []

    def save_code(self, inp_txt, i):
        self.lvl_file = "data/lvls/edited/" + str(i) +".txt"
        with open(self.lvl_file, "w") as file:
            file.write(str(inp_txt))
            file.close()

    def enter_code(self, i):
        self.lvl_file = "data/lvls/edited/" + str(i) + ".txt"
        self.from_file_end = ""
        with open(self.lvl_file, "r") as file:
            self.from_file = file.read().split("\n")
            file.close()
        for d in self.from_file:
            self.from_file_end += d + "\n"
        self.from_file_end = self.from_file_end[:-1]
