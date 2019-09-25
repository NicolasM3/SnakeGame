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
morreu = False

pygame.init()

tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

while True:

    #  cobrinha
    cobrinha = [(200, 200), (210, 200), (220, 200)]
    cobrinhaCor = pygame.Surface((10,10))
    cobrinhaCor.fill((0, 0, 255))
    direcao = ESQUERDA

    #  maça
    maca = pygame.Surface((10,10))
    maca.fill((255, 0, 0))
    macaPosicao = (random_grid()) 

    clock = pygame.time.Clock()
  
    while True:
        clock.tick(20)
        #  eventos
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

                elif (event.key == K_n):
                    for i in range(0, 10):
                        cobrinha.append((0, 0))
                    

        #  gerando posições
        tela.fill((0, 0, 0))
        tela.blit(maca, macaPosicao)
        
        #  desenhando a cobrinha
        for i in cobrinha:
            tela.blit(cobrinhaCor, i)

        #  verificando colisão com a maça
        if colisao(cobrinha[0], macaPosicao) == True:
            macaPosicao = random_grid()
            cobrinha.append((0, 0))

        #  verificando colisão com a parede
        if ((cobrinha[0][0] == -10) or (cobrinha[0][0] == 600) or (cobrinha[0][1] == 600) or (cobrinha[0][1] == -10)):
            morreu = True

        #  verificando colisão com a cobra
        for i in range(2, len(cobrinha)):
            if(cobrinha[0] == cobrinha[i]):
                morreu = True

        #  mudando a direção da cabeça da cobra
        if direcao == CIMA:
            cobrinha[0] = (cobrinha[0][0], cobrinha[0][1] - 10)
        elif direcao == BAIXO:
            cobrinha[0] = (cobrinha[0][0], cobrinha[0][1] + 10)
        elif direcao == ESQUERDA:
            cobrinha[0] = (cobrinha[0][0] - 10, cobrinha[0][1])
        elif direcao == DIREITA:
            cobrinha[0] = (cobrinha[0][0] + 10, cobrinha[0][1])

        '''for i in range(len(cobrinha) - 1, 1, -1):
            if (cobrinha[0][0] == cobrinha[i][0]) and (cobrinha[0][1] == cobrinha[1][1]):
                break'''

        #  reposicionando a ultima parte para o sucessor
        for i in range(len(cobrinha) - 1, 0, -1):
            cobrinha[i] = (cobrinha[i - 1][0], cobrinha[i - 1][1])
        
        if(morreu):
            print("Morreu")
            break

        #  atualiza o display
        pygame.display.update()
