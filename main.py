#import kwargs as kwargs
import pygame, sys, time, random, colorsys, math, pygame_gui, pygame_widgets
from pygame_widgets.textbox import TextBox
from pygame.locals import *
from cor_check import *
from settings import *
from saver import *
from utils import checkCollisions

loading = True

pygame.init()
w = 2160
h = 1440
DISPLAY = pygame.display.set_mode((w, h), pygame.FULLSCREEN)
pygame.display.set_caption('Algogame')

programIcon = pygame.image.load('data/gfx/icon.png')
pygame.display.set_icon(programIcon)

# get fonts
font_text = pygame.font.Font('data/fonts/ofont.ru_Pixeloid Sans.ttf', 40)
font = pygame.font.Font('data/fonts/font.otf', 100)
font_small = pygame.font.Font('data/fonts/font.otf', 50)
font_20 = pygame.font.Font('data/fonts/font.otf', 20)

# get some images
cmd = pygame.image.load('data/gfx/cmd.png')
start_button = pygame.image.load('data/gfx/start_button.png')
stop_button = pygame.image.load('data/gfx/stop_button.png')
logo = pygame.image.load('data/gfx/logo.png')
cor_cor = pygame.image.load('data/gfx/cor_cor.png')
cor_incor = pygame.image.load('data/gfx/cor_incor.png')
pl = pygame.image.load('data/gfx/player.png')

# get sounds
flapfx = pygame.mixer.Sound("data/sfx/flap.wav")
upgradefx = pygame.mixer.Sound("data/sfx/upgrade.wav")
beanfx = pygame.mixer.Sound("data/sfx/bean.wav")
deadfx = pygame.mixer.Sound("data/sfx/dead.wav")

cor = Cor()
set = Settings()
sav = Saver()
gamm = GameMap()

# colors
WHITE = (255, 255, 255)  # constant
clock = pygame.time.Clock()

light_button = "data/gfx/retry_button.png"
night_button = "data/gfx/night_button.png"

set.settings_check()

# Buttons color
if set.theme:
    retry_button = pygame.image.load(night_button)
else:
    retry_button = pygame.image.load(light_button)


framerate = 60
ii = 1
strcol = 15
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

        set.settings_check()

        # Filling bg
        if set.theme:
            DISPLAY.fill((119, 136, 153))
        else:
            DISPLAY.fill((231, 205, 183))

        # Start massage
        startMessage = font_small.render("AlgoGame", True, (139, 0, 0))

        # Rendering start massage
        DISPLAY.blit(startMessage, (DISPLAY.get_width() / 2 - startMessage.get_width() / 2,
                                    DISPLAY.get_height() / 2 - startMessage.get_height() / 2))

        pygame.display.update()
        pygame.time.delay(10)


# Start screen with buttons
def title_screen():
    def blit_text(surface, text, pos, font, color=pygame.Color("black")):
        words = [word.split(" ") for word in text.splitlines()]
        space = font.size(" ")[0]
        max_width, max_height = surface.get_size()
        i = 0
        x, y = pos
        for line in words:
            for word in line:
                if i < strcol:
                    i += 1
                    word_surface = font.render(word, 0, color)
                    word_width, word_height = word_surface.get_size()
                    if x + word_width >= max_width:
                        x = pos[0]
                        y += word_height
                    surface.blit(word_surface, (x, y))
                    x += word_width + space
                    cor.flag_col = False
                else:
                    cor.flag_col = True
            x = pos[0]
            y += word_height

    settingScreen = False
    last_time = time.time()
    titleScreen = True
    pygame.mixer.Sound.play(flapfx)

    # Y of start button
    bStart = 500
    # Y of settings button
    bSettings = 600
    # Y of exit button
    bExit = 700
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

        set.settings_check()

        # Filling bg
        if set.theme:
            DISPLAY.fill((105, 105, 105))
        else:
            DISPLAY.fill((255, 218, 185))

        # Buttons color
        if set.theme:
            retry_button = pygame.image.load(night_button)
        else:
            retry_button = pygame.image.load(light_button)

        # Log on on screen
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
        DISPLAY.blit(startMessage, (DISPLAY.get_width() / 2 - startMessage.get_width() / 2, bStart - 30 +
                                    retry_button.get_height() / 2))
        # Rendering title of settings button
        DISPLAY.blit(settingsMessage, (DISPLAY.get_width() / 2 - settingsMessage.get_width() / 2, bSettings - 30 +
                                    retry_button.get_height() / 2))
        # Rendering title of exit button
        DISPLAY.blit(exitMessage, (DISPLAY.get_width() / 2 - exitMessage.get_width() / 2, bExit - 30 +
                                    retry_button.get_height() / 2))

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

        pygame.display.update()
        pygame.time.delay(10)

    # Settings screen
    bTheme = 500
    while settingScreen:
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()

        clicked = False

        # Getting mouse positions
        mouseX, mouseY = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked = True
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    title_screen()

        set.settings_check()

        # Filling bg
        if set.theme:
            DISPLAY.fill((105, 105, 105))
        else:
            DISPLAY.fill((231, 205, 183))

        # Buttons color
        if set.theme:
            retry_button = pygame.image.load(night_button)
        else:
            retry_button = pygame.image.load(light_button)

