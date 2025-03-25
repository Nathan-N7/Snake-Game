import pygame
import time
from pygame.locals import *

WINDOWS_WIDTH = 600
WINDOWS_HEIGHT = 600
posix_x = WINDOWS_WIDTH / 2
posix_y = WINDOWS_HEIGHT / 2
BLOCK = 15
direcao = K_UP

pygame.init()

window = pygame.display.set_mode((WINDOWS_HEIGHT, WINDOWS_WIDTH))
posix_snake = [(posix_x, posix_y)]
surface_snake = pygame.Surface((BLOCK, BLOCK))

game_over_cor = (255, 0, 0)
fonte_gm_ov = pygame.font.SysFont('comicsansms', 72)
def game_over():
    text = fonte_gm_ov.render("GAME OVER", True, game_over_cor)
    texto_rect = text.get_rect(center=(WINDOWS_WIDTH // 2, WINDOWS_HEIGHT // 2))
    window.blit(text, texto_rect)
    pygame.display.update()

def verify_img(posix):
    if 0 <= posix[0] < WINDOWS_WIDTH and 0 <= posix[1] < WINDOWS_HEIGHT:
        return False
    else:
        return True

while True:
    pygame.time.Clock().tick(5)
    window.fill((68, 189, 50))

    for evento in pygame.event.get():
        if evento.type  == QUIT:
            pygame.quit()
            quit()
        elif evento.type == KEYDOWN:
            if evento.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                direcao = evento.key

    for posix in posix_snake:
        window.blit(surface_snake, posix)
    
    if verify_img(posix_snake[0]):
        game_over()
        time.sleep(1)
        pygame.quit()
        quit()

    if direcao == K_RIGHT:
        posix_snake[0] = posix_snake[0][0] + BLOCK, posix_snake[0][1]
    elif direcao == K_LEFT:
        posix_snake[0] = posix_snake[0][0] - BLOCK, posix_snake[0][1]
    elif direcao == K_UP:
        posix_snake[0] = posix_snake[0][0], posix_snake[0][1] - BLOCK
    elif direcao == K_DOWN:
        posix_snake[0] = posix_snake[0][0], posix_snake[0][1] + BLOCK
    
    pygame.display.update()