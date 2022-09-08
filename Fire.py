import pygame
from Entity import Entity
import random
import CheatFile
from globals import Globals


class Fire(Entity):
    picture = None
    sizeofEverything = Globals.sizeofEverything
    picture = pygame.image.load("Textures\\Fire.png")
    picture = pygame.transform.scale(picture, (sizeofEverything, sizeofEverything))

    def __init__(self, pos, generation) -> None:
        super().__init__(pos)
        self.dmg = 2
        self.randy = random
        randy = random
        self.hp = randy.randint(30, 150)
        self.randomSpread = 10
        self.generation = generation
        self.picture = pygame.image.load("Textures\\Fire.png")
        self.picture = pygame.transform.scale(
            self.picture, (Globals.sizeofEverything, Globals.sizeofEverything)
        )

    def reScale(self):
        self.picture = pygame.image.load("Textures\\Fire.png")
        self.picture = pygame.transform.scale(
            self.picture, (Globals.sizeofEverything, Globals.sizeofEverything)
        )

    def Update(self):
        # if self.randy.randint(1,100) == self.randomSpread():
        self.hp -= 1
        return super().Update()

    def OnCollide(self, other):
        other.takeDamage(self.dmg)

    def Draw(self, window, cameraOffset):
        print(self.picture.get_width())
        return super().Draw(self.picture, window, cameraOffset)
