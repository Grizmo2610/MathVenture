import pygame


class Wall:
    def __init__(self, pos):
       self.rect = pygame.Rect(pos[0], pos[1], 32, 32)

class ProductBlock:
    def __init__(self, pos, point, is_once):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.type_point = "*"
        self.point = point
        self.is_once = is_once

class SumBlock:
    def __init__(self, pos, point, is_once):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.type_point = "+"
        self.point = point
        self.is_once = is_once

class SignalBlock:
    def __init__(self, pos, point, is_once):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.type_point = "-"
        self.point = point
        self.is_once = is_once

class ExpBlock:
    def __init__(self, pos, point, is_once):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.type_point = "^"
        self.point = point
        self.is_once = is_once

class QuotientBlock:
    def __init__(self, pos, point, is_once):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.type_point = "/"
        self.point = point
        self.is_once = is_once
class MapGame:
<<<<<<< HEAD
    start = 255
    def str_to_int(point_type, inStr):
        s = inStr.split(point_type)[1]
        point = 1
        if s != '':
            point = int(s)
        return point
    def __init__(self, level, target):
        self.target = target
        self.level = level
        self.points = []
        self.walls = []
        x = self.start
        y = 100
=======
    walls = []
    points = []
    level = []
    # level = [
    # ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    # ["W", "*12*True", " ", " ", " ", "-99-True", " ", "^3^False", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
    # ["W", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W", "W", "W", "W", "W", "W", " ", " ", " ", "W"],
    # ["W", " ", " ", " ", "W", "W", "W", "W", " ", " ", " ", " ", " ", " ", " ", "W", " ", " ", " ", "W"],
    # ["W", " ", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", "W", "W", "W", "W", " ", " ", "W"],
    # ["W", " ", "W", "W", "W", " ", " ", "W", "W", "W", "W", " ", " ", " ", "+12+False", " ", " ", " ", " ", "W"],
    # ["W", " ", " ", " ", "W", " ", " ", " ", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
    # ["W", " ", " ", " ", "W", " ", " ", " ", " ", " ", "W", " ", " ", " ", "W", "W", "W", " ", "W", "W"],
    # ["W", " ", " ", " ", "W", "W", "W", " ", "W", "W", "W", " ", " ", " ", "W", " ", "W", " ", " ", "W"],
    # ["W", " ", " ", " ", " ", " ", "W", " ", " ", " ", "W", " ", " ", " ", "W", " ", "W", " ", " ", "W"],
    # ["W", "W", "W", "W", " ", " ", "W", " ", " ", " ", "W", "W", "W", "W", "W", " ", "W", " ", " ", "W"],
    # ["W", " ", " ", "W", " ", " ", " ", " ", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
    # ["W", " ", " ", "W", " ", " ", "W", "W", "W", "W", "W", " ", " ", "W", "W", "W", " ", " ", " ", "W"],
    # ["W", " ", " ", " ", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", "W", " ", " ", " ", "W"],
    # ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    # ]

    start_x = 255
    start_y = 100

    def __init__(self, level:list[list[str]]) -> None:
        self.level = level
        x = self.start_x
        y = self.start_y
>>>>>>> 5c8ed447fc5508f556434a698a7531d9b4c50f22
        for row in self.level:
            for col in row:
                if col[0] == "W":
                    self.walls.append(Wall((x, y)))    
                elif col[0] == "*":
                    point = 1
                    s = col.split("*")[1]
                    if s != '':
                        point = int(s)
                    is_once = eval(col.split("*")[2])
                    self.points.append(ProductBlock((x, y), point, is_once))
                elif col[0] == "-":
                    point = 0
                    s = col.split("-")[1]
                    if s != '':
                        point = int(s)
                    is_once = eval(col.split("-")[2])
                    self.points.append(SignalBlock((x, y), point, is_once))
                elif col[0] == "+":
                    point = 0
                    s = col.split("+")[1]
                    if s != '':
                        point = int(s)
                    is_once = eval(col.split("+")[2])
                    self.points.append(SumBlock((x, y), point, is_once))
                elif col[0] == "^":
                    point = 1
                    s = col.split("^")[1]
                    if s != '':
                        point = int(s)
                    is_once = eval(col.split("^")[2])
                    self.points.append(ExpBlock((x, y), point, is_once))
                elif col[0] == "/":
                    point = 1
                    s = col.split("/")[1]
                    if s != '':
                        point = int(s)
                    is_once = eval(col.split("/")[2])
                    self.points.append(QuotientBlock((x, y), point, is_once))
                elif col[0] == "f":
                    self.finish = (x, y)
                elif col[0] == "s":
                    self.start = (x, y)
                x += 32
            y += 32
            x = self.start_x

