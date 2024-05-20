import pygame
from objects import Planet, Spacecraft
from values import *

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A New World")
FONT = pygame.font.SysFont("comicsans", 16)
LOGO = pygame.image.load('graphics/logo.png')
pygame.display.set_icon(LOGO)


def main():
    run = True
    clock = pygame.time.Clock()

    earth = Planet(0, 0, 100, BLUE, 1.98892 * 10 ** 30)
    earth.orbited = True

    moon = Planet(-1.524 * Planet.AU, 0, 16, WHITE, 5.9742 * 10 ** 24)
    moon.y_vel = 24.077 * 1000

    spacecraft1 = Spacecraft(-1 * Spacecraft.AU, 0, 1000)
    spacecraft1.y_vel = 29.783 * 1000

    objects = [earth,moon, spacecraft1]

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