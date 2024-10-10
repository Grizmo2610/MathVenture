# import pygame
# import numpy as np

# pygame.init()

# screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

# running = True

# class Block:
#     def __init__(self, x, y, width, height, data : str):
#         self.x, self.y, self.width, self.height = x, y, width, height
#         self.data = data
#         self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
#     def visualizeBlock(self, screen):
#         pygame.draw.rect(screen, pygame.Color('pink'), self.rect)
#         font = pygame.font.Font('freesansbold.ttf',self.width//len(self.data))
#         text = font.render(self.data, True, pygame.Color('black'))
#         text_rect = text.get_rect(center=(self.x + self.width//2, self.y + self.height//2))
#         screen.blit(text, text_rect)

# block = Block(12, 12, 100, 110, "H")
    
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     block.visualizeBlock(screen)
#     pygame.display.flip()
# pygame.quit()