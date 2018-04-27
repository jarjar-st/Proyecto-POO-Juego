
import pygame
import random
from Ajustes import *
from Sprites import *


class Juego:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.pantalla = pygame.display.set_mode((ancho, largo))
        pygame.display.set_caption(titulo)
        self.reloj1 = pygame.time.Clock()
        self.running = True

    def nuevo_juego(self):
        self.Pijazo_Sprites = pygame.sprite.Group()
        self.plataformas = pygame.sprite.Group()
        self.jugador = jugador(self)
        self.Pijazo_Sprites.add(self.jugador)
        for plat in Lista_Plataformas:
            p = Plataformas(*plat)
            self.Pijazo_Sprites.add(p)
            self.plataformas.add(p)
        self.run()

    def run(self):
        self.jugando=True
        while self.jugando:
            self.reloj1.tick(FPS)
            self.eventos()
            self.update()
            self.dibujar()

    def update(self):
        self.Pijazo_Sprites.update()
        #Comprueba si se toca alguna plataforma solo si cae
        if self.jugador.vel.y > 0:
            contacto = pygame.sprite.spritecollide(self.jugador, self.plataformas, False)
            if contacto:
                self.jugador.pos.y = contacto[0].rect.top+1
                self.jugador.vel.y = 0

    def eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jugando:
                    self.jugando=False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.jugador.saltar()

    def dibujar(self):
        self.pantalla.fill(negro)
        self.Pijazo_Sprites.draw(self.pantalla)
        pygame.display.flip()

    def mostrar_pantalla_inicio(self):
        pass

    def mostrar_pantalla_go(self):
        pass

j=Juego()
j.mostrar_pantalla_inicio()
while j.running:
    j.nuevo_juego()
    j.mostrar_pantalla_go()
pygame.quit()