from Entity import Entity
import pygame
import CheatFile


class Door(Entity):
    sizeofEverything = CheatFile.sizeofEverything
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

    def Draw(self, window, cameraOffset):
        slika = self.ClosedDoor
        if self.interacted == 1:
            slika = self.OpenedDoor
        return super().Draw(slika, window, cameraOffset)

    def OnCollide(self, other):
        pass
