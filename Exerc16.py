import pygame
import math

pygame.init()
largura_tela = 800
altura_tela = 600
screen = pygame.display.set_mode((largura_tela, altura_tela))
terminou = False

class Polygon():
    def __init__(self):
        self.x, self.y = screen.get_width() // 2, screen.get_height() // 2

    def draw(self):

        num_points = 5
        angulation_constant = 90

        points = []
        for i in range(num_points * 2):
            radius = 100  # Polygon size
            if (
                i % 2 != 0
            ):  # It would be a normal polygon if the normal radius was applied.
                radius = radius // 2
            ang = (i * math.pi / num_points) + (angulation_constant * math.pi / 60)
            x = self.x + int(math.cos(ang) * radius)
            y = self.y + int(math.sin(ang) * radius)
            points.append((x, y))
        pygame.draw.polygon(screen, (255, 255, 0), points)



while not terminou:
    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            estrela = Polygon()
            estrela.draw()



    # Atualiza o desenho na tela
    pygame.display.update()

# Finaliza a janela do jogo
pygame.display.quit()
# Finaliza o pygame
pygame.quit()