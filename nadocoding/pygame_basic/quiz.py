from random import randint
import pygame
#############################################################################
# 기본 초기화 ( 반드시 해야 하는 것들 )
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기")

# FPS
clock = pygame.time.Clock()
#############################################################################

# 1. 사용자 게임 초기화 ( 배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 배경화면
background = pygame.image.load("C:/Users/qkrrh/Desktop/python poop/background/background.jpg")




# 캐릭터
character = pygame.image.load("C:/Users/qkrrh/Desktop/python poop/character/character.jpg")
character_size = character.get_rect().size # 70 x 70
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0

# 캐릭 이속
move_speed = 0.6


# 똥
poop = pygame.image.load("C:/Users/qkrrh/Desktop/python poop/poop/poop.jpg")
poop_size = poop.get_rect().size # 70 x 70
poop_width = poop_size[0]
poop_height = poop_size[1]
poop_x_pos = randint(0, screen_width - poop_width)
poop_y_pos = 0

# 똥 이속
poop_speed = 0.4




running = True
while running :
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            running = False 

    # 3. 게임 캐릭터 위치 정의

    ## 캐릭터
    # 키 누를때
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                to_x -= move_speed
            if event.key == pygame.K_RIGHT :
                to_x += move_speed

    # 키 땔 때
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0

    # 이동
    character_x_pos += to_x * dt # 값 보정

    # 가로 경계값
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width


    ## 똥
    poop_y_pos += poop_speed * dt # 값 보정

    if poop_y_pos > screen_height :
        poop_y_pos = 0
        poop_x_pos = randint(0, screen_width - poop_width)
        

    # 4. 충돌 처리
    # 충돌 처리를 위한 rect 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    poop_rect = poop.get_rect()
    poop_rect.left = poop_x_pos
    poop_rect.top = poop_y_pos

    # 충돌 체크 
    if character_rect.colliderect(poop_rect) :
        print ("충돌했어요")

    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos)) 
    screen.blit(poop, (poop_x_pos, poop_y_pos) )






    pygame.display.update() 

pygame.quit()
