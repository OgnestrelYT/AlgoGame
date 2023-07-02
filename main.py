import pygame, sys, time, random, colorsys, math, tkinter
from pygame.math import Vector2
from pygame.locals import *
#from player import Player
from background import Background
from button import Button
#from bean import Bean
#from utils import clamp
from utils import checkCollisions


loading = False


def main():
    pygame.init()
    w = 2160
    h = 1440
    DISPLAY = pygame.display.set_mode((w, h), pygame.FULLSCREEN)
    pygame.display.set_caption('Minecraft')
#    pygame.display.set_icon(Bean().sprite)
    # get fonts
    font = pygame.font.Font('data/fonts/font.otf', 100)
    font_small = pygame.font.Font('data/fonts/font.otf', 32)
    font_20 = pygame.font.Font('data/fonts/font.otf', 20)
    # get some images
    shop = pygame.image.load('data/gfx/shop.png')
    cmd = pygame.image.load('data/gfx/cmd.png')
    shop_bg = pygame.image.load('data/gfx/shop_bg.png')
    retry_button = pygame.image.load('data/gfx/retry_button.png')
    logo = pygame.image.load('data/gfx/logo.png')
    title_bg = pygame.image.load('data/gfx/bg.png')
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
#    player = Player()
    beans = []
    buttons = []
    # adding three buttons
    for i in range(3):
        buttons.append(Button())
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
#    for bean in beans:
#        bean.position.xy = random.randrange(0, DISPLAY.get_width() - bean.sprite.get_width()), beans.index(
#            bean) * -200 - player.position.y
    # creating a list of backgrounds, with each index being an object
    bg = [Background(), Background(), Background()]
    # some variables that we need
    beanCount = 0
