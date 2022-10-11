from Entity import Entity
import pygame

from globals import Globals


class Portal(Entity):
    def __init__(self, x, y, ID) -> None:
        self.ID = ID
        self.type = "portal"
        self.pos = pygame.Vector2(x, y)
        if self.ID == 0:
            self.picture = pygame.image.load("textures\\Portal1.png")
            self.picture = pygame.transform.scale(
                self.picture, (Globals.sizeofEverything, Globals.sizeofEverything)
            )
        if self.ID == 1:
            self.picture = pygame.image.load("textures\\Portal2.png")
            self.picture = pygame.transform.scale(
                self.picture, (Globals.sizeofEverything, Globals.sizeofEverything)
            )
        self.hp = 20

    def reScale(self):
        if self.ID == 0:
            self.picture = pygame.image.load("textures\\Portal1.png")
            self.picture = pygame.transform.scale(
                self.picture, (Globals.sizeofEverything, Globals.sizeofEverything)
            )
        if self.ID == 1:
            self.picture = pygame.image.load("textures\\Portal2.png")
            self.picture = pygame.transform.scale(
                self.picture, (Globals.sizeofEverything, Globals.sizeofEverything)
            )

    def Update(self):
        return super().Update()

    def Draw(self, window, cameraOffset):
        return super().Draw(self.picture, window, cameraOffset)

    def OnCollide(self, other):
        if other.type == "player":
            if other.portalCD <= 0:
                other.pos = Globals.portalList[self.ID - 1].pos
                other.portalCD = 250
                other.cameraOffset.x -= (
                    Globals.portalList[self.ID].pos.x
                    - Globals.portalList[self.ID - 1].pos.x
                )
                other.cameraOffset.y -= (
                    Globals.portalList[self.ID].pos.y
                    - Globals.portalList[self.ID - 1].pos.y
                )
        return super().OnCollide(other)
