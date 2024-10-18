import pygame
from Asset import *
from GameMap import *
import os

# Init pygame
pygame.init()
# Init music
pygame.mixer.init()

# direction
moves = ["Down", "Up", "Left", "Right"]
point_types = ['sum', 'multiply', 'minus', 'divide', 'pow']

# paths
block_points_path = {_ : "assets/PNG/block/point/{}.png".format(_) for _ in point_types}
block_points_path_move1 = {_ : "assets/PNG/block/point/{}_move1.png".format(_) for _ in point_types}
wall_path = "assets/PNG/block/wall/block-big.png"
move_blocks_path = {move : "assets/PNG/block/move/arow3{}.png".format(move) for move in moves}
background_path = "assets/PNG/background/background.png"
icon_path = "assets/PNG/Logo/3.png"
sprite_path = "assets/PNG/player"
player_image_paths = os.listdir(sprite_path)
player_path = "./assets/PNG/player/player-idle-3.png"
background_music_path = "assets/Sound/platformer_level03.mp3"
background_level_path = "assets/PNG/Level/BackLevel.png"

# Load image
background = pygame.image.load(background_path)
block = pygame.image.load(wall_path)
icon = pygame.image.load(icon_path)
origin = pygame.image.load(player_path)
move_blocks = {path : pygame.image.load(move_blocks_path[path]) for path in move_blocks_path}
point_blocks = {path : pygame.image.load(block_points_path[path]) for path in block_points_path}
background_level = pygame.image.load(background_level_path)
point_blocks_move1 = {path : pygame.image.load(block_points_path_move1[path]) for path in block_points_path_move1}
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
FPS = 300
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
xPlayer = screen.get_width() / 2 + 16
yPlayer = screen.get_height() / 2
player = Player(xPlayer, yPlayer, dt, distance)

# Draw background at first
screen.blit(background, (0, 0))

# Play musix (-1 for looping music)
pygame.mixer.music.play(-1)

# init point
pointer = Point(player)

#init level
level = 0

# targets
targets = []

# maps
levels = []
game_maps = []

#max_level
maxLevel = 4

def init():
    for i in range(maxLevel):
        [target, map_level] = read_level(i + 1)
        targets.append(target)
        levels.append(map_level)
        game_maps.append(MapGame(levels[i], targets[i]))

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
    player.setlocation(xPlayer, yPlayer)
    if level >= maxLevel:
        level = 0
        game_maps = [MapGame(levels[_], targets[_]) for _ in range(maxLevel)]


def draw_back_point(type_point, x, y):
    if type_point == '+':
        screen.blit(point_blocks['sum'], (x, y))
    elif type_point == '*':
        screen.blit(point_blocks['multiply'], (x, y))
    elif type_point == '-':
        screen.blit(point_blocks['minus'], (x, y))
    elif type_point == '/':
        screen.blit(point_blocks['divide'], (x, y))
    elif type_point == '^':
        screen.blit(point_blocks['pow'], (x, y))

def draw_back_point_move1(type_point, x, y):
    if type_point == '+':
        screen.blit(point_blocks_move1['sum'], (x, y))
    elif type_point == '*':
        screen.blit(point_blocks_move1['multiply'], (x, y))
    elif type_point == '-':
        screen.blit(point_blocks_move1['minus'], (x, y))
    elif type_point == '/':
        screen.blit(point_blocks_move1['divide'], (x, y))
    elif type_point == '^':
        screen.blit(point_blocks_move1['pow'], (x, y))

def draw_point_block(points, screen):
    for point in points:
        text = str(point.point)
        font = pygame.font.Font(None, (30//len(text)*len(text)))
        txt = font.render(text, (True), pygame.Color('black'))
        text_rect = txt.get_rect(center=(point.rect.x + 30//2, point.rect.y + 32//2))
        if point.is_once:
            draw_back_point_move1(point.type_point, point.rect.x, point.rect.y)
        else:
            draw_back_point(point.type_point, point.rect.x, point.rect.y)
        screen.blit(txt, text_rect)

def draw_move_block(moveBloks, screen):
    for moveBlock in moveBloks:
        screen.blit(move_blocks[moveBlock.direction], (moveBlock.rect.x, moveBlock.rect.y))

def draw_level():
    x, y = 1000, 150
    screen.blit(background_level, (x, y))
    text = "Level: " + str(level + 1)
    font = pygame.font.SysFont('comicsans', 50//len(text)*len(text))
    txt = font.render(text, (True), (225, 225, 225))
    text_rect = txt.get_rect(center=(x + 230//2, y + 102//2))
    screen.blit(txt, text_rect)

def draw_target_score(target):
    x, y = 1000, 280
    font = pygame.font.SysFont('comicsans', 40)
    target_str = font.render("Target: " + str(target), (True), (225, 225, 0))
    text = font.render("Score: " + str(pointer.point), (True), (225, 0, 0))
    screen.blit(target_str, (x, y))
    screen.blit(text, (x, y + 45))

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

    draw_level()
    # Draw wall
    for wall in walls:
        screen.blit(block,(wall.rect.x, wall.rect.y))
    
    draw_point_block(points, screen)

    draw_move_block(mapGame.moveBloks, screen)
    
    pointer.calculation_collidision_point(points)
    player.moveInMoveBlock(game_maps[level].moveBloks)
    
    if target == pointer.point:
        update_level()
    
    draw_target_score(target)
    # pygame.draw.rect(screen, (0, 0, 0), player.rect)
    
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
        player.move(0, -3, walls)  
    if keys[pygame.K_s] or  keys[pygame.K_DOWN]:
        player.move(0, 3, walls)
    # Move left - right
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.move(-3, 0, walls)
        player_image = player_right
    if keys[pygame.K_d] or  keys[pygame.K_RIGHT]:
        player.move(3, 0, walls)
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
                if 1000 < mouse_x < 1000 + 1920/12 and 150 < mouse_y < 150 + 1080/12:
                    game_maps[level] = MapGame(levels[level], targets[level])
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

if __name__ == '__main__':
    main()