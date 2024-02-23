import pygame
from Asset import Player
from GameMap import MapGame
from GameMap import game_maps

# Init pygame
pygame.init()
# Init music
pygame.mixer.init()

# paths
block_path = "assets/sunny-land-files/Sunny-land-assets-files/PNG/environment/props/block-big.png" 
background_path = "assets/sunny-land-files/Sunny-land-assets-files/PNG/environment/layers/back.png" 
icon_path = "assets/Logo/3.png"
player_path = "./assets/sunny-land-files/Sunny-land-assets-files/PNG/sprites/player/idle/player-idle-3.png"
background_music_path = "assets/sunny-land-files/Sunny-land-assets-files/Sound/platformer_level03.mp3"

# Load media

#@ Load image
background = pygame.image.load(background_path)
block = pygame.image.load(block_path)
icon = pygame.image.load(icon_path)
origin = pygame.image.load(player_path)

## Load music
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

# Variable
clock = pygame.time.Clock() 
FPS = 120

## Screen bound
right_bound = screen_width - 40 
bottom_bound = screen_height - 40 

# Player setup

## Player variable
dt = clock.tick(FPS) / 1000
distance = 300

## Setup image
player_left = origin
player_right = pygame.transform.flip(player_left, True, False)
player_image = player_right # At first display

## Init payer
player = Player(screen.get_width() / 2, screen.get_height() / 2, dt, distance)


# Draw background at first
screen.blit(background, (0,0))

# Play musix (-1 for looping music)
pygame.mixer.music.play(-1)

def draw_background(mapGame: MapGame):
    """
    This function draw background of game and all object in every game level
    """
    screen.blit(background, (0,0))


def play_game(mapGame: MapGame, keys):
    global player_image

    # Drawing backgroud
    draw_background(mapGame)

    # Player start position
    screen.blit(player_image, player.get_pos())

    # Move Up - Down
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player.up()
    if keys[pygame.K_s] or  keys[pygame.K_DOWN]:
        player.down(bottom_bound)
    
    # Move left - right
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.left()   
        player_image = player_right
    if keys[pygame.K_d] or  keys[pygame.K_RIGHT]:
        player.right(right_bound)
        player_image = player_left

running  = True
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

    # limits FPS to 60
    player.dt = clock.tick(FPS) / 1000
pygame.quit()