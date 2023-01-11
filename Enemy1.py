import pygame
from Entity import Entity
import random
from Door import Door
from globals import Globals
from globals import Textures


class Enemy1(Entity):
    sizeofEverything = Globals.sizeofEverything
    picture = Textures.enemy1
    picture = pygame.transform.scale(
        picture, (Globals.sizeofEverything, Globals.sizeofEverything)
    )
    originalPic = picture
    originalPictures = [picture]
    pictures = [picture]

    def __init__(self, pos, isPassable) -> None:
        super().__init__(pos)
        self.hp = 20
        self.pos = pygame.Vector2(pos[0], pos[1])
        self.alive = 1
        self.type = "entity"
        self.name = "enemy1"
        self.movementCooldown = 100
        self.isPassable = isPassable
        self.picture = Textures.enemy1
        self.picture = pygame.transform.scale(
            self.picture, (Globals.sizeofEverything, Globals.sizeofEverything)
        )

    def Update(self):
        # return super().Update()
        if self.hp > 0:
            self.Movement()

    def reScale(self):
        self.picture = Textures.enemy1
        self.picture = pygame.transform.scale(
            self.picture, (Globals.sizeofEverything, Globals.sizeofEverything)
        )

    def Draw(self, window, cameraOffset):
        picture = Enemy1.pictures[0]
        if self.hp > 0:
            return super().Draw(
                picture,
                window,
                cameraOffset,
            )

    def Movement(self):
        self.movementCooldown -= 1
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

    def takeDamage(self, damage):
        return super().takeDamage(damage)

    def OnCollide(self, other):
        if isinstance(other, Door):
            other.interacted = 1
