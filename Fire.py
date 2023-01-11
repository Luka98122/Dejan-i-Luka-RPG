import pygame
from Entity import Entity
import random
import CheatFile
from globals import Globals
from globals import Textures


class Fire(Entity):
    picture = None
    sizeofEverything = Globals.sizeofEverything
    picture = Textures.fire
    picture = pygame.transform.scale(picture, (sizeofEverything, sizeofEverything))
    originalPic = picture
    originalPictures = [picture]
    pictures = [picture]

    def __init__(self, pos, generation) -> None:
        super().__init__(pos)
        self.dmg = 2
        self.randy = random
        randy = random
        self.hp = randy.randint(30, 150)
        self.randomSpread = 10
        self.generation = generation

    def reScale(self):
        Fire.picture = Textures.fire
        Fire.picture = pygame.transform.scale(
            Fire.picture, (Globals.sizeofEverything, Globals.sizeofEverything)
        )

    def Update(self):
        # if self.randy.randint(1,100) == self.randomSpread():
        self.hp -= 1
        return super().Update()

    def OnCollide(self, other):
        other.takeDamage(self.dmg)

    def Draw(self, window, cameraOffset):
        # print(Fire.picture.get_width())
        return super().Draw(Fire.pictures[0], window, cameraOffset)
