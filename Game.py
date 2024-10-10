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
# path demo tree == menu
tree_path = "assets/sunny-land-files/Sunny-land-assets-files/PNG/environment/props/tree.png"
cherry_path = "assets/sunny-land-files/Sunny-land-assets-files/PNG/sprites/cherry/cherry-2.png"
gem_path = "assets/sunny-land-files/Sunny-land-assets-files/PNG/sprites/gem/gem-5.png"
# Load media

# Load image
background = pygame.image.load(background_path)
block = pygame.image.load(block_path)
icon = pygame.image.load(icon_path)
origin = pygame.image.load(player_path)
path_img_level = ['assets/level/' + str(_ + 1)  + '.png' for _ in range(9)]
img_level = [pygame.image.load(path) for path in path_img_level]

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
player_left = origin
player_right = pygame.transform.flip(player_left, True, False)
player_image = player_right  # At first display

# Init payer
player = Player(screen.get_width() / 2, screen.get_height() / 2, dt, distance)


# Draw background at first
screen.blit(background, (0, 0))

# Play musix (-1 for looping music)
pygame.mixer.music.play(-1)

# init point
pointer = Point(player)

font = pygame.font.Font(None, 23)
font_target = pygame.font.Font(None, 50)
#init level
level = 0

# targets
targets = []

# maps
levels = []
game_maps = []

#max_level
maxLevel = 4

font_chose = pygame.font.SysFont('comicsans', 40)
text_chose = font_chose.render('Chose level', 1, (255, 255, 255))

def init():
    for i in range(maxLevel):
        [target, map_level] = read_level(i + 1)
        targets.append(target)
        levels.append(map_level)
        game_maps.append(MapGame(levels[i], targets[i], img_level[i]))


def chose_level():
    pygame.draw.rect(screen, pygame.Color('pink'), pygame.Rect(140, 70, 1000, 600))
    screen.blit(text_chose, (500, 100))
    for i in range(3):
        screen.blit(game_maps[i].level_img, (200 + 350 * i, 200))
    for i in range(3, 5):
        screen.blit(game_maps[i].level_img, (380 + 350 * (i - 3), 400))

def read_level(numStr):
    file = open('maps/level'+ str(numStr) +'.txt', 'r')
    data = []
    target = int(file.readline())
    for _ in range(16):
        line = file.readline()
        data.append(line[:len(line) - 2].split(', '))
    
    return [int(target), data]

#update level
def update_level():
    global level
    global game_maps
    global pointer
    global player
    global maxLevel
    level += 1
    pointer.point = 0
    player.setlocation(screen.get_width()/2, screen.get_height()/2)
    if level >= maxLevel:
        level = 0
        game_maps = [MapGame(levels[_], targets[_], img_level[_]) for _ in range(maxLevel)]


def draw_point_block(points, screen):
    for point in points:
        text = point.type_point + str(point.point)
        font = pygame.font.Font(None, (32//len(text)) * len(text) - 4)
        txt = font.render(text, (True), pygame.Color('black'))
        txt.get_rect(center=(point.rect.x + 32//len(text), point.rect.y + 32//len(text)))
        if point.is_once:
            pygame.draw.circle(screen, (225, 125, 225),
                                (point.rect.x + 16, point.rect.y + 16), 16)
        else:
            pygame.draw.rect(screen, pygame.Color('green'), point.rect)
        screen.blit(txt, (point.rect.x + 1, point.rect.y + 10))

def draw_move_block(moveBloks, screen):
    for moveBlock in moveBloks:
        text = str(moveBlock.direction)
        text += text
        font = pygame.font.Font(None, (32//len(text)) * len(text) - 4)
        txt = font.render(text, (True), pygame.Color('black'))
        txt.get_rect(center=(moveBlock.rect.x + 32//len(text), moveBlock.rect.y + 32//len(text)))
        pygame.draw.rect(screen, pygame.Color('red'), moveBlock.rect)
        screen.blit(txt, (moveBlock.rect.x + 1, moveBlock.rect.y + 10))

        

def draw_background(mapGame: MapGame):
    """
    This function draw background of game and all object in every game level
    """
    global level
    global game_maps
    screen.blit(background, (0, 0))
    walls = mapGame.walls
    points = mapGame.points
    target = mapGame.target
    #pygame.draw.rect(screen, (0, 0, 0), player.rect)

    screen.blit(mapGame.level_img, (1000, 200))
    # screen.blit(tree, (1100, 100))    
    # Draw wall
    for wall in walls:
        screen.blit(block,(wall.rect.x, wall.rect.y))
    
    draw_point_block(points, screen)
    
    draw_move_block(mapGame.moveBloks, screen)
    # pygame.draw.rect(screen, (0, 0, 0), player.rect)
    pointer.calculation_collidision_point(points)
    player.moveInMoveBlock(game_maps[level].moveBloks)
    
    if target == pointer.point:
        update_level()
    
    target_str = font_target.render("Target: " + str(target), (True), (225, 225, 0))
    text = font_target.render("Score: " + str(pointer.point), (True), (225, 0, 0))
    screen.blit(target_str, (100, 600))
    screen.blit(text, (100, 650))
    
def play_game(mapGame: MapGame, keys):
    global player_image
    global moving_left
    global moving_right
    walls = mapGame.walls

    # Drawing backgroud
    draw_background(mapGame)

    # Player start position
    screen.blit(player_image, player.get_pos())

     # Move Up - Down
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        #player.up()
        player.move(0, -2, walls)  
    if keys[pygame.K_s] or  keys[pygame.K_DOWN]:
        player.move(0, 2, walls)
    # Move left - right
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.move(-2, 0, walls)
        player_image = player_right
    if keys[pygame.K_d] or  keys[pygame.K_RIGHT]:
        player.move(2, 0, walls)
        player_image = player_left

def main():
    global running, level, game_maps, pointer, player, player_image
    global moving_left, moving_right, player_left, player_right

    
    init()

    while running:
        # Quit game event
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 1000 < mouse_x < 1000 + 1920/12 and 200 < mouse_y < 200 + 1080/12:
                    game_maps[level] = MapGame(levels[level], targets[level], img_level[level])
                    pointer.point = 0
        # if press Key
        keys = pygame.key.get_pressed()

        play_game(game_maps[level], keys)

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

main()