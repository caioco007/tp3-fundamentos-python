import pygame, sys
from pygame.locals import *

# CONSTANTES
# Constantes que vamos usar para o tamanho da tela
LARGURA_TELA = 800
ALTURA_TELA = 600
# Será utilizado para a velocidade do jogo
FPS = 200
# Valores para o desenho das paletas e do fundo
LARGURA_LINHA =50

# cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Função para desenhar a bola
def desenhaBola(bola):
    pygame.draw.circle(DISPLAYSURF, (0, 255, 0), (bola.x, bola.y), 100)

# altera a direção da bola e retorna ela
def moveBola(bola, bolaDirX, bolaDirY):
    bola.x += bolaDirX
    bola.y += bolaDirY
    return bola

# Verifica por colisão com as bordas
def verificaColisao(bola, bolaDirX):
    if bola.left == (LARGURA_LINHA) or bola.right == (LARGURA_TELA - LARGURA_LINHA):
        bolaDirX = bolaDirX * -1
    return bolaDirX


# Função principal
def main():
    pygame.init()
    global BASICFONT, BASICFONTSIZE
    BASICFONTSIZE = 20
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    global DISPLAYSURF

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('PongNet')

    # Iniciando as variáveis nas posições iniciais
    # Estas variáveis serão alteradas ao longo da execução
    bolaX = LARGURA_TELA // 2 - LARGURA_LINHA // 2
    bolaY = ALTURA_TELA // 2 - LARGURA_LINHA // 2

    # altera a posição da bola
    bolaDirX = +1
    bolaDirY = 0

    # Criando os retangulos para a bola e paletas.
    bola = pygame.Rect(bolaX, bolaY, LARGURA_LINHA, LARGURA_LINHA)

    # Desenhando as posições iniciais da Arena
    DISPLAYSURF.fill(PRETO)
    desenhaBola(bola)

    pygame.mouse.set_visible(0)
    while True:  # Loop principal
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        DISPLAYSURF.fill(PRETO)
        desenhaBola(bola)

        bola = moveBola(bola, bolaDirX, bolaDirY)
        bolaDirX= verificaColisao(bola, bolaDirX)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
