from Entity import Entity
import pygame
import CheatFile
from globals import Globals


class Door(Entity):
    sizeofEverything = Globals.sizeofEverything
    ClosedDoor = pygame.image.load("textures\\ClosedDoor.png")
    OpenedDoor = pygame.image.load("textures\\OpenedDoor.png")
    ClosedDoor = pygame.transform.scale(
        ClosedDoor, (sizeofEverything, sizeofEverything)
    )
    OpenedDoor = pygame.transform.scale(
        OpenedDoor, (sizeofEverything, sizeofEverything)
    )

    def __init__(self, x, y) -> None:
        pos = pygame.Vector2(x, y)
        super().__init__(pos)
        self.interacted = 0
        self.ClosedDoor = pygame.image.load("textures\\ClosedDoor.png")
        self.OpenedDoor = pygame.image.load("textures\\OpenedDoor.png")
        self.ClosedDoor = pygame.transform.scale(
            self.ClosedDoor, (Globals.sizeofEverything, Globals.sizeofEverything)
        )
        self.OpenedDoor = pygame.transform.scale(
            self.OpenedDoor, (Globals.sizeofEverything, Globals.sizeofEverything)
        )

    def reScale(self):
        self.ClosedDoor = pygame.image.load("textures\\ClosedDoor.png")
        self.OpenedDoor = pygame.image.load("textures\\OpenedDoor.png")
        self.ClosedDoor = pygame.transform.scale(
            self.ClosedDoor, (Globals.sizeofEverything, Globals.sizeofEverything)
        )
        self.OpenedDoor = pygame.transform.scale(
            self.OpenedDoor, (Globals.sizeofEverything, Globals.sizeofEverything)
        )

    def Draw(self, window, cameraOffset):
        slika = self.ClosedDoor
        if self.interacted == 1:
            slika = self.OpenedDoor
        return super().Draw(slika, window, cameraOffset)

    def OnCollide(self, other):
        pass