<<<<<<< HEAD
target_1 = -324
level_1 = [
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "*12*True", " ", " ", " ", "-99-True", " ", "^3^False", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
    ["W", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W", "W", "W", "W", "W", "W", " ", " ", " ", "W"],
    ["W", " ", " ", " ", "W", "W", "W", "W", " ", " ", " ", " ", " ", " ", " ", "W", " ", " ", " ", "W"],
    ["W", " ", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", "W", "W", "W", "W", " ", " ", "W"],
    ["W", " ", "W", "W", "W", " ", " ", "W", "W", "W", "W", " ", " ", " ", "+12+False", " ", " ", " ", " ", "W"],
    ["W", " ", " ", " ", "W", " ", " ", " ", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
    ["W", " ", " ", " ", "W", " ", " ", " ", " ", " ", "W", " ", " ", " ", "W", "W", "W", " ", "W", "W"],
    ["W", " ", " ", " ", "W", "W", "W", " ", "W", "W", "W", " ", " ", " ", "W", " ", "W", " ", " ", "W"],
    ["W", " ", " ", " ", " ", " ", "W", " ", " ", " ", "W", " ", " ", " ", "W", " ", "W", " ", " ", "W"],
    ["W", "W", "W", "W", " ", " ", "W", " ", " ", " ", "W", "W", "W", "W", "W", " ", "W", " ", " ", "W"],
    ["W", " ", " ", "W", " ", " ", " ", " ", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
    ["W", " ", " ", "W", " ", " ", "W", "W", "W", "W", "W", " ", " ", "W", "W", "W", " ", " ", " ", "W"],
    ["W", " ", " ", " ", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", "W", " ", " ", " ", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
]

target_2 = 31
level_2 = [
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", " ", " ", " ", "W", " ", " ", " ", "W", "W", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
    ["W", "W", "W", " ", "W", " ", " ", " ", " ", "W", " ", "W", "W", "W", "W", "W", "W", "W", " ", "W"],
    ["W", " ", "W", " ", " ", " ", "W", "W", " ", " ", " ", " ", " ", " ", " ", "W", " ", "W", " ", "W"],
    ["W", " ", " ", " ", " ", " ", "W", " ", " ", "W", "W", " ", " ", " ", " ", "W", " ", "W", " ", "W"],
    ["W", "W", "W", " ", " ", " ", "W", "W", " ", " ", "W", "W", " ", "W", " ", "W", " ", "W", " ", "W"],
    ["W", " ", "W", " ", "W", "W", " ", "W", "W", " ", "W", "W", " ", " ", " ", "W", " ", "W", " ", "W"],
    ["W", " ", " ", " ", "W", " ", " ", " ", "W", " ", " ", " ", " ", " ", " ", "W", " ", " ", " ", "W"],
    ["W", "W", "W", " ", "W", " ", " ", " ", "W", " ", "W", " ", " ", "W", " ", "W", " ", " ", " ", "W"],
    ["W", " ", " ", " ", " ", " ", " ", " ", "W", " ", "W", "W", " ", " ", " ", "W", "W", " ", " ", "W"],
    ["W", " ", " ", "W", " ", " ", " ", "W", "W", " ", " ", " ", "W", " ", " ", " ", " ", " ", " ", "W"],
    ["W", "W", " ", "W", "W", " ", "W", " ", " ", " ", "W", " ", "W", " ", " ", " ", " ", "W", " ", "W"],
    ["W", " ", " ", " ", " ", " ", "W", " ", " ", " ", "W", " ", " ", " ", "W", " ", " ", " ", " ", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"]
]
game_maps = [MapGame(level_1, target_1), MapGame(level_2, target_2)]
=======
    def str_to_int(point_type, inStr: str):
        s = inStr.split(point_type)[1]
        point = 1
        if s != '':
            point = int(s)
        return point

level = []
with open('maps/level01.txt', 'r+') as f:
    level = f.readlines()
level = [x.strip().replace(', ', ',').split(',') for x in level]

game_maps = [MapGame(level), MapGame(level)]
>>>>>>> 5c8ed447fc5508f556434a698a7531d9b4c50f22
