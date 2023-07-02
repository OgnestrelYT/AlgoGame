import pygame, random, sys, time, random, colorsys, math
from utils import *


def main():
    pygame.init()
    # set the display
    DISPLAY = pygame.display.set_mode((640, 480), 0, 32)
    pygame.display.set_caption('Flappuccino')
    #pygame.display.set_icon(Bean().sprite)
    # get fonts

    font = pygame.font.Font('data/fonts/font.otf', 100)
    font_small = pygame.font.Font('data/fonts/font.otf', 32)
    font_20 = pygame.font.Font('data/fonts/font.otf', 20)
    # get some images
    shop = pygame.image.load('data/gfx/shop.png')
    shop_bg = pygame.image.load('data/gfx/shop_bg.png')
    retry_button = pygame.image.load('data/gfx/retry_button.png')
    logo = pygame.image.load('data/gfx/logo.png')
    title_bg = pygame.image.load('data/gfx/bg.png')
    title_bg.fill((255, 30.599999999999998, 0.0), special_flags=pygame.BLEND_ADD)
    shadow = pygame.image.load('data/gfx/shadow.png')
    # get sounds
    flapfx = pygame.mixer.Sound("data/sfx/flap.wav")
    upgradefx = pygame.mixer.Sound("data/sfx/upgrade.wav")
    beanfx = pygame.mixer.Sound("data/sfx/bean.wav")
    deadfx = pygame.mixer.Sound("data/sfx/dead.wav")
    # colors
    WHITE = (255, 255, 255)  # constant
    # variables
    rotOffset = -5
    # creating a new object player
    #player = Player()
    beans = []
    buttons = []
    # adding three buttons
    """for i in range(3): buttons.append(Button())
    # now simply loading images based off of indexes in the list
    buttons[0].typeIndicatorSprite = pygame.image.load('data/gfx/flap_indicator.png')
    buttons[0].price = 5
    buttons[1].typeIndicatorSprite = pygame.image.load('data/gfx/speed_indicator.png')
    buttons[1].price = 5
    buttons[2].typeIndicatorSprite = pygame.image.load('data/gfx/beanup_indicator.png')
    buttons[2].price = 30
    
    # getting 5 beans
    #    for i in range(5): beans.append(Bean())
    # now looping through the beans list
    for bean in beans:
        bean.position.xy = random.randrange(0, DISPLAY.get_width() - bean.sprite.get_width()), beans.index(
            bean) * -200 - player.position.y
            """

    print(1)
    # creating a list of backgrounds, with each index being an object
    #    """bg = [Background(), Background(), Background()]"""
    # some variables that we need
    beanCount = 0
    #    startingHeight = player.position.y
    height = 0
    health = 100
    flapForce = 3
    beanMultiplier = 5
    dead = False
    # we need the framerate and then the time
    framerate = 60
    last_time = time.time()
    splashScreenTimer = 0
    # splash screen
    # playing a sound
    pygame.mixer.Sound.play(flapfx)
    while splashScreenTimer < 100:
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()

        splashScreenTimer += dt

        for event in pygame.event.get():
            # if the user clicks the button
            if event.type == event.QUIT:
                pygame.quit()
                sys.exit()

        DISPLAY.fill((231, 205, 183))
        # fill the start message on the top of the game
        startMessage = font_small.render("POLYMARS", True, (171, 145, 123))
        DISPLAY.blit(startMessage, (DISPLAY.get_width() / 2 - startMessage.get_width() / 2,
                                    DISPLAY.get_height() / 2 - startMessage.get_height() / 2))

        # update display
        pygame.display.update()
        # wait for 10 seconds
        pygame.time.delay(10)

    titleScreen = True
    # title screen
    pygame.mixer.Sound.play(flapfx)
    while titleScreen:
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        # get the position of the mouse
        mouseX, mouseY = pygame.mouse.get_pos()
        # getting the keys pressed
        clicked = False
        keys = pygame.key.get_pressed()
        # checking events
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked = True
            # if the player quits
            if event.type == event.QUIT:
                pygame.quit()
                sys.exit()
        # so the user clicked, and by any change the mouse's position was on the buttons
        if (clicked and checkCollisions(mouseX, mouseY, 3, 3, DISPLAY.get_width() / 2 - retry_button.get_width() / 2,
                                        288, retry_button.get_width(), retry_button.get_height())):
            clicked = False
            pygame.mixer.Sound.play(upgradefx)
            titleScreen = False

        DISPLAY.fill(WHITE)
        DISPLAY.blit(title_bg, (0, 0))
        DISPLAY.blit(shadow, (0, 0))
        DISPLAY.blit(logo, (DISPLAY.get_width() / 2 - logo.get_width() / 2,
                            DISPLAY.get_height() / 2 - logo.get_height() / 2 + math.sin(time.time() * 5) * 5 - 25))
        DISPLAY.blit(retry_button, (DISPLAY.get_width() / 2 - retry_button.get_width() / 2, 288))
        startMessage = font_small.render("START", True, (0, 0, 0))
        DISPLAY.blit(startMessage, (DISPLAY.get_width() / 2 - startMessage.get_width() / 2, 292))

        pygame.display.update()
        pygame.time.delay(10)

if __name__ == "__main__":
    main()