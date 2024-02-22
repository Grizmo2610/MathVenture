import pygame
from random import randint
from Asset import Player

pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running  = True

right_bound = screen_width - 40
bottom_bound = screen_height - 40

# paths
block_path = "assets/sunny-land-files/Sunny-land-assets-files/PNG/environment/props/block-big.png"

background = pygame.image.load("assets/sunny-land-files/Sunny-land-assets-files/PNG/environment/layers/back.png")
block = pygame.image.load(block_path)


test_map = [[0] * 40 for i in range(22)]

for i in range(22):
    for j in range(40):
        if randint(1, 100) == 6:
            test_map[i][j] = 1

dt = 0
distance = 300

origin = pygame.image.load("./assets/sunny-land-files/Sunny-land-assets-files/PNG/sprites/player/idle/player-idle-3.png")
player_left = origin
player_right = pygame.transform.flip(player_left, True, False)
player_image = player_right
player = Player(screen.get_width() / 2, screen.get_height() / 2, dt, distance)

# Transform asset
background = pygame.transform.scale(background, (screen_width, screen_height))



def draw_background(map_background: list[list[int]]):
    screen.blit(background, (0,0))
    for i in range(22):
        for j in range(40):
            if (map_background[i][i] == 1):
                screen.blit(block, (i * 32, j * 32))

while running:
    # Quit game event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Drawing backgroud
    draw_background(test_map)

    # Player start position
    screen.blit(player_image, player.get_pos())

    # if press Key
    keys = pygame.key.get_pressed()

    # Move right - left
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        if (player.y - distance * dt >= 0):
            player.y -= distance * dt
        else:
            player.y = 0
    if keys[pygame.K_s] or  keys[pygame.K_DOWN]:
        if player.y + distance * dt > bottom_bound:
            player.y = bottom_bound
        else:
            player.y += distance * dt
            
    # Move Up - down
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if (player.x - distance * dt < 0):
            player.x = 0
        else:
            player.x -= distance * dt
        player_image = player_right
    if keys[pygame.K_d] or  keys[pygame.K_RIGHT]:
        if player.x + distance * dt > right_bound:
            player.x = right_bound
        else:
            player.x += distance * dt
        player_image = player_left

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    player.dt = clock.tick(60) / 1000
pygame.quit()