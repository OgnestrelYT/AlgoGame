import pygame

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
        self.light_button = "data/gfx/light_button.png"
        self.night_button = "data/gfx/night_button.png"
        self.retry_button = pygame.image.load(self.night_button)

    def settings_check(self, DISPLAY):
        with open(self.settings_file) as file:
            a = file.read().split("\n")
            for tip in a:
                if tip == "night theme":
                    self.theme = True
                    DISPLAY.fill((105, 105, 105))
                    self.retry_button = pygame.image.load(self.night_button)
                elif tip == "light theme":
                    self.theme = False
                    DISPLAY.fill((255, 218, 185))
                    self.retry_button = pygame.image.load(self.light_button)

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