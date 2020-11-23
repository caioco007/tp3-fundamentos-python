import pygame

pygame.init()
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

#circle
posx = 400

terminou = False
while not terminou:

    # Atualiza o desenho na tela
    pygame.display.update()

    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

    posx -= -0.1

    if posx <= 0:
        posx = 800

    if posx >= 800:
        posx = 0

    tela.fill((0, 0, 0))

    # desenha o quadrado em sua nova posição
    pygame.draw.circle(tela, (0, 255, 0), (posx, 300), 100)

# Finaliza a janela do jogo
pygame.display.quit()
# Finaliza o pygame
pygame.quit()