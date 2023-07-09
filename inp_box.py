import pygame_widgets, pygame
from pygame_widgets.textbox import TextBox
from saver import Saver

class Input:
    def __init__(self):
        self.sav = Saver()

    def output(self, textbox):
        textbox.setText(textbox.getText())

    def edit(self, textbox, lvl):
        self.sav.save_code(textbox.getText(), lvl)

    def blit(self, DISPLAY, lvl, events):
        textbox = TextBox(DISPLAY, 1, 100, 658, 50, fontSize=40,
                          borderColour=(0, 0, 0), textColour=(0, 200, 0), radius=10, borderThickness=0)
        textbox.onSubmit = self.output(textbox)
        textbox.onTextChanged = self.edit(textbox, lvl)
        pygame_widgets.update(events)
