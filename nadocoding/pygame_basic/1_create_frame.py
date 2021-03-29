import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 400
screen_height = 640
screen = pygame.display.set_mode((screen_height, screen_width))

# 화면 타이틀 설정
pygame.display.set_caption("Nado game")

# 이벤트 루프
running = True # 게임이 진행중인가?
while running :
    for event in pygame.event.get() : # 어떤 이벤트 발생함?
        if event.type == pygame.QUIT : # 창이 닫힘?
            running = False # 게임 종료


# pygame 종료
pygame.quit()
