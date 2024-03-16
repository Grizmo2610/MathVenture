# import pygame
# from GameMap import *

# pygame.init()

# screen = pygame.display.set_mode((1280, 720))

# runing = True
# clock = pygame.time.Clock()
# dt = clock.tick(120) / 1000

# font_chose = pygame.font.SysFont('comicsans', 40)
# text_chose = font_chose.render('Chose level', 1, (255, 255, 255))
# def chose_level():
#     pygame.draw.rect(screen, pygame.Color('pink'), pygame.Rect(140, 70, 1000, 600))
#     screen.blit(text_chose, (500, 100))
#     for i in range(3):
#         screen.blit(game_maps[i].level_img, (200 + 350 * i, 200))
#     for i in range(3, 5):
#         screen.blit(game_maps[i].level_img, (380 + 350 * (i - 3), 400))

# print(game_maps[0].level_img.get_height(), game_maps[0].level_img.get_width())

# # while runing:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             runing = False
# #         # Create a font object
# #     chose_level()
# #     screen.blit(screen, (0, 0))
# #     pygame.display.flip()
# # pygame.quit()