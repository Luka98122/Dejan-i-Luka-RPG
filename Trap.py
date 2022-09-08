import pygame
from Entity import Entity
from Enemy1 import Enemy1
import CheatFile


class Trap(Entity):
    sizeofEverything = CheatFile.sizeofEverything
    explosiveBarrel = pygame.image.load("textures\\ExplosiveBarrel.png")
    oilSpill = pygame.image.load("textures\\OilSpill.png")
    explosiveBarrel = pygame.transform.scale(
        explosiveBarrel, (sizeofEverything, sizeofEverything)
    )
    oilSpill = pygame.transform.scale(oilSpill, (sizeofEverything, sizeofEverything))
    type = "trap"

    def __init__(self, x, y) -> None:
        pos = pygame.Vector2(x, y)
        super().__init__(pos)
        self.damage = 20
        self.interacted = 0
        self.type = "trap"

    def Activate(self):
        return super().Activate()

    def reScale(self, newSize):
        self.explosiveBarrel = pygame.image.load("textures\\ExplosiveBarrel.png")
        self.oilSpill = pygame.image.load("textures\\OilSpill.png")
        self.explosiveBarrel = pygame.transform.scale(
            self.explosiveBarrel, (newSize, newSize)
        )
        self.oilSpill = pygame.transform.scale(self.oilSpill, (newSize, newSize))

    def Update(self):
        self.Activate()
        return super().Update()

    def Draw(self, window, cameraOffset):
        picture = self.explosiveBarrel
        if self.interacted == 1:
            picture = self.oilSpill
        return super().Draw(
            picture, window, cameraOffset, self.explosiveBarrel.get_width()
        )

    def OnCollide(self, other):
        if self.interacted == 0:
            other.takeDamage(self.damage)
            self.interacted = 1
        # return super().OnCollide(other)
