import time
import math
import pygame.key
from pygame.locals import *
from game_map import GameMap
from cor_check import *
from settings import *
from saver import *
from buttons import *
from utils import checkCollisions

loading = True

pygame.init()
w = 2160
h = 1440
DISPLAY = pygame.display.set_mode((w, h), pygame.FULLSCREEN)
pygame.display.set_caption('Algogame')

programIcon = pygame.image.load('data/gfx/icon.png')
pygame.display.set_icon(programIcon)

# Get fonts
font_text = pygame.font.Font('data/fonts/ofont.ru_Pixeloid Sans.ttf', 40)
font = pygame.font.Font('data/fonts/font.otf', 100)
font_small = pygame.font.Font('data/fonts/font.otf', 50)
font_20 = pygame.font.Font('data/fonts/font.otf', 20)
font_rus = pygame.font.Font("data/fonts/rusf.ttf", 40)
font_rus_small = pygame.font.Font("data/fonts/rusf.ttf", 35)
font_ton = pygame.font.Font('data/fonts/ton.ttf', 35)

# Get some images
cmd = pygame.image.load('data/gfx/cmd.png')
start_button = pygame.image.load('data/gfx/start_button.png')
stop_button = pygame.image.load('data/gfx/stop_button.png')
logo = pygame.image.load('data/gfx/logo.png')
cor_cor = pygame.image.load('data/gfx/cor_cor.png')
cor_incor = pygame.image.load('data/gfx/cor_incor.png')
pl = pygame.image.load('data/gfx/player.png')

cor = Cor()
set = Settings()
sav = Saver()
gamm = GameMap()
but = Buttons()

# Colors
WHITE = (255, 255, 255)  # constant
clock = pygame.time.Clock()

set.settings_check(DISPLAY=DISPLAY)

framerate = 60
ii = 1
strcol = 15
last_time = time.time()
splashScreenTimer = 0

# ----------------------------------------------------------------------------------------------------------------------

# Loading screen
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

        set.settings_check(DISPLAY=DISPLAY)

        # Start massage
        startMessage = font_small.render("AlgoGame", True, (139, 0, 0))

        # Rendering start massage
        DISPLAY.blit(startMessage, (DISPLAY.get_width() / 2 - startMessage.get_width() / 2,
                                    DISPLAY.get_height() / 2 - startMessage.get_height() / 2))

        pygame.display.update()
        pygame.time.delay(10)

# ----------------------------------------------------------------------------------------------------------------------

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
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]
                    y += word_height
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]
            y += word_height

    last_time = time.time()

    settingScreen = False
    selectorOfLvls = False
    selectorOfSelection = False
    lvlSelectorScreenNotMy = False

    titleScreen = True

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

        set.settings_check(DISPLAY=DISPLAY)

        # Log on on screen
        DISPLAY.blit(logo, (DISPLAY.get_width() / 2 - logo.get_width() / 2,
                            DISPLAY.get_height() / 2 - 200 - logo.get_height() / 2 +
                            math.sin(time.time() * 5) * 5 - 25))

        # Button start
        but.button(DISPLAY=DISPLAY, click=clicked, button=set.retry_button, mouseX=mouseX, mouseY=mouseY,
                   bx=DISPLAY.get_width() / 2 - 320 / 2, by=500,
                   bw=320, bh=90, textMessage="НАЧАТЬ", font=font_rus)
        if but.check_click(click=clicked):
            titleScreen = False
            selectorOfSelection = True

        # Button settings
        but.button(DISPLAY=DISPLAY, click=clicked, button=set.retry_button, mouseX=mouseX, mouseY=mouseY,
                   bx=DISPLAY.get_width() / 2 - 320 / 2, by=600,
                   bw=320, bh=90, textMessage="НАСТРОЙКИ", font=font_rus)
        if but.check_click(click=clicked):
            titleScreen = False
            settingScreen = True

        # Button exit
        but.button(DISPLAY=DISPLAY, click=clicked, button=set.retry_button, mouseX=mouseX, mouseY=mouseY,
                   bx=DISPLAY.get_width() / 2 - 320 / 2, by=700,
                   bw=320, bh=90, textMessage="ВЫХОД", font=font_rus)
        if but.check_click(click=clicked):
            sys.exit()

        clicked = False

        pygame.display.update()
        pygame.time.delay(10)

# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
    # Selector of my and user`s lvls
    while selectorOfSelection:
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        mouseX, mouseY = pygame.mouse.get_pos()
        clicked = False

        # Click checking
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked = True
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    title_screen()

        set.settings_check(DISPLAY=DISPLAY)

        # Button user lvls
        but.button(DISPLAY=DISPLAY, click=clicked, button=set.retry_button, mouseX=mouseX, mouseY=mouseY,
                   bx=DISPLAY.get_width() / 2 - 620 / 2, by=500,
                   bw=620, bh=90, textMessage="ПОЛЬЗОВАТЕЛЬСКИЕ УРОВНИ", font=font_rus)
        if but.check_click(click=clicked):
            lvlSelectorScreenNotMy = True
            selectorOfSelection = False

        # Button my lvls
        but.button(DISPLAY=DISPLAY, click=clicked, button=set.retry_button, mouseX=mouseX, mouseY=mouseY,
                   bx=DISPLAY.get_width() / 2 - 620 / 2, by=600,
                   bw=620, bh=90, textMessage="ПРЕДУСТАНОВЛЕННЫЕ УРОВНИ", font=font_rus)
        if but.check_click(click=clicked):
            selectorOfLvls = True
            selectorOfSelection = False

        clicked = False

        pygame.display.update()
        pygame.time.delay(10)

# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
    # Selector of user levels
    while selectorOfLvls:
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
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    title_screen()

        set.settings_check(DISPLAY=DISPLAY)

        # Button exit
        but.button(DISPLAY=DISPLAY, click=clicked, button=set.retry_button, mouseX=mouseX, mouseY=mouseY,
                   bx=DISPLAY.get_width() / 2 - set.retry_button.get_width() / 2, by=635,
                   bw=320, bh=90, textMessage="ВЫХОД", font=font_rus)
        if but.check_click(click=clicked):
            sys.exit()

        clicked = False

        pygame.display.update()
        pygame.time.delay(10)

# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------

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
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    title_screen()

        set.settings_check(DISPLAY=DISPLAY)

        # Theme massage
        if set.theme:
            themeMessageOnB = "Поменять на светлую"
        else:
            themeMessageOnB = "Поменять на тёмную"

        # Button theme
        but.button(DISPLAY=DISPLAY, click=clicked, button=set.retry_button, mouseX=mouseX, mouseY=mouseY,
                   bx=DISPLAY.get_width() / 2 - set.retry_button.get_width() / 2, by=500,
                   bw=320, bh=90, textMessage=themeMessageOnB, font=font_rus_small)
        if but.check_click(click=clicked):
            if set.theme:
                set.edit(0, "light theme")
            else:
                set.edit(0, "night theme")

        clicked = False

        pygame.display.update()
        pygame.time.delay(10)

# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------

        # Levels selector screen (Not my)
        aling = 350
        fromScreen = 100
        while lvlSelectorScreenNotMy:
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
                Message = font_small.render(str(i) + " уровень", True, (0, 0, 0))
                # Button
                DISPLAY.blit(retry_button, (
                DISPLAY.get_width() / 2 + (aling * i - aling) - 2 * aling - retry_button.get_width() / 2,
                DISPLAY.get_height() / 2 - retry_button.get_height() / 2))
                # Rendering title of button
                DISPLAY.blit(Message, (DISPLAY.get_width() / 2 + (aling * i - aling - 6) - 2 * aling,
                                       DISPLAY.get_height() / 2 - Message.get_height() / 2))

                if (clicked and checkCollisions(mouseX, mouseY, 3, 3,
                                                DISPLAY.get_width() / 2 + (
                                                        aling * i - aling) - 2 * aling - retry_button.get_width() / 2,
                                                DISPLAY.get_height() / 2 - retry_button.get_height() / 2,
                                                retry_button.get_width(), retry_button.get_height())):
                    clicked = False
                    lvlSelectorScreen = False
                    print(i)
                    lvl = i

            pygame.display.update()
            pygame.time.delay(10)

# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------

    # Levels selector screen (My)
    aling = 350
    fromScreen = 100
    lvlSelectorScreenMy = False
    while lvlSelectorScreenMy:
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

# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------

    # Map loader
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

    print(game_map[12:13])

    try:
        for layer in game_map[12]:
            string_no_1 += str(layer)
            string_no_1 += " "
    except:
            pass

    try:
        for layer in game_map[13]:
            string_no_2 += str(layer)
            string_no_2 += " "
    except:
            pass

    cor.pl(game_map)
    print(game_map)

    sav.enter_code(lvl)
    print(sav.from_file_end)

    BSPR = False
    i = 0

# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------

    # Game screen
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
        text = sav.from_file_end

        st = []
        leng = False
        try:
            st = text.split("\n")
            for fgh in st:
                if len(fgh) < 25:
                    leng = True
                else:
                    leng = False
                    break
        except:
            pass

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked = True
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    cor.x_pl = 0
                    cor.y_pl = 0
                    title_screen()
                elif event.key == K_BACKSPACE:
                    text = text[:-2]
                    text += "|"
                elif len(st) < 16:
                    if leng:
                        text = text[:-1]
                        text += event.unicode
                        text += "|"
                else:
                    text = text[:-1]
                    text += "|"

#        i += 1
#        if i == 6:
#            i = 0
#            if pygame.key.get_pressed()[K_BACKSPACE]:
#                text = text[:-2]
#                text += "|"

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
            game_map = []
            lvl_file = "data/lvls/" + str(lvl) + ".txt"
            with open(lvl_file) as file:
                for tip in file:
                    game_map.append(tip.split())
            clicked = False
            cor.bon_count = 0
            cor.x_pl = 0
            cor.y_pl = 0
            imp = text
            cor.pl(game_map)
            cor.start(imp, game_map, DISPLAY, pl, levelMessage, bonuseMessage)
            print(cor.x_pl, cor.y_pl)

        # Button to stop function
        if (clicked and checkCollisions(mouseX, mouseY, 3, 3, 500, 0, stop_button.get_width(),
                                        stop_button.get_height())):
            game_map = []
            lvl_file = "data/lvls/" + str(lvl) + ".txt"
            with open(lvl_file) as file:
                for tip in file:
                    game_map.append(tip.split())
            clicked = False
            cor.flag_finish = False
            cor.bon_count = 0
            cor.conf = ""
            cor.flag_st = False
            cor.x_pl = 0
            cor.y_pl = 0
            cor.pl(game_map)
            print(cor.x_pl, cor.y_pl)

        if cor.direction == "вниз":
            pl_r = pygame.transform.rotate(pl, -90)
        elif cor.direction == "вверх":
            pl_r = pygame.transform.rotate(pl, +90)
        elif cor.direction == "влево":
            pl_r = pygame.transform.flip(pl, True, False)
        elif cor.direction == "вправо":
            pl_r = pygame.transform.rotate(pl, 0)

        DISPLAY.blit(pl_r, (cor.x_pl * 90 + 660, cor.y_pl * 90))

        confMessage = font_rus.render(cor.conf, True, (0, 0, 0))

        bonuseMessage = font_small.render(str(cor.bon_count), True, (0, 0, 0))

        levelMessage = font_small.render("Level " + str(lvl), True, (0, 0, 0))

        string1 = font_rus.render(string_no_1, True, (0, 0, 0))
        string2 = font_rus.render(string_no_2, True, (0, 0, 0))

        space = font_ton.render("Дано только 15 строчек для кода!", True, (0, 0, 0))

        pygame.draw.rect(DISPLAY, (178, 34, 34), pygame.Rect(3, 820, 640, 55), border_radius=3)

        pygame.draw.rect(DISPLAY, (72, 61, 139), pygame.Rect(3, 85, 640, 790), 7, 3)

        DISPLAY.blit(bonuseMessage, (5, 1025))
        DISPLAY.blit(levelMessage, (515, 1025))
        DISPLAY.blit(confMessage, (5, 20))

        DISPLAY.blit(string1, (5, 880))
        DISPLAY.blit(string2, (5, 920))

        DISPLAY.blit(space, (40, 820))

        blit_text(DISPLAY, text, (15, 80), font_text)

        pygame.display.update()

if __name__ == "__main__":
    title_screen()