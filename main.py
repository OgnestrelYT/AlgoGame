import pygame, sys, time, random, colorsys, math, pygame_gui
from pygame.locals import *
from cor_check import *
from utils import checkCollisions


loading = False


def main():
    global game_map
    pygame.init()
    w = 2160
    h = 1440
    DISPLAY = pygame.display.set_mode((w, h), pygame.FULLSCREEN)
    pygame.display.set_caption('Algogame')

    programIcon = pygame.image.load('data/gfx/icon.png')
    pygame.display.set_icon(programIcon)

    # get fonts
    font = pygame.font.Font('data/fonts/font.otf', 100)
    font_small = pygame.font.Font('data/fonts/font.otf', 32)
    font_20 = pygame.font.Font('data/fonts/font.otf', 20)

    # get some images
    cmd = pygame.image.load('data/gfx/cmd.png')
    retry_button = pygame.image.load('data/gfx/retry_button.png')
    start_button = pygame.image.load('data/gfx/start_button.png')
    stop_button = pygame.image.load('data/gfx/stop_button.png')
    logo = pygame.image.load('data/gfx/logo.png')
    cor_cor = pygame.image.load('data/gfx/cor_cor.png')
    cor_incor = pygame.image.load('data/gfx/cor_incor.png')
    pl = pygame.image.load('data/gfx/player.png')

    grass = pygame.image.load('data/gfx/grass.png')
    stone = pygame.image.load('data/gfx/stone.png')

    # get sounds
    flapfx = pygame.mixer.Sound("data/sfx/flap.wav")
    upgradefx = pygame.mixer.Sound("data/sfx/upgrade.wav")
    beanfx = pygame.mixer.Sound("data/sfx/bean.wav")
    deadfx = pygame.mixer.Sound("data/sfx/dead.wav")

    # colors
    WHITE = (255, 255, 255)  # constant
    clock = pygame.time.Clock()

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
                    sys.exit()

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
    aling = 200
    fromScreen = 100
    lvlSelectorScreen = True
    while lvlSelectorScreen:
        global lvl
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        mouseX, mouseY = pygame.mouse.get_pos()
        clicked = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()



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
            DISPLAY.blit(retry_button, (DISPLAY.get_width() / 2 + (aling * i - aling) - 2 * aling - retry_button.get_width() / 2, DISPLAY.get_height() / 2 - retry_button.get_height() / 2))
            # Rendering title of button
            DISPLAY.blit(Message, (DISPLAY.get_width() / 2 + (aling * i - aling - 6) - 2 * aling, DISPLAY.get_height() / 2 - Message.get_height() / 2))

            if (clicked and checkCollisions(mouseX, mouseY, 3, 3,
                                            DISPLAY.get_width() / 2 + (aling * i - aling) - 2 * aling - retry_button.get_width() / 2,
                                            DISPLAY.get_height() / 2 - retry_button.get_height() / 2,
                                            retry_button.get_width(), retry_button.get_height())):
                clicked = False
                lvlSelectorScreen = False
                print(i)
                lvl = i


        pygame.display.update()
        pygame.time.delay(10)

    game_map = []

    lvl_file = "data/lvls/" + str(lvl) + ".txt"
    with open(lvl_file) as file:
        for tip in file:
            game_map.append(tip.split())

    print(game_map)

    # Main game screen
    manager = pygame_gui.UIManager((800, 600))

    dialog_box = pygame_gui.elements.UITextEntryBox(relative_rect=pygame.Rect((-1, 81), (658, 998)),
                                                    manager=manager)
    dialog_box.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR)

    cor = Cor()
    text = ""

    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if tile == "0":
                cor.x_pl += 1
                if cor.x_pl > 13:
                    cor.y_pl += 1
                    cor.x_pl = 0
            x += 1
        y += 1


    while True:
        dt = time.time() - last_time
        dt *= 60
        time_delta = clock.tick(60) / 1000
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
            elif event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                print(event.text)
                text = str(event.text)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        manager.process_events(event)
        manager.update(time_delta)

        DISPLAY.fill((152, 251, 152))

        tile_rect = []
        y = 0
        for layer in game_map:
            x = 0
            for tile in layer:
                if tile == '1':
                    DISPLAY.blit(grass, (x * 90 + 660, y * 90))
                if tile == '2':
                    DISPLAY.blit(stone, (x * 90 + 660, y * 90))
                x += 1
            y += 1

        DISPLAY.blit(cmd, (0, 0))

        cor.synt_check(text)

        if (cor.synt_er and cor.flag_st == False):
            cor.conf = ""
            DISPLAY.blit(cor_cor, (0, 0))
        else:
            DISPLAY.blit(cor_incor, (0, 0))

        # Button start
        DISPLAY.blit(start_button, (580, 0))

        # Button stop
        DISPLAY.blit(stop_button, (500, 0))

        # Button to play function
        if (clicked and (checkCollisions(mouseX, mouseY, 3, 3, 580, 0, start_button.get_width(),
                                        start_button.get_height()))):
            clicked = False
            pygame.mixer.Sound.play(upgradefx)
            cor.x_pl = 0
            cor.y_pl = 0
            imp = text
            cor.pl(game_map)
            cor.start(imp, game_map)
            print(cor.x_pl, cor.y_pl)

        # Button to stop function
        if (clicked and checkCollisions(mouseX, mouseY, 3, 3, 500, 0, stop_button.get_width(),
                                        stop_button.get_height())):
            clicked = False
            pygame.mixer.Sound.play(upgradefx)
            cor.conf = ""
            cor.flag_st = False
            cor.x_pl = 0
            cor.y_pl = 0
            cor.pl(game_map)
            print(cor.x_pl, cor.y_pl)


        manager.draw_ui(DISPLAY)

        DISPLAY.blit(pl, (cor.x_pl * 90 + 660, cor.y_pl * 90))

        confMessage = font_small.render(cor.conf, True, (0, 0, 0))

        DISPLAY.blit(confMessage, (5, 20))

        pygame.display.update()


if __name__ == "__main__":
    loading = True
    main()