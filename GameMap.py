import pygame

class Wall(object):
    def __init__(self, pos):
       self.rect = pygame.Rect(pos[0], pos[1], 32, 32)

class ProductBlock(object):
    def __init__(self, pos, point):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.type_point = "*"
        self.point = point

class SumBlock(object):
    def __init__(self, pos, point):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.type_point = "+"
        self.point = point

class SignalBlock(object):
    def __init__(self, pos, point):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.type_point = "-"
        self.point = point

class ExpBlock(object):
    def __init__(self, pos, point):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.type_point = "^"
        self.point = point

class QuotientBlock(object):
    def __init__(self, pos, point):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.type_point = "/"
        self.point = point

class MapGame:
    walls = []
    points = []
    level = [
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "*12", " ", "*", " ", "-99", " ", "^", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
    ["W", " ", " ", " ", " ", " ", "*", " ", " ", " ", "W", "W", "W", "W", "W", "W", " ", " ", " ", "W"],
    ["W", " ", " ", " ", "W", "W", "W", "W", " ", " ", " ", " ", " ", " ", " ", "W", " ", " ", " ", "W"],
    ["W", " ", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", "W", "W", "W", "W", " ", " ", "W"],
    ["W", " ", "W", "W", "W", " ", " ", "W", "W", "W", "W", " ", " ", " ", "+12", " ", " ", " ", " ", "W"],
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
                    self.points.append(ProductBlock((x, y), point))
                elif col[0] == "-":
                    point = 0
                    s = col.split("-")[1]
                    if s != '':
                        point = int(s)
                    self.points.append(SignalBlock((x, y), point))
                elif col[0] == "+":
                    point = 0
                    s = col.split("+")[1]
                    if s != '':
                        point = int(s)
                    self.points.append(SumBlock((x, y), point))
                elif col[0] == "^":
                    point = 1
                    s = col.split("^")[1]
                    if s != '':
                        point = int(s)
                    self.points.append(ExpBlock((x, y), point))
                elif col[0] == "/":
                    point = 1
                    s = col.split("/")[1]
                    if s != '':
                        point = int(s)
                    self.points.append(QuotientBlock((x, y), point))
                x += 32
            y += 32
            x = self.start

game_maps = [MapGame(), MapGame()]
