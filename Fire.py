import pygame
from Entity import Entity
import random


class Fire(Entity):
    picture = None

    def __init__(self, pos, generation) -> None:
        super().__init__(pos)
        self.dmg = 2
        self.randy = random
        randy = random
        self.hp = randy.randint(30, 150)
        self.randomSpread = 10
        self.generation = generation
        if Fire.picture == None:
            Fire.picture = pygame.image.load("Textures\\Fire.png")
            Fire.picture = pygame.transform.scale(Fire.picture, (100, 100))

    def Update(self):
        # if self.randy.randint(1,100) == self.randomSpread():
        self.hp -= 1
        return super().Update()

    def OnCollide(self, other):
        other.takeDamage(self.dmg)

    def Draw(self, window, cameraOffset):
        return super().Draw(Fire.picture, window, cameraOffset)
