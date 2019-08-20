from random import randint
import pygame
from pygame.locals import *

def random_grid():
    x = randint(0, 590)
    y = randint(0, 590)

    return(x//10 * 10, y//10 * 10)

def colisao(posicao1, posicao2):
    return((posicao1[0] == posicao2[0]) and posicao1[1] == posicao2[1]) 
    


CIMA = 0
BAIXO = 1
ESQUERDA = 2
DIREITA = 3

pygame.init()

tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

cobrinha = [(200, 200), (210, 200), (220, 200)]
cobrinhaCor = pygame.Surface((10,10))
cobrinhaCor.fill((255, 0, 0))
direcao = ESQUERDA


maca = pygame.Surface((10,10))
maca.fill((255, 255, 255))
macaPosicao = (random_grid()) 

clock = pygame.time.Clock()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if (event.type == KEYDOWN):
            if (event.key == K_UP)  and (direcao != BAIXO):
                direcao = CIMA

            elif (event.key == K_DOWN) and (direcao != CIMA):
                direcao = BAIXO

            elif (event.key == K_RIGHT) and (direcao != ESQUERDA):
                direcao = DIREITA

            elif (event.key == K_LEFT) and (direcao != DIREITA):
                direcao = ESQUERDA

    tela.fill((0, 0, 0))
    tela.blit(maca, macaPosicao)
        
    for i in cobrinha:
        tela.blit(cobrinhaCor, i)

    if colisao(cobrinha[0], macaPosicao) == True:
        macaPosicao = random_grid()
        cobrinha.append((0, 0))

    if direcao == CIMA:
        cobrinha[0] = (cobrinha[0][0], cobrinha[0][1] - 10)
    elif direcao == BAIXO:
        cobrinha[0] = (cobrinha[0][0], cobrinha[0][1] + 10)
    elif direcao == ESQUERDA:
        cobrinha[0] = (cobrinha[0][0] - 10, cobrinha[0][1])
    elif direcao == DIREITA:
        cobrinha[0] = (cobrinha[0][0] + 10, cobrinha[0][1])

    for i in range(len(cobrinha) - 1, 0, -1):
        cobrinha[i] = (cobrinha[i - 1][0], cobrinha[i - 1][1])

    pygame.display.update()
