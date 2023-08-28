import pygame
from utils import checkCollisions

class Buttons:
    def __init__(self):
        self.collision = False
        self.b_cl = False

    def button(self, DISPLAY, click, button, mouseX, mouseY, bx, by, bw, bh, textMessage="", color=(0, 0, 0), font=None):
        self.button_blit(DISPLAY=DISPLAY, button=button, bx=bx, by=by, bw=bw, bh=bh)
        self.button_text_blit(DISPLAY=DISPLAY, textMessage=textMessage, font=font, bx=bx, by=by, bw=bw, bh=bh, color=color)
        self.check_colis(DISPLAY=DISPLAY, mouseX=mouseX, mouseY=mouseY, bx=bx, by=by, bw=bw, bh=bh)
        self.click_blit(DISPLAY=DISPLAY, click=click, button=button)

    def button_blit(self, DISPLAY, button, bx, by, bw, bh):
        new_button = pygame.transform.scale(button, (bw, bh))
        DISPLAY.blit(new_button, (bx, by))

    def button_text_blit(self, DISPLAY, textMessage, font, bx, by, bw, bh, color):
        message = font.render(textMessage, True, color)
        DISPLAY.blit(message, ((bx + bw/2) - message.get_width()/2, (by + bh/2) - message.get_height()/2))

    def check_colis(self, DISPLAY, mouseX, mouseY, bx, by, bw, bh):
        if checkCollisions(mouseX, mouseY, 3, 3, bx, by, bw, bh):
            pygame.draw.rect(DISPLAY, (0, 0, 0), (bx, by, bw, bh), 3)
            self.collision = True

    def click_blit(self, DISPLAY, click, button):
        if click and self.collision:
            pass

    def check_click(self, click):
        if click and self.collision:
            self.collision = False
            return True
        else:
            self.collision = False
            return False
