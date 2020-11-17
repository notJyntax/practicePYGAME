import pygame
import os
#################################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

#화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Pang")

#FPS
clock = pygame.time.Clock()
#################################################################################


current_path = os.path.dirname(__file__) #현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") #image폴더 위치 반환

background = pygame.image.load(os.path.join(image_path, "background.png"))

#스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] #스테이지의 높이 위에 캐릭터를 두기 위해 사용

#캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) -(character_width / 2)
character_y_pos = (screen_height - character_height - stage_height)


#이동할 좌표


#이동 속도


#적 캐릭터


#폰트 정의
game_font = pygame.font.Font(None, 40)

#총 시간
total_time = 10

#시작 시간
start_ticks = pygame.time.get_ticks()

#이벤트 루프
running = True
while running:
    dt = clock.tick(60) #게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. 게임 캐릭터 위치 정의

    
    #가로 경계값 처리

    
    #세로 경계값 처리


    # 4. 충돌 처리
    #충돌 처리



    #충돌 체크


    # 5. 화면에 그리기
    screen.blit(background, (0, 0)) #배경 그리기
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))


    #타이머 집어 넣기
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (0, 0, 0))
    screen.blit(timer, (10, 10))

    #만약 시간이 0이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임 아웃")
        running = False

    pygame.display.update() #게임 화면 다시 그리기

#pygame 종료
pygame.quit()
