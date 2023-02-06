import pygame
from objects import Object
from values import *

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A New World")
FONT = pygame.font.SysFont("comicsans", 16)


def main():
    run = True
    clock = pygame.time.Clock()

    sun = Object(0, 0, 30, YELLOW, 1.98892 * 10 ** 30)
    sun.sun = True

    earth = Object(-1 * Object.AU, 0, 16, BLUE, 5.9742 * 10 ** 24)
    earth.y_vel = 29.783 * 1000

    spacecraft1 = Object(-1.524 * Object.AU, 0, 5, DARK_GREY, 1000)
    spacecraft1.y_vel = 24.077 * 1000
    spacecraft1.spacecraft = True

    objects = [sun, earth, spacecraft1]

    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for object in objects:
            object.update(objects)
            object.draw(WIN)

        pygame.display.update()

    pygame.quit()


main()