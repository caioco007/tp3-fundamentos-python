import pygame

pygame.init()
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

quadrado = pygame.Rect(350,250,100,100)

terminou = False
while not terminou:

    # Atualiza o desenho na tela
    pygame.display.update()

    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                quadrado.move_ip(10, 0)
            if event.key == pygame.K_LEFT:
                quadrado.move_ip(-10, 0)
            if event.key == pygame.K_UP:
                quadrado.move_ip(0, -10)
            if event.key == pygame.K_DOWN:
                quadrado.move_ip(0, 10)

    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, (255, 0, 0), quadrado)

# Finaliza a janela do jogo
pygame.display.quit()
# Finaliza o pygame
pygame.quit()