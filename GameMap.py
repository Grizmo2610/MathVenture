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

class MoveBlock:
    def __init__(self, position, direction):
        self.rect = pygame.Rect(position[0], position[1], 32, 32)
        self.direction = direction
        pass

class MapGame:
    start = 255
    def __init__(self, level, target):
        self.target = target
        self.level = level
        self.points = []
        self.walls = []
        self.moveBloks = []
        x = self.start
        y = 100
        for row in self.level:
            for col in row:
                if col[0] == "*":
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
                elif col[0] == '@':
                    # print("MoveBlock")
                    if col[1] == "U":
                        self.moveBloks.append(MoveBlock((x, y), "Up"))
                    elif col[1] == "D":
                        self.moveBloks.append(MoveBlock((x, y), "Down"))
                    elif col[1] == "L":
                        self.moveBloks.append(MoveBlock((x, y), "Left"))
                    elif col[1] == "R":
                        self.moveBloks.append(MoveBlock((x, y), "Right"))

                elif col[0] == "W":
                    self.walls.append(Wall((x, y)))    
                x += 32
            y += 32
            x = self.start