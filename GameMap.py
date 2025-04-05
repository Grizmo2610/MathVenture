import pygame


class Wall:
    def __init__(self, pos):
       self.rect = pygame.Rect(pos[0], pos[1], 32, 32)

class ProductBlock:
    def __init__(self, pos, point, isOnce):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.typePoint = "*"
        self.point = point
        self.isOnce = isOnce

class SumBlock:
    def __init__(self, pos, point, isOnce):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.typePoint = "+"
        self.point = point
        self.isOnce = isOnce

class SignalBlock:
    def __init__(self, pos, point, isOnce):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.typePoint = "-"
        self.point = point
        self.isOnce = isOnce

class ExpBlock:
    def __init__(self, pos, point, isOnce):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.typePoint = "^"
        self.point = point
        self.isOnce = isOnce

class QuotientBlock:
    def __init__(self, pos, point, isOnce):
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        self.typePoint = "/"
        self.point = point
        self.isOnce = isOnce

class MoveBlock:
    def __init__(self, position, direction):
        self.rect = pygame.Rect(position[0], position[1], 32, 32)
        self.direction = direction
        pass

class MapGame:
    start = 310
    def __init__(self, level, target):
        self.target = target
        self.level = level
        self.points = []
        self.walls = []
        self.moveBlocks = []
        self.x = self.start
        self.y = 100
        self.__detachLevel()
        
    def __detachLevel(self):
        x = self.x
        y = self.y
        for row in self.level:
            for col in row:
                if col[0] == "*":
                    point = 1
                    s = col.split("*")[1]
                    if s != '':
                        point = int(s)
                    isOnce = eval(col.split("*")[2])
                    self.points.append(ProductBlock((x, y), point, isOnce))
                elif col[0] == "-":
                    point = 0
                    s = col.split("-")[1]
                    if s != '':
                        point = int(s)
                    isOnce = eval(col.split("-")[2])
                    self.points.append(SignalBlock((x, y), point, isOnce))
                elif col[0] == "+":
                    point = 0
                    s = col.split("+")[1]
                    if s != '':
                        point = int(s)
                    isOnce = eval(col.split("+")[2])
                    self.points.append(SumBlock((x, y), point, isOnce))
                elif col[0] == "^":
                    point = 1
                    s = col.split("^")[1]
                    if s != '':
                        point = int(s)
                    isOnce = eval(col.split("^")[2])
                    self.points.append(ExpBlock((x, y), point, isOnce))
                elif col[0] == "/":
                    point = 1
                    s = col.split("/")[1]
                    if s != '':
                        point = int(s)
                    isOnce = eval(col.split("/")[2])
                    self.points.append(QuotientBlock((x, y), point, isOnce))
                elif col[0] == "f":
                    self.finish = (x, y)
                elif col[0] == "s":
                    self.start = (x, y)
                elif col[0] == '@':
                    # print("MoveBlock")
                    if col[1] == "U":
                        self.moveBlocks.append(MoveBlock((x, y), "Up"))
                    elif col[1] == "D":
                        self.moveBlocks.append(MoveBlock((x, y), "Down"))
                    elif col[1] == "L":
                        self.moveBlocks.append(MoveBlock((x, y), "Left"))
                    elif col[1] == "R":
                        self.moveBlocks.append(MoveBlock((x, y), "Right"))

                elif col[0] == "W":
                    self.walls.append(Wall((x, y)))    
                x += 32
            y += 32
            x = self.start
    
    def updateLevel(self, level, target):
        self.level = level
        self.__detachLevel()