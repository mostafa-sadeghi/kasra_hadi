import pygame

pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
GREEN = (0, 255, 0)
DarkGREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
display_surface = pygame.display.set_mode((WINDOW_WIDTH, \
                                           WINDOW_HEIGHT))
pygame.display.set_caption("Dragon Game")
dragon_left_image = pygame.image.load \
    ("assets/images/dragon_left.png")
dragon_left_image_rect = dragon_left_image.get_rect()
dragon_left_image_rect.topleft = (0, 0)
dragon_right_image = pygame.transform.flip( \
    pygame.image.load("assets/images/dragon_left.png"), \
    True, False)
dragon_right_image_rect = dragon_right_image.get_rect()
dragon_right_image_rect.topright = (WINDOW_WIDTH, 0)

# font = pygame.font.SysFont("arial", 32)
font = pygame.font.Font("assets/fonts/DragonHunter.otf", 48)
title_text = font.render("Dragon Game", True, GREEN, DarkGREEN)
title_text_rect = title_text.get_rect()
title_text_rect.top = 0
title_text_rect.centerx = WINDOW_WIDTH/2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.blit(dragon_left_image, \
                         dragon_left_image_rect)
    display_surface.blit(dragon_right_image, \
                         dragon_right_image_rect)
    display_surface.blit(title_text, title_text_rect)
    pygame.draw.line(display_surface, WHITE, \
                     (0, 128), (WINDOW_WIDTH, 128), 4)
    pygame.display.update()
pygame.quit()
