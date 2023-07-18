import pygame
from utils import checkCollisions

class Buttons:
    def __init__(self):
        self.collision = False
        self.b_cl = False

    def button(self, DISPLAY, click, button, mouseX, mouseY, bx, by, bw, bh, textMessage="", color=(0, 0, 0), font=None):
        self.button_blit(DISPLAY=DISPLAY, button=button, bx=bx, by=by)
        self.button_text_blit(DISPLAY=DISPLAY, textMessage=textMessage, font=font, bx=bx, by=by, bw=bw, bh=bh, color=color)
        self.check_colis(DISPLAY=DISPLAY, mouseX=mouseX, mouseY=mouseY, bx=bx, by=by, bw=bw, bh=bh)
        self.check_click(click=click)
        self.collision = False

    def button_blit(self, DISPLAY, button, bx, by):
        DISPLAY.blit(button, (bx, by))

    def button_text_blit(self, DISPLAY, textMessage, font, bx, by, bw, bh, color):
        message = font.render(textMessage, True, color)
        DISPLAY.blit(message, ((bx + bw/2) - message.get_width()/2, (by + bh/2) - message.get_height()/2))

    def check_colis(self, DISPLAY, mouseX, mouseY, bx, by, bw, bh):
        if checkCollisions(mouseX, mouseY, 3, 3, bx, by, bw, bh):
            pygame.draw.rect(DISPLAY, (0, 0, 0), (bx, by, bx + bw, by + bh), 2)
            self.collision = True

    def check_click(self, click, lamda):
        if click and self.collision:
            pass
