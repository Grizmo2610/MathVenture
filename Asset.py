class Map:
    def __init__(self, background: list[list[int]] = ...) -> None:
        """
        Each map must be init must have exactly 22 * 40 block. Each block is 32 * 32 pixels
        """

        # block = "assets/sunny-land-files/Sunny-land-assets-files/PNG/environment/props/block-big.png"
        
        # for i in range(40):
        #     background[0][i] = background[-1][i] = block
        #     if (i < 22):
        #         background[i][0] = background [i][-1] = block
            
        self.background = background
    
    def __str__(self) -> str:
        result = ""
        for i in range(22):
            for j in range(40):
                result += str(self.background[i][j]) + " "
            result += "\n"
        return result
    
    def get_background(self):
        return self.background

class Player:
    _instance = None

    def __new__(cls):
        if (cls._instance is None):
            cls._instance = super(Player, cls).__new__(cls)
        return cls._instance

    def __init__(self, x: int = 0, y: int = 0, dt: float = 0, distance: float = 300) -> None:
        self.x = x
        self.y = y
        self.dt = dt
        self.distance = distance
        self.point = 0
        self.speed = self.distance * self.dt
    
    def up(self):
        self.y -= self.speed
    
    def down(self):
        self.y += self.speed
    
    def left(self):
        self.x -= self.speed
    
    def right(self):
        self.x += self.speed