import pygame
from Chest import Chest
from Entity import Entity
from Fire import Fire
from Door import Door
from HealthPotion import HealthPotion
from Trap import Trap
import CheatFile


class Player(Entity):
    sizeofEverything = 0
    speed = 5
    hp = 100
    movementCooldown = 0
    potionCooldown = 100
    defaultCooldown = 15
    type = "player"
    isPassable = 0
    addEntity = 0
    picture = 0
    bloodpool = 0

    def __init__(self, pos, isPassable, addEntity, cameraOffset) -> None:
        super().__init__(pos)
        self.type = "player"
        self.isPassable = isPassable
        self.addEntity = addEntity
        self.cameraOffset = cameraOffset
        self.sizeofEverything = CheatFile.sizeofEverything
        self.inventory = [
            [HealthPotion(10, self), 1],
            [HealthPotion(10, self), 1],
            [HealthPotion(10, self), 1],
        ]
        self.spellSlot = 1
        self.picture = pygame.image.load("textures\\wizard.png")
        self.picture = pygame.transform.scale(
            self.picture, (self.sizeofEverything, self.sizeofEverything)
        )

        self.bloodpool = pygame.image.load("textures\\BloodPool.png")
        self.bloodpool = pygame.transform.scale(
            self.bloodpool, (self.sizeofEverything, self.sizeofEverything)
        )

    startx = 4  # * sizeofEverything // 100
    starty = 4  # * sizeofEverything // 100
    pos = pygame.Vector2(startx, starty)

    def Heal(self, amount):
        self.hp = self.hp + amount

    def spell1(
        self,
    ):
        mousePos = pygame.mouse.get_pos()
        mousePos = list(mousePos)
        mousePos[0] = mousePos[0] // self.sizeofEverything * self.sizeofEverything
        mousePos[1] = mousePos[1] // self.sizeofEverything * self.sizeofEverything

        # window.blit(
        #    Door.OpenedDoor,
        #    (
        #        mousePos[0] // 100 * 100,
        #        mousePos[1] // 100 * 100,
        #    ),
        # )
        for event in pygame.event.get():
            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1
                and self.isPassable(
                    int(self.pos.x) - 4 + int(mousePos[0]) // self.sizeofEverything,
                    int(self.pos.y) - 4 + int(mousePos[1]) // self.sizeofEverything,
                )
            ):
                self.addEntity(
                    Fire(
                        pygame.Vector2(
                            self.pos.x - 4 + mousePos[0] // self.sizeofEverything,
                            self.pos.y - 4 + mousePos[1] // self.sizeofEverything,
                        ),
                        5,
                    ),
                    1,
                )
                print(
                    self.pos.x - 4 + mousePos[0] // self.sizeofEverything,
                    self.pos.y - 4 + mousePos[1] // self.sizeofEverything,
                    self.cameraOffset,
                )

    def spell2(self):
        mousePos = pygame.mouse.get_pos()
        mousePos = list(mousePos)
        mousePos[0] = mousePos[0] // 100 * 100
        mousePos[1] = mousePos[1] // 100 * 100
        for event in pygame.event.get():
            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1
                and self.isPassable(
                    int(self.pos.x) - 4 + int(mousePos[0]) // 100,
                    int(self.pos.y) - 4 + int(mousePos[1]) // 100,
                )
            ):
                self.addEntity(
                    Trap(
                        self.pos.x - 4 + mousePos[0] // 100,
                        self.pos.y - 4 + mousePos[1] // 100,
                    ),
                    1,
                )

    def spell3(self):
        mousePos = pygame.mouse.get_pos()
        mousePos = list(mousePos)
        mousePos[0] = mousePos[0] // 100 * 100
        mousePos[1] = mousePos[1] // 100 * 100
        keys = pygame.key.get_pressed()
        if keys[pygame.K_o]:
            self.addEntity(
                Portal(
                    self.pos.x - 4 + mousePos[0] // 100,
                    self.pos.y - 4 + mousePos[1] // 100,
                    0,
                ),
                1,
            )
        if keys[pygame.K_p]:
            self.addEntity(
                Portal(
                    self.pos.x - 4 + mousePos[0] // 100,
                    self.pos.y - 4 + mousePos[1] // 100,
                    1,
                ),
                1,
            )

    def Activations(self, entityList):
        for i in range(len(entityList)):
            if (
                self.pos.x == entityList[i].pos.x
                and self.pos.y == entityList[i].pos.y
                and entityList[i].type != "trap"
            ):
                entityList[i].interacted = 1
                # print(entityList[i].interacted)
                # entityList[i].Draw()

    def useInventory(self):
        realI = 0
        keys = pygame.key.get_pressed()
        # print(keys[48])
        self.potionCooldown -= 1
        if len(self.inventory) == 0:
            return
        if self.inventory[-1][0].uses == 0:
            del self.inventory[-1]
        if len(self.inventory) == 0:
            return
        if keys[pygame.K_r]:
            if self.inventory[-1][0].uses >= 1:
                if (
                    self.inventory[-1][0].type == "HealthPotion"
                    and self.inventory[-1][0].uses > 0
                    and self.potionCooldown <= 0
                ):
                    self.Heal(self.inventory[-1][0].heal)
                    self.inventory[-1][0].uses -= 1
                    self.potionCooldown = 100

    def selectSpell(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.spellSlot = 1
        if keys[pygame.K_2]:
            self.spellSlot = 2

    def Update(self):
        if self.hp > 0:
            self.movementCooldown = self.movementCooldown - 1
            self.Move()
            self.useInventory()
            self.selectSpell()
            if self.spellSlot == 1:
                self.spell1()
            if self.spellSlot == 2:
                self.spell2()

    def Draw(self, window, cameraOffset):
        picture = self.picture
        if self.hp <= 0:
            picture = self.bloodpool
        return super().Draw(picture, window, cameraOffset)

    def Move(self):
        global latestMove
        if self.movementCooldown < 0:
            keys = pygame.key.get_pressed()
            if (
                keys[pygame.K_w]
                and self.isPassable(int(self.pos.x), int(self.pos.y - 1)) == True
            ):
                self.pos.y = self.pos.y - 1
                self.movementCooldown = self.defaultCooldown
                self.cameraOffset.y -= 1
                print(self.pos)
            if (
                keys[pygame.K_s]
                and self.isPassable(int(self.pos.x), int(self.pos.y + 1)) == True
            ):
                self.pos.y = self.pos.y + 1
                self.movementCooldown = self.defaultCooldown
                self.cameraOffset.y += 1
                print(self.pos)
            if (
                keys[pygame.K_a]
                and self.isPassable(int(self.pos.x - 1), int(self.pos.y)) == True
            ):
                self.pos.x = self.pos.x - 1
                self.movementCooldown = self.defaultCooldown
                self.cameraOffset.x -= 1
                print(self.pos)
            if (
                keys[pygame.K_d]
                and self.isPassable(int(self.pos.x + 1), int(self.pos.y)) == True
            ):
                self.pos.x = self.pos.x + 1
                self.movementCooldown = self.defaultCooldown
                self.cameraOffset.x += 1
                print(self.pos)

    def takeDamage(self, damage):
        GodMode = False
        if GodMode:
            pass
        else:
            return super().takeDamage(damage)

    def OnCollide(self, other):
        if isinstance(other, Door):
            other.interacted = 1
        if isinstance(other, Chest) and other.interacted == 0:
            other.interacted = 1
            self.inventory.append([HealthPotion(10, self), 1])
        # return super().OnCollide(other)
