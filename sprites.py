import pygame as pg
from settings import *
from tilemap import collide_hit_rect
import sys
import random
vec = pg.math.Vector2

pg.mixer.init()
choice = random.choice(['1.wav', '2.wav', '3.wav', '4.wav', '5.wav',
                           '6.wav', '7.wav', '8.wav', '9.wav'])
explosion = pg.mixer.Sound('snd/explosions/' + choice)

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load('img/spaceship.png')
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE
        self.rot = 0
        self.boom = False

    def get_keys(self):
        self.rot_speed = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rot_speed = PLAYER_ROT_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rot_speed = -PLAYER_ROT_SPEED
        if keys[pg.K_SPACE] or keys[pg.K_w] or keys[pg.K_UP]:
            self.vel += vec(PLAYER_THRUST, 0).rotate(-self.rot)

        for event in pg.event.get():

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.game.channelfire.play(self.game.fire, loops=-1)
                    self.animate('fire')
                if event.key == pg.K_UP:
                    self.game.channelfire.play(self.game.fire, loops=-1)
                    self.animate('fire')
                if event.key == pg.K_w:
                    self.game.channelfire.play(self.game.fire, loops=-1)
                    self.animate('fire')
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    self.game.channelfire.stop()
                if event.key == pg.K_UP:
                    self.game.channelfire.stop()
                if event.key == pg.K_w:
                    self.game.channelfire.stop()

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if abs(self.vel.x) < abs(350):
                    self.pos.x = hits[0].rect.left - self.hit_rect.width / 2.0
                    self.vel.x = 0
                    self.vel.y = 0
                    self.hit_rect.centerx = self.pos.x
                else:
                    self.explode()
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if abs(self.vel.y) < abs(350):
                    self.pos.y = hits[0].rect.top - self.hit_rect.height / 2.0
                    self.vel.y = 0
                    self.vel.x = 0
                    self.hit_rect.centery = self.pos.y
                else:
                    self.explode()



    def explode(self):
        self.boom = True
        self.kill()
        pg.mixer.Sound.play(explosion)

    def animate(self, type):
        if type == 'fire':
            self.image = pg.image.load('img/spaceship2.png')
        else:
            self.image = pg.image.load('img/spaceship.png')




    def update(self):
        self.get_keys()
        if abs(self.vel.x) < abs(400) and abs(self.vel.y) < abs(400):
            self.vel += (0, 0)
        self.rot = (self.rot + self.rot_speed * self.game.dt) % 360
        self.image = pg.transform.rotate(self.game.player_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        self.collide_with_walls('x')
        self.hit_rect.centery = self.pos.y
        self.collide_with_walls('y')
        self.rect.center = self.hit_rect.center


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

