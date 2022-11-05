from Entity import Entity
import pygame
from Enemy1 import Enemy1
import random
import CheatFile
from globals import Globals


class EnemySpawner(Entity):
    sizeofEverything = Globals.sizeofEverything
    picture = pygame.image.load("textures\\EnemySorcerer.png")
    picture = pygame.transform.scale(
        picture, (Globals.sizeofEverything, Globals.sizeofEverything)
    )
    originalPic = picture
    originalPictures = [picture]
    pictures = [picture]

    def __init__(self, pos, isPassable, addEntity) -> None:
        self.addEntity = addEntity
        self.isPassable = isPassable
        self.cooldown = 100
        self.movementCooldown = 100
        super().__init__(pos)
        self.picture = pygame.image.load("textures\\EnemySorcerer.png")
        self.picture = pygame.transform.scale(
            self.picture, (Globals.sizeofEverything, Globals.sizeofEverything)
        )

    def Draw(self, window, cameraOffset):
        return super().Draw(EnemySpawner.pictures[0], window, cameraOffset)

    def reScale(self):
        self.picture = pygame.image.load("textures\\EnemySorcerer.png")
        self.picture = pygame.transform.scale(
            self.picture, (Globals.sizeofEverything, Globals.sizeofEverything)
        )

    def Update(self):
        if self.hp > 0:
            self.Movement()
            if self.cooldown <= 0:
                self.Summon()
        self.cooldown -= 1
        self.movementCooldown -= 1
        return super().Update()

    def Summon(self):
        pos2 = [0, 0]
        r = random.SystemRandom()
        direct = r.randint(1, 4)
        # print("entered")
        if direct == 1:
            pos2 = [self.pos.x - 1, self.pos.y]
        if direct == 2:
            pos2 = [self.pos.x + 1, self.pos.y]
        if direct == 3:
            pos2 = [self.pos.x, self.pos.y - 1]
        if direct == 4:
            pos2 = [self.pos.x, self.pos.y + 1]
        if self.isPassable(int(pos2[0]), int(pos2[1])):
            self.addEntity(
                Enemy1(pygame.Vector2(int(pos2[0]), int(pos2[1])), self.isPassable),
                1,
            )
            self.cooldown = 600

    def Movement(self):
        pos2 = [0, 0]
        r = random.SystemRandom()
        direct = r.randint(1, 4)
        if self.movementCooldown <= 0:
            # print("entered")
            if direct == 1:
                pos2 = [self.pos.x - 1, self.pos.y]
            if direct == 2:
                pos2 = [self.pos.x + 1, self.pos.y]
            if direct == 3:
                pos2 = [self.pos.x, self.pos.y - 1]
            if direct == 4:
                pos2 = [self.pos.x, self.pos.y + 1]
            if self.isPassable(int(pos2[0]), int(pos2[1])):
                self.pos = pygame.Vector2(pos2[0], pos2[1])
                self.movementCooldown = 100

    def OnCollide(self, other):
        return super().OnCollide(other)
