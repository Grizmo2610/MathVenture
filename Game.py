import pygame
from Asset import *
from GameMap import *
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
finish_block = "assets/temp/finish.png"
levels_path = "assets/Level"
level_button_paths = os.listdir("assets/Level")

# button path
start_path = "assets/temp/Start.png"
tutorial_path = "assets/temp/Tutorial.png"
quit_path = "assets/temp/Quit.png"

# Load media

# Load image
background = pygame.image.load(background_path)
block = pygame.image.load(block_path)
icon = pygame.image.load(icon_path)
origin = pygame.image.load(player_path)
finish_image = pygame.image.load(finish_block)

def load_image_button(path, scale = 0.1):
    image = pygame.image.load(path)
    return pygame.transform.scale(image, (image.get_width() * scale, image.get_height() * scale))

# load button image
buttons_images = {"Start": load_image_button(start_path),
          "Tutorial": load_image_button(tutorial_path),
          "Quit": load_image_button(quit_path)
          }

# Load level button
for i in range(len(level_button_paths)):
    buttons_images.setdefault(f"level{i+1:02d}", load_image_button(levels_path + "/" + level_button_paths[i]))

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


# Player setup
# Player variable
dt = clock.tick(FPS) / 1000
distance = 300

# Setup image
player_right = origin
player_left = pygame.transform.flip(origin, True, False)

player_image = player_right  # At first display

# Init player
player = Player(screen.get_width() / 2, screen.get_height() / 2, dt, distance)


# Draw background at first
screen.blit(background, (0, 0))

# Play musix (-1 for looping music)
pygame.mixer.music.play(-1)

# init point
pointer = Point(player)


def draw_background(map_game: MapGame):
    """
    This function draw background of game and all object in every game level
    """
    screen.blit(background, (0, 0))
    global walls
    global points
    global first
    if first:
        first = False
        walls = map_game.walls.copy()
        points = map_game.points.copy()

    for wall in walls:
        screen.blit(block, (wall.rect.x, wall.rect.y))

    for point in points:
        txt = font.render(point.type_point +
                          str(point.point), (True), (225, 0, 0))
        if point.is_once == True:
            pygame.draw.circle(screen, (225, 225, 225),
                               (point.rect.x + 16, point.rect.y + 16), 16)
        else:
            pygame.draw.rect(screen, (0, 0, 0), point.rect)
        screen.blit(txt, (point.rect.x, point.rect.y))
    pointer.calculation_collidision_point(points)
    score = font.render("Score: " + str(pointer.point), (True), (225, 0, 0))
    screen.blit(score, (10, 10))
    screen.blit(finish_image, (map_game.finish[0] * 32 + 255, map_game.finish[1] * 32 + 100))


def draw_text(text, font, text_col, x=255, y=255):
    img = font.render(text, True, text_col)
    screen.blit(text, (x, y))


def main_menu():
    x = screen.get_width() / 2 - buttons_images['Start'].get_width() / 10 - 60
    y = 100
    global status
    global running
    start_button = Button(x, y * 1, buttons_images["Start"], 1)
    tutorial_button = Button(x, y * 3, buttons_images["Tutorial"], 1)
    quit_button = Button(x, y * 5, buttons_images["Quit"], 1)
    if start_button.draw(screen):
        status = level_game
    elif tutorial_button.draw(screen):
        status = tutorial
    elif quit_button.draw(screen):
        running = False


def end(map_game: MapGame, keys):
    default_status(map_game, keys)
    pass

def tutorial(map_game: MapGame, keys):
    pass

def level_game(map_game: MapGame, keys):
    screen.blit(background, (0, 0))
    global status
    buttons = []
    left = 300
    up = 30
    for i in range(5):
        buttons.append(Button(left, i * 130 + up, buttons_images[f'level{2 * i + 1:02d}'], 1))
        buttons.append(Button(left + 500, i * 130 + up, buttons_images[f'level{2 * i + 2:02d}'], 1))

    for button in buttons:
        if (button.draw(screen)):
            status = play_game

def default_status(map_game: MapGame, keys):
    global player_image
    global status
    global first

    player_image = player_left
    player.rect.x, player.rect.y = map_game.start
    pointer.point = 0
    draw_background(map_game)
    screen.blit(player_image, player.get_pos())
    screen.blit(finish_image, map_game.finish)
    first = True
    status = play_game


def play_game(map_game: MapGame, keys):
    global player_image
    global moving_left
    global moving_right
    global status
    if (first):
        default_status(map_game, keys)
    walls = map_game.walls.copy()

    if (pointer.point < 0):
        status = end

    # Drawing backgroud
    draw_background(map_game)
    screen.blit(finish_image, map_game.finish)

    # Player start position
    screen.blit(player_image, player.get_pos())
    # Move Up - Down
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        # player.up()
        player.move(0, -2, walls)
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player.move(0, 2, walls)
    # Move left - right
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.move(-2, 0, walls)
        moving_left = True
        moving_right = False
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.move(2, 0, walls)
        moving_right = True
        moving_left = False

    # limits FPS to 120
    player.dt = clock.tick(FPS) / 1000

    # Change image of sprite
    if moving_left:
        player_image = player_left
    elif moving_right:
        player_image = player_right


# Game status
status = main_menu
walls = []
points = []
first = True
font = pygame.font.Font(None, 30)

# Main loop
while running:
    # Quit game event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if press Key
    keys = pygame.key.get_pressed()

    if status == main_menu:
        status()
    else:
        status(game_maps[0], keys)

    pygame.display.flip()

pygame.quit()
