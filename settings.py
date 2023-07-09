
class Settings:
    def __init__(self):
        self.settings_file = "data/settings/settings.txt"
        self.settings_list = []
        self.edited_old = []
        self.ind = 0
        self.print = "1"
        self.edited_compl = ""
        self.theme = True
        self.volume = True

    def settings_check(self):
        with open(self.settings_file) as file:
            a = file.read().split("\n")
            for tip in a:
                if tip == "night theme":
                    self.theme = True
                elif tip == "light theme":
                    self.theme = False

                elif tip == "volume on":
                    self.volume = True
                elif tip == "volume off":
                    self.volume = False

                """
                elif tip == "volume on":
                    self.volume = True
                elif tip == "volume off":
                    self.volume = False
                """

    def edit(self, ind, sw_txt):
        self.edited_compl = ""
        with open(self.settings_file, "r") as file:
            self.edited_old = file.read().split("\n")
            file.close()
        self.edited_old.insert(ind, sw_txt)
        self.edited_old.pop(ind + 1)
        for i in self.edited_old:
            self.edited_compl += i + "\n"
        self.edited_compl = self.edited_compl[:-1]
        with open(self.settings_file, "w") as file:
            file.write(str(self.edited_compl))
            file.close()