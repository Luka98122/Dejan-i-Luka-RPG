import pygame
from DialogueSystem import DialogueSystem
from Entity import Entity
from Player import Player
from TextWindow import TextWindow
from globals import Globals

dialogueSystem = DialogueSystem


def myFunction(actionParams: dict):
    Globals.entityList[actionParams["reciever"]].hp += actionParams["health"]


class NPC(Entity):
    merchant1 = pygame.image.load("Textures\\merchant1.png")
    originalPictures = [merchant1]
    pictures = [merchant1]

    ICON_Merchant1 = pygame.image.load("textures\\ICONS\\Merchant1ICON.png")
    ICON_Merchant1 = pygame.transform.scale(ICON_Merchant1, (120, 120))

    ICON_Unkown = pygame.image.load("textures\\ICONS\\UnknownICON.png")
    ICON_Unkown = pygame.transform.scale(ICON_Unkown, (120, 120))
    type = "npc"

    def __init__(self, pos, id, texts, isPassable) -> None:
        self.pos = pos
        self.isPassable = isPassable
        self.hp = 200
        self.texts = texts
        self.id = id
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
        if (
            type(other) == Player
            and self.collisonCooldown < 0
            and self.id == "merchant1"
        ):
            pos1 = pygame.Vector2(50, 1000)
            if self.id == "merchant1":
                self.window.blit(
                    self.ICON_Merchant1,
                    pygame.Rect(pos1.x, pos1.y - len(self.texts) * 100, 120, 120),
                )

            if self.id == "unknown":
                self.window.blit(
                    self.ICON_Unkown,
                    pygame.Rect(pos1.x, pos1.y - len(self.texts) * 100, 120, 120),
                )
            dialogueSystem.addWindow(
                self,
                pygame.Vector2(50, 1000),
                self.texts[0],
                [5, 150],
                action=myFunction,
                actionParams={"health": 10, "reciever": 0},
            )
            dialogueSystem.addWindow(
                self,
                pygame.Vector2(50, 900),
                self.texts[1],
                [5, 150],
                action=myFunction,
                actionParams={"health": -10, "reciever": 0},
            )
            DialogueSystem.pairs.append([])
            DialogueSystem.pairs[-1].append(DialogueSystem.listOfTextWindows[-1])
            DialogueSystem.pairs[-1].append(DialogueSystem.listOfTextWindows[-2])
            self.collisonCooldown = 100
        return super().OnCollide(other)
