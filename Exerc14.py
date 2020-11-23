import pygame

pygame.init()
largura_tela = 800
altura_tela = 600
velocidade = 10
tela = pygame.display.set_mode((largura_tela, altura_tela))

#circle
posx = 400
posy = 300
terminou = False
while not terminou:

    # Atualiza o desenho na tela
    pygame.display.update()

    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            (posx, posy) = pygame.mouse.get_pos()


    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, (255, 255, 0), (posx,posy,50,50))


# Finaliza a janela do jogo
pygame.display.quit()
# Finaliza o pygame
pygame.quit()