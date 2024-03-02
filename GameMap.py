import pygame

class Wall:
    def __init__(self, pos):
       self.rect = pygame.Rect(pos[0], pos[1], 32, 32)

class ProductBlock(object):
    def __init__(self, pos, point, is_once):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.type_point = "*"
        self.point = point
        self.is_once = is_once

class SumBlock(object):
    def __init__(self, pos, point, is_once):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.type_point = "+"
        self.point = point
        self.is_once = is_once

class SignalBlock(object):
    def __init__(self, pos, point, is_once):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.type_point = "-"
        self.point = point
        self.is_once = is_once

class ExpBlock(object):
    def __init__(self, pos, point, is_once):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.type_point = "^"
        self.point = point
        self.is_once = is_once

class QuotientBlock(object):
    def __init__(self, pos, point, is_once):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.type_point = "/"
        self.point = point
        self.is_once = is_once
class MapGame:
    walls = []
    points = []
    level = [
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

    start = 255
    def str_to_int(point_type, inStr):
        s = inStr.split(point_type)[1]
        point = 1
        if s != '':
            point = int(s)
        return point
    def __init__(self) -> None:
        
        x = self.start
        y = 100
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
                x += 32
            y += 32
            x = self.start

game_maps = [MapGame(), MapGame()]
