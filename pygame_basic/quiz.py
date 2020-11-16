# Quiz) 하늘에서 떨어지는 파이썬 피하기 게임

# [게임 조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능 ㅇ
# 2. 파이썬은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 파이썬을 피하면 다음 파이썬이 다시 떨어짐
# 4. 캐릭터가 파이썬과 충돌하면 게임 종료
# 5. FPS는 30으로 고정 ㅇ


# [게임 이미지]
# 1. 배경 : 640 * 480 (세로 가로) 
# 2. 캐릭터 : 70 * 70
# 3. 똥 : 70 * 70
import random
import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Vengeance of AI")

clock = pygame.time.Clock()

game_font =  pygame.font.Font(None, 50)
msg = game_font.render('WASTED', True, (255, 0, 0))


background = pygame.image.load("C:/Users/bank/Desktop/dev/py_game/background2.png")

character = pygame.image.load("C:/Users/bank/Desktop/dev/py_game/character2.png")
character_size = character.get_rect().size #이미지 크기를 구해옴
character_width = character_size[0] #캐릭터의 가로크기
character_height = character_size[1] #캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height

enemy = pygame.image.load("C:/Users/bank/Desktop/dev/py_game/enemy2.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 10

to_x = 0
character_speed = 0.6

running = True
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    enemy_y_pos += enemy_speed
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False


    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(msg, (0, 50))
    

    
    pygame.display.update()
pygame.time.delay(2000) #2초 정도 대기

pygame.quit()