import pygame
from Entity import Entity


class Chest(Entity):
    Chest1 = pygame.image.load("textures\\Chest1.png")
    OpenedChest1 = pygame.image.load("textures\\OpenedChest1.png")
    Chest1 = pygame.transform.scale(Chest1, (100, 100))
    OpenedChest1 = pygame.transform.scale(OpenedChest1, (100, 100))

    def __init__(self, x, y) -> None:
        pos = pygame.Vector2(x, y)
        super().__init__(pos)
        self.interacted = 0
        self.type = "chest"

    def Activate(self):
        return super().Activate()

    def Update(self):
        return super().Update()

    def Draw(self, window, cameraOffset):
        picture = self.Chest1
        if self.interacted == 1:
            picture = self.OpenedChest1
        return super().Draw(picture, window, cameraOffset)

    def OnCollide(self, other):
        if other.type == "player":
            self.interacted = 1
        else:
            pass
        # return super().OnCollide(other)
