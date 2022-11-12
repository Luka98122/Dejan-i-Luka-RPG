import pygame
from DialogueSystem import DialogueSystem
from Entity import Entity
from Player import Player

dialogueSystem = DialogueSystem


class NPC(Entity):
    merchant1 = pygame.image.load("Textures\\merchant1.png")
    originalPictures = [merchant1]
    pictures = [merchant1]

    def __init__(self, pos, texts, isPassable) -> None:
        self.pos = pos
        self.isPassable = isPassable
        self.hp = 200
        self.texts = texts
        self.collisonCooldown = 200

    def Draw(self, window, cameraOffset):
        picture = NPC.pictures[0]
        self.window = window
        return super().Draw(picture, window, cameraOffset)

    def Update(self):
        self.collisonCooldown -= 1

    def takeDamage(self, damage):
        return super().takeDamage(damage)

    def OnCollide(self, other):
        if type(other) == Player and self.collisonCooldown < 0:
            dialogueSystem.addWindow(
                self, pygame.Vector2(50, 500), self.texts[0], [5, 150], "merchant1"
            )
            self.collisonCooldown = 200
        return super().OnCollide(other)
