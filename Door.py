from Entity import Entity
import pygame
import CheatFile
from globals import Globals
from globals import Textures


class Door(Entity):
    sizeofEverything = Globals.sizeofEverything
    ClosedDoor = Textures.closedDoor
    OpenedDoor = Textures.openedDoor
    ClosedDoor = pygame.transform.scale(
        ClosedDoor, (sizeofEverything, sizeofEverything)
    )
    OpenedDoor = pygame.transform.scale(
        OpenedDoor, (sizeofEverything, sizeofEverything)
    )
    picture = OpenedDoor
    originalPic = ClosedDoor
    originalPic2 = OpenedDoor
    originalPictures = [OpenedDoor, ClosedDoor]
    pictures = [picture, ClosedDoor]

    def __init__(self, x, y) -> None:
        pos = pygame.Vector2(x, y)
        super().__init__(pos)
        self.interacted = 0
        self.type = "entity"
        self.name = "door"
        self.ClosedDoor = Textures.closedDoor
        self.OpenedDoor = Textures.openedDoor
        self.ClosedDoor = pygame.transform.scale(
            self.ClosedDoor, (Globals.sizeofEverything, Globals.sizeofEverything)
        )
        self.OpenedDoor = pygame.transform.scale(
            self.OpenedDoor, (Globals.sizeofEverything, Globals.sizeofEverything)
        )

    def reScale(self):
        self.ClosedDoor = Textures.closedDoor
        self.OpenedDoor = Textures.openedDoor
        self.ClosedDoor = pygame.transform.scale(
            self.ClosedDoor, (Globals.sizeofEverything, Globals.sizeofEverything)
        )
        self.OpenedDoor = pygame.transform.scale(
            self.OpenedDoor, (Globals.sizeofEverything, Globals.sizeofEverything)
        )

    def Draw(self, window, cameraOffset):
        self.picture = Door.pictures[1]
        if self.interacted == 1:
            self.picture = Door.pictures[0]
        return super().Draw(self.picture, window, cameraOffset)

    def OnCollide(self, other):
        pass
