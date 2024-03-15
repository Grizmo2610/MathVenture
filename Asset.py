import pygame

class Point:
    def __init__(self, player):
        self.point = 0 #point
        self.player = player
        self.is_calculated = False
    
    def collide(self, type_point, point):
        if type_point == "*":
            self.point *= point # self.player.point
        elif type_point == "+":
            self.point += point
        elif type_point == "-":
            self.point -= point
        elif type_point == "/":
            self.point /= point
        elif type_point == "^":
            self.point = self.point ** point
    
    def calculation_collidision_point(self, points):
        count_length = 0
        count = 0
        for point in points:
            if self.player.rect.colliderect(point.rect) and not self.is_calculated:
                self.collide(point.type_point, point.point)
                # self.result = point
                self.is_calculated = True
            elif not self.player.rect.colliderect(point.rect):
                count_length += 1
            # if del_point == False:
            if point.is_once and self.player.rect.colliderect(point.rect):
                    del points[count]
            count += 1
        #print(count_length, len(points))
        if count_length == len(points):
            self.is_calculated = False
        # self.collide(self, '+', 4)
    

class Player:
    _instance = None

    def __new__(cls, x: int = 0, y: int = 0, dt: float = 0, distance: float = 300):
        if (cls._instance is None):
            cls._instance = super(Player, cls).__new__(cls)
            cls._instance.x = x
            cls._instance.y = y
            cls._instance.dt = dt
            cls._instance.distance = distance
            cls._instance.rect = pygame.Rect(x + 8, y + 15, 16, 16)

        return cls._instance


    def __init__(self, x: int = 0, y: int = 0, dt: float = 0, distance: float = 300) -> None:
        self.x = x
        self.y = y
        self.dt = dt
        self.distance = distance
        self.point = 0
        self.speed = self.distance * self.dt
        self.rect = pygame.Rect(x + 8, y + 15, 16, 16)

    def setlocation(self, x: int, y: int):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x + 8, y + 15, 16, 16)


    def get_pos(self):
        return (self.x, self.y)
    
    def move(self, dx, dy, walls):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0, walls)
        if dy != 0:
            self.move_single_axis(0, dy, walls)

    def move_single_axis(self, dx, dy, walls):
        # Move the rect
        self.resx = self.x
        self.resy = self.y
        self.x += dx
        self.y += dy
        self.rect.x += dx
        self.rect.y += dy
         # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                    self.x = self.resx
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                    self.x = self.resx
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                    self.y = self.resy
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
                    self.y = self.resy
    