# ----------------------------------------------------------------------------------------------------------------------

        # Theme massage
        if set.theme:
            themeMessageBB = font_small.render("Switch to", True, (0, 0, 0))
            themeMessageOnB = font_small.render("light", True, (0, 0, 0))
        else:
            themeMessageBB = font_small.render("Switch to", True, (171, 145, 123))
            themeMessageOnB = font_small.render("night", True, (171, 145, 123))

        # Button theme
        DISPLAY.blit(retry_button, (DISPLAY.get_width() / 2 - retry_button.get_width() / 2,
                                    bTheme))

        # Rendering theme on button txt
        DISPLAY.blit(themeMessageOnB, (DISPLAY.get_width() / 2 - retry_button.get_width() / 2 +
                                       themeMessageOnB.get_width() / 2,
                                       bTheme - 30 +
                                       retry_button.get_height() / 2))

        # Rendering theme before button txt
        DISPLAY.blit(themeMessageBB, (DISPLAY.get_width() / 2 - retry_button.get_width() / 2 -
                                       themeMessageBB.get_width() - 5,
                                       bTheme - 30 +
                                       retry_button.get_height() / 2))

        # Button to switch theme
        if (clicked and (checkCollisions(mouseX, mouseY, 3, 3, DISPLAY.get_width() / 2 - retry_button.get_width() / 2,
                                         bTheme, retry_button.get_width(),
                                         retry_button.get_height()))):
            clicked = False
            if set.theme:
                set.edit(0, "light theme")
            else:
                set.edit(0, "night theme")
            print("switch theme")

# ----------------------------------------------------------------------------------------------------------------------


        pygame.display.update()
        pygame.time.delay(10)


    # Levels selector screen
    aling = 350
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
                    title_screen()

        set.settings_check()

        # Filling bg
        if set.theme:
            DISPLAY.fill((105, 105, 105))
        else:
            DISPLAY.fill((231, 205, 183))

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

    text = ""

    y = 0
    for layer in game_map[0:11]:
        x = 0
        for tile in layer:
            if tile == "0":
                cor.x_pl += 1
                if cor.x_pl > 13:
                    cor.y_pl += 1
                    cor.x_pl = 0
            x += 1
        y += 1

    string_no_1 = ""
    string_no_2 = ""

    try:
        for layer in game_map[12]:
            string_no_1 = str(layer)
    except:
        try:
            for layer in game_map[13]:
                string_no_2 = str(layer)
        except:
            pass

    cor.pl(game_map)
    print(game_map)

    sav.enter_code(lvl)
    print(sav.from_file_end)

    while True:
        dt = time.time() - last_time
        dt *= 60
        time_delta = clock.tick(60) / 1000
        last_time = time.time()

        # Getting mouse positions
        mouseX, mouseY = pygame.mouse.get_pos()

        clicked = False
        keys = pygame.key.get_pressed()
        events = pygame.event.get()

        sav.enter_code(lvl)
        print(sav.from_file_end)
        text = sav.from_file_end
        print(text[:-1])

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked = True
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    title_screen()
                elif event.key == K_BACKSPACE:
                    text = text[:-1]
                elif cor.flag_col == False:
                    text += event.unicode

        set.settings_check()

        # Filling bg
        if set.theme:
            DISPLAY.fill((47, 79, 79))
        else:
            DISPLAY.fill((152, 251, 152))

        sav.save_code(text, lvl)

        tile_rect = []

        DISPLAY.blit(cmd, (0, 0))

        cor.synt_check(text)

        if (cor.synt_er and cor.flag_st == False):
            cor.conf = ""
            DISPLAY.blit(cor_cor, (0, 0))
        else:
            DISPLAY.blit(cor_incor, (0, 0))

        gamm.game_map(game_map, DISPLAY)

        # Button start
        DISPLAY.blit(start_button, (580, 0))

        # Button stop
        DISPLAY.blit(stop_button, (500, 0))

        # Button to play function
        if (clicked and (checkCollisions(mouseX, mouseY, 3, 3, 580, 0, start_button.get_width(),
                                        start_button.get_height()))):
            clicked = False
            cor.bon_count = 0
            pygame.mixer.Sound.play(upgradefx)
            cor.x_pl = 0
            cor.y_pl = 0
            imp = text
            cor.pl(game_map)
            cor.start(imp, game_map, DISPLAY, pl, levelMessage, bonuseMessage)
            print(cor.x_pl, cor.y_pl)

        # Button to stop function
        if (clicked and checkCollisions(mouseX, mouseY, 3, 3, 500, 0, stop_button.get_width(),
                                        stop_button.get_height())):
            clicked = False
            cor.bon_count = 0
            pygame.mixer.Sound.play(upgradefx)
            cor.conf = ""
            cor.flag_st = False
            cor.x_pl = 0
            cor.y_pl = 0
            cor.pl(game_map)
            print(cor.x_pl, cor.y_pl)

        DISPLAY.blit(pl, (cor.x_pl * 90 + 660, cor.y_pl * 90))

        confMessage = font_small.render(cor.conf, True, (0, 0, 0))

        bonuseMessage = font_small.render(str(cor.bon_count), True, (0, 0, 0))

        levelMessage = font_small.render("Level " + str(lvl), True, (0, 0, 0))

        string1 = font_small.render(string_no_1, True, (0, 0, 0))
        string2 = font_small.render(string_no_2, True, (0, 0, 0))

        pygame.draw.rect(DISPLAY, (72, 61, 139), pygame.Rect(3, 85, 588, 740), 7, 3)

        DISPLAY.blit(bonuseMessage, (5, 1025))
        DISPLAY.blit(levelMessage, (515, 1025))
        DISPLAY.blit(confMessage, (5, 20))
        DISPLAY.blit(string1, (5, 850))
        DISPLAY.blit(string2, (10, 850))

        blit_text(DISPLAY, text, (15, 80), font_text)

        pygame.display.update()


title_screen()