import pygame
from Entity import Entity
from globals import Globals
from globals import Textures


class Chest(Entity):
    sizeofEverything = Globals.sizeofEverything
    Chest1 = Textures.chest1
    OpenedChest1 = Textures.openedChest1
    Chest1 = pygame.transform.scale(Chest1, (sizeofEverything, sizeofEverything))
    OpenedChest1 = pygame.transform.scale(
        OpenedChest1, (sizeofEverything, sizeofEverything)
    )
    picture = Chest1
    originalPic = Chest1
    originalPic2 = OpenedChest1
    pictures = [Chest1, OpenedChest1]
    originalPictures = [Chest1, OpenedChest1]

    def __init__(self, x, y) -> None:
        pos = pygame.Vector2(x, y)
        super().__init__(pos)
        self.interacted = 0
        self.type = "entity"
        self.name = "chest"
        self.Chest1 = pygame.transform.scale(
            self.Chest1, (Globals.sizeofEverything, Globals.sizeofEverything)
        )
        self.OpenedChest1 = pygame.transform.scale(
            self.OpenedChest1, (Globals.sizeofEverything, Globals.sizeofEverything)
        )

    def reScale(self):
        self.Chest1 = Textures.chest1
        self.OpenedChest1 = Textures.openedChest1
        self.Chest1 = pygame.transform.scale(
            self.Chest1, (Globals.sizeofEverything, Globals.sizeofEverything)
        )
        self.OpenedChest1 = pygame.transform.scale(
            self.OpenedChest1, (Globals.sizeofEverything, Globals.sizeofEverything)
        )

    def Activate(self):
        return super().Activate()

    def Update(self):
        return super().Update()

    def Draw(self, window, cameraOffset):
        self.picture = self.pictures[0]
        if self.interacted == 1:
            self.picture = self.pictures[1]
        return super().Draw(self.picture, window, cameraOffset)

    def OnCollide(self, other):
        if other.name == "player":
            self.interacted = 1
        else:
            pass
        # return super().OnCollide(other)
