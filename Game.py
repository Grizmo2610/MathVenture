import pygame
from Asset import Map
from random import randint

pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running  = True

right_bound = screen_width - 40
bottom_bound = screen_height - 40
dt = 0

# paths
block_path = "assets/sunny-land-files/Sunny-land-assets-files/PNG/environment/props/block-big.png"

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
background = pygame.image.load("assets/sunny-land-files/Sunny-land-assets-files/PNG/environment/layers/back.png")
block = pygame.image.load(block_path)


test = [[0] * 40 for i in range(22)]

for i in range(22):
    for j in range(40):
        if randint(1, 100) == 6:
            test[i][j] = 1

map_1 = Map(test)



origin = player_left = pygame.image.load("./assets/sunny-land-files/Sunny-land-assets-files/PNG/sprites/player/idle/player-idle-3.png")
player_left = origin
player_right = pygame.transform.flip(player_left, True, False)


# Transform asset
background = pygame.transform.scale(background, (screen_width, screen_height))

player = player_right

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
    draw_background(test)

    # Player start position
    screen.blit(player, player_pos)

    # if press Key
    keys = pygame.key.get_pressed()

    # Move right - left
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        if (player_pos.y - 300 * dt >= 0):
            player_pos.y -= 300 * dt
        else:
            player_pos.y = 0
    if keys[pygame.K_s] or  keys[pygame.K_DOWN]:
        if player_pos.y + 300 * dt > bottom_bound:
            player_pos.y = bottom_bound
        else:
            player_pos.y += 300 * dt
            
    # Move Up - down
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if (player_pos.x - 300 * dt < 0):
            player_pos.x = 0
        else:
            player_pos.x -= 300 * dt
        player = player_right
    if keys[pygame.K_d] or  keys[pygame.K_RIGHT]:
        if player_pos.x + 300 * dt > right_bound:
            player_pos.x = right_bound
        else:
            player_pos.x += 300 * dt
        player = player_left

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
pygame.quit()