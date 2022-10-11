import pygame
from Entity import Entity
from Player import Player
import globals


class MapDoor(Entity):
    mainMap = 0

    def __init__(self, x, y, switchTo):
        self.switchTo = switchTo
        self.pos = pygame.Vector2(x, y)
        self.hp = 1000000000
        self.picture = pygame.image.load("textures\\ClosedDoor.png")

    def OnCollide(self, other):
        if type(other) == Player:
            self.mainMap = self.switchTo
            globals.Globals.currentMap = self.switchTo
            if self.switchTo == 1:
                other.pos.x = 1
                other.pos.y = 4
                other.cameraOffset.x -= 67
            if self.switchTo == 0:
                other.pos.x = 67
                other.pos.y = 4
                other.cameraOffset.x += 67
        return super().OnCollide(other)

    def Update(self):
        return super().Update()

    def reScale(self):
        self.picture = pygame.image.load("textures\\ClosedDoor.png")
        self.picture = pygame.transform.scale(
            self.picture,
            (globals.Globals.sizeofEverything, globals.Globals.sizeofEverything),
        )

    def Draw(self, window, cameraOffset):
        return super().Draw(self.picture, window, cameraOffset)
