import pygame

pygame.init()
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

#circle
posx = 400
posy = 300

posx_c = 0
posy_c = 0

clock = pygame.time.Clock()

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
                posx_c = 10
                posy_c = 0
            elif event.key == pygame.K_LEFT:
                posx_c = -10
                posy_c = 0
            elif event.key == pygame.K_UP:
                posx_c = 0
                posy_c = -10
            elif event.key == pygame.K_DOWN:
                posx_c = 0
                posy_c = 10


    posx+=posx_c
    posy+=posy_c

    if posx <= 0:
        posx = 800

    elif posx >= 800:
        posx = 0

    if posy <= 0:
        posy = 600

    elif posy >= 600:
        posy = 0

    tela.fill((0, 0, 0))
    pygame.draw.circle(tela, (255, 255, 0), (posx, posy), 100)

    clock.tick(30)

# Finaliza a janela do jogo
pygame.display.quit()
# Finaliza o pygame
pygame.quit()