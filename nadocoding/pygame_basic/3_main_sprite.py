import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado game")

# 배경이미지 불러오기 # 탈출문자 때문에 \\혹은 /로 사용
background = pygame.image.load("C:/Users/qkrrh/Desktop/background.png")

## 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/qkrrh/Desktop/character.png")
character_size = character.get_rect().size ## 이미지의 크기를 구해옴
character_width = character_size[0] ## 캐릭터의 가로 크기
character_height = character_size[1] ## 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) ## 화면 가로의 절반 크기에 해당하는 곳
character_y_pos = screen_height - character_height ## 화면 크기 가장 아래


# 이벤트 루프
running = True # 게임이 진행중인가?
while running :
    for event in pygame.event.get() : # 어떤 이벤트 발생함?
        if event.type == pygame.QUIT : # 창이 닫힘?
            running = False # 게임 종료
    
    # screen.fill((0, 0, 255)) # RGB 값으로 설정
    screen.blit(background, (0,0)) # 배경그리기

    screen.blit(character, (character_x_pos, character_y_pos)) ## 캐릭터 그리기

    pygame.display.update() # 게임화면을 다시 그리기!

# pygame 종료
pygame.quit()
