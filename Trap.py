import pygame
from Entity import Entity
from Enemy1 import Enemy1


class Trap(Entity):
    explosiveBarrel = pygame.image.load("textures\\ExplosiveBarrel.png")
    oilSpill = pygame.image.load("textures\\OilSpill.png")
    explosiveBarrel = pygame.transform.scale(explosiveBarrel, (100, 100))
    oilSpill = pygame.transform.scale(oilSpill, (100, 100))
    type = "trap"

    def __init__(self, x, y) -> None:
        pos = pygame.Vector2(x, y)
        super().__init__(pos)
        self.damage = 20
        self.interacted = 0
        self.type = "trap"

    def Activate(self):
        return super().Activate()

    def Update(self):
        self.Activate()
        return super().Update()

    def Draw(self, window, cameraOffset):
        picture = self.explosiveBarrel
        if self.interacted == 1:
            picture = self.oilSpill
        return super().Draw(picture, window, cameraOffset)

    def OnCollide(self, other):
        if self.interacted == 0:
            other.takeDamage(self.damage)
            self.interacted = 1
        # return super().OnCollide(other)
