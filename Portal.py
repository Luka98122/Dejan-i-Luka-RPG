from Entity import Entity
import pygame

from globals import Globals
from globals import Textures


class Portal(Entity):
    portal1 = pygame.image.load("textures\\Portal1.png")
    portal1 = pygame.transform.scale(
        portal1, (Globals.sizeofEverything, Globals.sizeofEverything)
    )
    portal2 = pygame.image.load("textures\\Portal2.png")
    portal2 = pygame.transform.scale(
        portal2, (Globals.sizeofEverything, Globals.sizeofEverything)
    )
    originalPic = portal1
    originalPic2 = portal2
    originalPictures = [portal1, portal2]
    pictures = [portal1, portal2]

    def __init__(self, x, y, ID) -> None:
        self.ID = ID
        self.type = "entity"
        self.name = "portal"
        self.pos = pygame.Vector2(x, y)
        if self.ID == 0:
            self.picture = Portal.portal1
            self.picture = pygame.transform.scale(
                self.picture, (Globals.sizeofEverything, Globals.sizeofEverything)
            )
        if self.ID == 1:
            self.picture = Portal.portal2
            self.picture = pygame.transform.scale(
                self.picture, (Globals.sizeofEverything, Globals.sizeofEverything)
            )
        self.hp = 20

    picture = portal1

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
        self.picture = Portal.pictures[0]
        if self.ID == 1:
            self.picture = Portal.pictures[1]
        return super().Draw(self.picture, window, cameraOffset)

    def OnCollide(self, other):
        if other.name == "player":
            if other.portalCD <= 0:
                if Globals.portalList[self.ID - 1] != 0:
                    other.pos = Globals.portalList[self.ID - 1].pos.copy()
                    other.portalCD = 250
                    other.cameraOffset.x -= (
                        Globals.portalList[self.ID].pos.x
                        - Globals.portalList[self.ID - 1].pos.x
                    )
                    other.cameraOffset.y -= (
                        Globals.portalList[self.ID].pos.y
                        - Globals.portalList[self.ID - 1].pos.y
                    )
                    print("moved")

        return super().OnCollide(other)