#    startingHeight = player.position.y
    height = 0
    health = 100
    flapForce = 3
    beanMultiplier = 5
    dead = False
    framerate = 60
    last_time = time.time()
    splashScreenTimer = 0
    settingScreen = False
    pygame.mixer.Sound.play(flapfx)


    #Loading screen
    if loading:
        while splashScreenTimer < 100:
            dt = time.time() - last_time
            dt *= 60
            last_time = time.time()

            splashScreenTimer += dt

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # Filling bg
            DISPLAY.fill((231, 205, 183))

            # Start massage
            startMessage = font_small.render("AlgoGame", True, (171, 145, 123))

            # Rendering start massage
            DISPLAY.blit(startMessage, (DISPLAY.get_width() / 2 - startMessage.get_width() / 2,
                                        DISPLAY.get_height() / 2 - startMessage.get_height() / 2))

            pygame.display.update()
            pygame.time.delay(10)


    # Start screen with buttons
    titleScreen = True
    pygame.mixer.Sound.play(flapfx)

    # Y of start button
    bStart = 500
    # Y of settings button
    bSettings = 560
    # Y of exit button
    bExit = 620

    while titleScreen:
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        mouseX, mouseY = pygame.mouse.get_pos()
        clicked = False
        keys = pygame.key.get_pressed()

        # Click checking
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked = True
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Button to play function
        if (clicked and checkCollisions(mouseX, mouseY, 3, 3, DISPLAY.get_width() / 2 - retry_button.get_width() / 2,
                                        bStart, retry_button.get_width(), retry_button.get_height())):
            clicked = False
            pygame.mixer.Sound.play(upgradefx)
            titleScreen = False

        # Button to settings function
        if (clicked and checkCollisions(mouseX, mouseY, 3, 3,
                                        DISPLAY.get_width() / 2 - retry_button.get_width() / 2,
                                        bSettings, retry_button.get_width(), retry_button.get_height())):
            clicked = False
            settingScreen = True
            titleScreen = False

        # Button to exit function
        if (clicked and checkCollisions(mouseX, mouseY, 3, 3, DISPLAY.get_width() / 2 - retry_button.get_width() / 2,
                                        bExit, retry_button.get_width(), retry_button.get_height())):
            clicked = False
            sys.exit()

        # Filling bg
        DISPLAY.fill(WHITE)
        DISPLAY.fill((255, 218, 185))

        # Logon on screen
        DISPLAY.blit(logo, (DISPLAY.get_width() / 2 - logo.get_width() / 2,
                            DISPLAY.get_height() / 2 - 200 - logo.get_height() / 2 + math.sin(time.time() * 5) * 5 - 25))

        # Button start
        DISPLAY.blit(retry_button, (DISPLAY.get_width() / 2 - retry_button.get_width() / 2, bStart))
        # Button settings
        DISPLAY.blit(retry_button, (DISPLAY.get_width() / 2 - retry_button.get_width() / 2, bSettings))
        # Button exit
        DISPLAY.blit(retry_button, (DISPLAY.get_width() / 2 - retry_button.get_width() / 2, bExit))

        # Title of start button
        startMessage = font_small.render("START", True, (0, 0, 0))
        # Title of settings button
        settingsMessage = font_small.render("SETTINGS", True, (0, 0, 0))
        # Title of exit button
        exitMessage = font_small.render("EXIT", True, (0, 0, 0))

        # Rendering title of start button
        DISPLAY.blit(startMessage, (DISPLAY.get_width() / 2 - startMessage.get_width() / 2, bStart + 4))
        # Rendering title of settings button
        DISPLAY.blit(settingsMessage, (DISPLAY.get_width() / 2 - settingsMessage.get_width() / 2, bSettings + 4))
        # Rendering title of exit button
        DISPLAY.blit(exitMessage, (DISPLAY.get_width() / 2 - exitMessage.get_width() / 2, bExit + 4))

        pygame.display.update()
        pygame.time.delay(10)

    # Settings screen
    while settingScreen:
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main()

        # Filling bg
        DISPLAY.fill((231, 205, 183))

        # Start massage
        startMessage = font_small.render("SOON...", True, (171, 145, 123))

        # Rendering start massage
        DISPLAY.blit(startMessage, (DISPLAY.get_width() / 2 - startMessage.get_width() / 2,
                                    DISPLAY.get_height() / 2 - startMessage.get_height() / 2))

        pygame.display.update()
        pygame.time.delay(10)


    # Levels selector screen
    Y = 100
    lvlSelectorScreen = True
    while lvlSelectorScreen:
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pass



        # Filling bg
        DISPLAY.fill((231, 205, 183))

        # Start massage
        startMessage = font_small.render("SOON...", True, (171, 145, 123))

        # Rendering start massage
        DISPLAY.blit(startMessage, (DISPLAY.get_width() / 2 - startMessage.get_width() / 2,
                                    DISPLAY.get_height() / 2 - startMessage.get_height() / 2))

        for i in range(1, 6):
            # Title of button
            Message = font_small.render(str(i), True, (0, 0, 0))
            # Button
            DISPLAY.blit(retry_button, (Y * i, DISPLAY.get_height() / 2 - retry_button.get_height()))
            # Rendering title of button
            DISPLAY.blit(Message, (Y * i + 4, DISPLAY.get_height() / 2 - Message.get_height() / 2))


        pygame.display.update()
        pygame.time.delay(10)


    # Main game screen
    bRetry = (100, DISPLAY.get_height())
    while True:
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        # Getting mouse positions
        mouseX, mouseY = pygame.mouse.get_pos()

        clicked = False
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked = True
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main()


        DISPLAY.fill((152, 251, 152))
        DISPLAY.blit(cmd, (0, 0))

        if dead:
            DISPLAY.blit(retry_button, bRetry)
            deathMessage = font_small.render("RETRY", True, (0, 0, 0))
            DISPLAY.blit(deathMessage, (bRetry[0], bRetry[1] + 4))

        if health <= 0 and not dead:
            dead = True
            pygame.mixer.Sound.play(deadfx)

        if dead and clicked and checkCollisions(mouseX, mouseY, 3, 3, 4, 4, retry_button.get_width(),
                                                retry_button.get_height()):
#            player.position.xy = 295, 100
            starsCount = 0
            height = 0
            flapForce = 3
            beanMultiplier = 5
            buttons = []

            for i in range(3): buttons.append(Button())
            buttons[0].typeIndicatorSprite = pygame.image.load('data/gfx/flap_indicator.png')
            buttons[0].price = 5
            buttons[1].typeIndicatorSprite = pygame.image.load('data/gfx/speed_indicator.png')
            buttons[1].price = 5
            buttons[2].typeIndicatorSprite = pygame.image.load('data/gfx/beanup_indicator.png')
            buttons[2].price = 30
            pygame.mixer.Sound.play(upgradefx)
            dead = False

        pygame.display.update()
        pygame.time.delay(10)


if __name__ == "__main__":
    loading = True
    main()
