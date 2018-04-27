import pygame
from Ajustes import *

vec = pygame.math.Vector2
class jugador(pygame.sprite.Sprite):
    def __init__(self, Juego):
        pygame.sprite.Sprite.__init__(self)
        self.juego = Juego
        self.image = pygame.Surface((30, 40))
        self.image.fill(azul)
        self.rect = self.image.get_rect()
        self.rect.center = (ancho/2,largo/2)
        self.pos = vec(ancho / 2, largo / 2)
        self.vel = vec(0, 0)
        self.ace = vec(0, 0)

    def saltar(self):
        #saltar solo si esta sobre algo
        self.rect.x += 1
        contacto = pygame.sprite.spritecollide(self, self.juego.plataformas, False)
        self.rect.x -= 1
        if contacto:
            self.vel.y = -20

    def update(self,*args):
        self.ace= vec(0, Jugador_GRAV)
        teclado = pygame.key.get_pressed()
        if teclado[pygame.K_LEFT]:
            self.ace.x = -Jugador_ACE
        if teclado[pygame.K_RIGHT]:
            self.ace.x = Jugador_ACE

        self.ace.x += self.vel.x * Jugador_FRICCION
        self.vel += self.ace
        self.pos += self.vel + 0.5 * self.ace

        self.rect.center = self.pos

        if self.pos.x > ancho:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = ancho
        #if self.pos.y > largo:
            #self.pos.y = 0


        self.rect.midbottom = self.pos

class Plataformas(pygame.sprite.Sprite):
    def __init__(self, x, y, a, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((a, h))
        self.image.fill(verde)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

