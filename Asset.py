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
            cls._instance.dt = dt
            cls._instance.distance = distance
            cls._instance.rect = pygame.Rect(x + 9, y + 15, 16, 16) #Modify the square to match player icon
        return cls._instance


    def __init__(self, x: int = 0, y: int = 0, dt: float = 0, distance: float = 300) -> None:
        self.dt = dt
        self.distance = distance
        self.point = 0
        self.speed = self.distance * self.dt
        self.rect = pygame.Rect(x + 9, y + 15, 16, 16) # Modify the square to match player icon
    
    def get_pos(self):
        return (self.rect.x - 9, self.rect.y - 15)
    
    def move(self, dx, dy, walls):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0, walls)
        if dy != 0:
            self.move_single_axis(0, dy, walls)

    def move_single_axis(self, dx, dy, walls):
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy
         # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

#button class
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action