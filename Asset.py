class MyObject:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def collide(self) -> None:
        pass

class Wall(MyObject):
    def collide(self):
        pass
        

class Point(MyObject):
    def __init__(self, x: int, y: int, player, type_point: str, point: int = 0) -> None:
        super().__init__(x, y)
        self.type_point = type_point
        self.point = point
        self.player = player
    
    def collide(self):
        if self.type_point == "*":
            self.player.point *= self.point
        elif self.type_point == "+":
            self.player.point += self.point
        elif self.type_point == "-":
            self.player.point -= self.point
        elif self.type_point == "/":
            self.player.point /= self.point
        elif self.type_point == "^":
            self.player.point = self.player.point ** self.point

class Player:
    _instance = None

    def __new__(cls, x: int = 0, y: int = 0, dt: float = 0, distance: float = 300):
        if (cls._instance is None):
            cls._instance = super(Player, cls).__new__(cls)
            cls._instance.x = x
            cls._instance.y = y
            cls._instance.dt = dt
            cls._instance.distance = distance

        return cls._instance


    def __init__(self, x: int = 0, y: int = 0, dt: float = 0, distance: float = 300) -> None:
        self.x = x
        self.y = y
        self.dt = dt
        self.distance = distance
        self.point = 0
        self.speed = self.distance * self.dt
    

    def up(self):
        if (self.y - self.speed < 0):
            self.y = 0
        else:
            self.y -= self.speed
    
    def down(self, bound):
        if (self.y + self.speed >= bound):
            self.y = bound
        else:
            self.y += self.speed
    
    def left(self):
        if (self.x - self.speed < 0):
            self.x = 0
        else:
            self.x -= self.speed
    
    def right(self, bound):
        if (self.x + self.speed >= bound):
            self.x = bound
        else:
            self.x += self.speed
    
    def get_pos(self):
        return (self.x, self.y)
    


