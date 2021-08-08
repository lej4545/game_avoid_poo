import pygame
import random
import math

def start_game():
    # 전연변수 설정: 게임 스크린 사이즈 및 초기 설정
    pygame.init()
    background = pygame.image.load("background.jpg")
    screen_width, screen_height = background.get_rect().size
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("똥피하기")

    # 폰트 및 색상 정의
    game_font = pygame.font.Font(None, 40) # 폰트, 크기
    large_font = pygame.font.SysFont(None, 80)
    small_font = pygame.font.Font(None, 32)
    large_font_size = 80
    small_font_size = 30
    RED = (250, 0, 0)

    character = pygame.image.load("character.png")
    character_size = character.get_rect().size
    character_width = character_size[0]
    character_height = character_size[1]
    character_xpos = screen_width / 2 - character_width / 2
    character_ypos = screen_height - character_height

    # 똥의 좌표값 설정
    poo_ylist = []
    poo = []
    for i in range(0, 10):
        poo.append(pygame.image.load("ddong.png"))
    poo_size = poo[0].get_rect().size
    # print(poo_size)
    poo_width = poo_size[0]
    poo_height = poo_size[1]
    poo_xpos = random.randrange(0, screen_width - poo_width)
    poo_ypos = 0

    mouse_xpos = 0
    mouse_ypos = 0
    x_touch = False
    y_touch = False

    poo_list = []

    # 똥 내려오는 초기 좌표 설정, 똥은 최대 10개로 설정
    while True:
        randomNumber = random.randrange(0, screen_width - poo_width)
        if poo_list.count(randomNumber) == 0:
            temp_dict = {}
            temp_dict["poo"] = pygame.image.load("ddong.png")
            temp_dict["x"] = randomNumber
            temp_dict["y"] = 0
            temp_dict["speed"] = random.uniform(0.7, 1.3)
            poo_list.append(temp_dict)
        if len(poo_list) == 10:
            break

    game_over = False

    # 똥이 내려올 때 위치와 마우스 위치(캐릭터)의 좌표 설정
    # 똥의 좌표들이 캐릭터의 좌표 안에 들어오면 게임이 종료되게끔 설정.
    # 다시 말해, 똥과 캐릭터가 겹치지 않을 때까지 게임 실행. 겹치면 게임 종료

    while True:
        timer = math.floor(pygame.time.get_ticks()/1000)
        score = math.floor(timer)
        for poo in poo_list:
            poo["y"] += poo["speed"]
            if poo["y"] + poo_height >= screen_height:
                poo["x"] = random.randrange(0, screen_width - poo_width)
                poo["y"] = 0
                poo["speed"] = random.uniform(0.7, 1.3)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    mouse_xpos = event.__dict__["pos"][0]
                    mouse_ypos = event.__dict__["pos"][1]
                    character_xpos = mouse_xpos - character_width / 2
                    character_ypos = mouse_ypos - character_height / 2
            if character_xpos <= poo["x"] <= character_xpos + character_width:
                x_touch = True

            if character_xpos <= poo["x"] + poo_width <= character_xpos + character_width:
                x_touch = True

            if character_ypos <= poo["y"] <= character_ypos + character_height:
                y_touch = True

            if character_ypos <= poo["y"] + poo_height <= character_ypos + character_height:
                y_touch = True

            if x_touch is True and y_touch is True:
                game_over = True
            x_touch = False
            y_touch = False


        if game_over is True:
            game_over_image = large_font.render('Game Over', True, RED)
            score_image = game_font.render("Score: " + str(score), True, RED)
            set_restart_image = game_font.render('Press ENTER : RESTART', True, RED)
            set_exit_image = game_font.render('Click [X] : EXIT', True, RED)
            screen.blit(game_over_image, (screen_width // 2 - game_over_image.get_width() // 2, screen_height // 2 - 100))
            screen.blit(score_image, (screen_width // 2 - score_image.get_width() // 2 , screen_height // 2 - score_image.get_height() // 2 - 20))
            screen.blit(set_restart_image,
                        (screen_width // 2 - game_over_image.get_width() // 2 , screen_height // 2 - game_over_image.get_height() // 2 +  large_font_size))
            screen.blit(set_exit_image,
                        (screen_width // 2 - game_over_image.get_width() // 2 + 68,screen_height // 2 - game_over_image.get_height() // 2 +  large_font_size + 40))
            pygame.display.update()

            # 게임 종료 후 종료 or 재시작 설정
            input_button = ""
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        input_button = "QUIT"
                    elif event.type == pygame.KEYUP:
                        input_button = "RESTART"
                if input_button != "":
                    break
            return input_button



        str_score = game_font.render("Score: " + str(score), True, (200, 200, 200))
        screen.blit(background, (0, 0))
        screen.blit(character, (character_xpos, character_ypos))
        screen.blit(character, (character_xpos, character_ypos))
        screen.blit(str_score, (10, 30))
        for poo in poo_list:
            screen.blit(poo["poo"], (poo["x"], poo["y"]))
        pygame.display.update()



while True:
    input_button = start_game()
    if input_button == "QUIT":
        break
    elif input_button == "RESTART":
        pygame.quit()
        continue
