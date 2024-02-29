import pygame

class Wall(object):
     def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

class MapGame:
    walls = []
    level = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W                  W",
    "W         WWWWWW   W",
    "W   WWWW       W   W",
    "W   W        WWWW  W",
    "W WWW  WWWW        W",
    "W   W     W        W",
    "W   W     W   WWW WW",
    "W   WWW WWW   W W  W",
    "W     W   W   W W  W",
    "WWWW  W   WWWWW W  W",
    "W  W      W        W",
    "W  W  WWWWW  WWW   W",
    "W     W        W   W",
    "WWWWWWWWWWWWWWWWWWWW",
    ]

    start = 255
    def __init__(self) -> None:
        
        x = self.start
        y = 100
        for row in self.level:
            for col in row:
                if col == "W":
                    self.walls.append(Wall((x, y)))    
                x += 32
            y += 32
            x = self.start

game_maps = [MapGame(), MapGame()]
