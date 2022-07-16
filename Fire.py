import pygame
from Entity import Entity


class Fire(Entity):
    picture = None

    def __init__(
        self,
        pos,
    ) -> None:
        super().__init__(pos)
        self.dmg = 2

        if Fire.picture == None:
            Fire.picture = pygame.image.load("Textures\\Fire.png")
            Fire.picture = pygame.transform.scale(Fire.picture, (100, 100))

    def Update(self):
        return super().Update()

    def OnCollide(self, other):
        other.takeDamage(self.dmg)

    def Draw(self, window, cameraOffset):
        return super().Draw(Fire.picture, window, cameraOffset)
