import pygame
from Asset import Player
from GameMap import MapGame
from GameMap import game_maps
import os

# Init pygame
pygame.init()
# Init music
pygame.mixer.init()

# paths
block_path = "assets/sunny-land-files/Sunny-land-assets-files/PNG/environment/props/block-big.png"
background_path = "assets/sunny-land-files/Sunny-land-assets-files/PNG/environment/layers/back.png"
icon_path = "assets/Logo/3.png"
sprite_path = "assets/sunny-land-files/Sunny-land-assets-files/PNG/sprites/player/idle"
player_image_paths = os.listdir(sprite_path)
player_path = "./assets/sunny-land-files/Sunny-land-assets-files/PNG/sprites/player/idle/player-idle-3.png"
background_music_path = "assets/sunny-land-files/Sunny-land-assets-files/Sound/platformer_level03.mp3"

# Load media

# Load image
background = pygame.image.load(background_path)
block = pygame.image.load(block_path)
icon = pygame.image.load(icon_path)
origin = pygame.image.load(player_path)

# Load music
pygame.mixer.music.load(background_music_path)

# Srceen
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# Setup
pygame.display.set_caption("HAMIC MathVentrue")
pygame.display.set_icon(icon)

# Background
background = pygame.transform.scale(background, (screen_width, screen_height))

# Constant
clock = pygame.time.Clock()
FPS = 120
moving_left = False
moving_right = False
running = True

# Screen bound
right_bound = screen_width - 40
bottom_bound = screen_height - 40

# Player setup
# Player variable
dt = clock.tick(FPS) / 1000
distance = 300

# Setup image
player_right = origin
player_left = pygame.transform.flip(player_right, True, False)
player_image = player_right  # At first display

# Init payer
player = Player(screen.get_width() / 2, screen.get_height() / 2, dt, distance)


# Draw background at first
screen.blit(background, (0, 0))

# Play musix (-1 for looping music)
pygame.mixer.music.play(-1)

boxes = [pygame.Rect(100, 200, 50, 50),  # Vật thể không thể đi qua
            pygame.Rect(300, 300, 50, 50),  # Vật thể có thể đi qua
            ]
def draw_background(mapGame: MapGame):
    """
    This function draw background of game and all object in every game level
    """
    screen.blit(background, (0, 0))

    
    
    for box in boxes:
        pygame.draw.rect(screen, "RED", box)


def play_game(mapGame: MapGame, keys):
    global player_image
    global moving_left
    global moving_right

    # Drawing backgroud
    draw_background(mapGame)


    # Player start position
    screen.blit(player_image, player.get_pos())
    box = boxes[0]

    if player.rect.colliderect(box):
        # Xử lý va chạm
        if player.rect.top < box.bottom and player.rect.bottom > box.top:
            # Nếu nhân vật va chạm với vật thể từ trên hoặc dưới
            if player.rect.left < box.right and player.rect.right > box.left:
                # Nếu nhân vật đang ở bên trái vật thể
                player.rect.right = box.left
            elif player.rect.right > box.left and player.rect.left < box.right:
                # Nếu nhân vật đang ở bên phải vật thể
                player.rect.left = box.right
        elif player.rect.left < box.right and player.rect.right > box.left:
            # Nếu nhân vật va chạm với vật thể từ bên trái hoặc phải
            if player.rect.top < box.bottom and player.rect.bottom > box.top:
                # Nếu nhân vật đang ở phía trên vật thể
                player.rect.bottom = box.top
            elif player.rect.bottom > box.top and player.rect.top < box.bottom:
                # Nếu nhân vật đang ở phía dưới vật thể
                player.rect.top = box.bottom
    else:
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            player.up()
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player.down(bottom_bound)
        # Move left - right
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player.left()
            moving_left = True
            moving_right = False
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            moving_left = False
            moving_right = True
            player.right(right_bound)


while running:
    # Quit game event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if press Key
    keys = pygame.key.get_pressed()

    play_game(game_maps[0], keys)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 120
    player.dt = clock.tick(FPS) / 1000

    # Change image of sprite
    if moving_left:
        player_image = player_left
    elif moving_right:
        player_image = player_right

pygame.quit()
