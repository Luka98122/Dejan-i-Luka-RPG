import pygame
from Chest import Chest
from Entity import Entity
from Fire import Fire
from Door import Door
from HealthPotion import HealthPotion
from Trap import Trap
from globals import Globals
from Portal import Portal
from inventory import Inventory
import random


class Player(Entity):
    sizeofEverything = 0
    speed = 5
    hp = 500
    movementCooldown = 0
    potionCooldown = 100
    defaultCooldown = 15
    type = "player"
    isPassable = 0
    addEntity = 0
    bloodpool = 0
    spellCooldown = 50
    picture = pygame.image.load("textures\\wizard.png")
    picture = pygame.transform.scale(
        picture, (Globals.sizeofEverything, Globals.sizeofEverything)
    )
    originalPic = picture

    bloodpool = pygame.image.load("textures\\BloodPool.png")
    bloodpool = pygame.transform.scale(
        picture, (Globals.sizeofEverything, Globals.sizeofEverything)
    )

    originalPictures = [picture, bloodpool]
    pictures = [picture, bloodpool]

    def __init__(self, pos, isPassable, addEntity, cameraOffset) -> None:
        super().__init__(pos)
        self.type = "player"
        self.isPassable = isPassable
        self.addEntity = addEntity
        self.cameraOffset = cameraOffset
        self.sizeofEverything = Globals.sizeofEverything
        self.inventory = Inventory.inventory
        self.portalCD = 200
        self.spellSlot = 1
        self.picture = pygame.image.load("textures\\wizard.png")
        self.picture = pygame.transform.scale(
            self.picture, (Globals.sizeofEverything, Globals.sizeofEverything)
        )

        self.bloodpool = pygame.image.load("textures\\BloodPool.png")
        self.bloodpool = pygame.transform.scale(
            self.bloodpool, (Globals.sizeofEverything, Globals.sizeofEverything)
        )
        self.hp = 100

    startx = 4  # * sizeofEverything // 100
    starty = 4  # * sizeofEverything // 100
    pos = pygame.Vector2(startx, starty)

    def Heal(self, amount):
        self.hp = self.hp + amount

    def reScale(self):
        self.picture = pygame.image.load("textures\\wizard.png")
        self.picture = pygame.transform.scale(
            self.picture, (Globals.sizeofEverything, Globals.sizeofEverything)
        )

        self.bloodpool = pygame.image.load("textures\\BloodPool.png")
        self.bloodpool = pygame.transform.scale(
            self.bloodpool, (Globals.sizeofEverything, Globals.sizeofEverything)
        )

    def spell1(
        self,
    ):
        mousePos = pygame.mouse.get_pos()
        mousePos = list(mousePos)
        mousePos[0] = mousePos[0] // Globals.sizeofEverything * Globals.sizeofEverything
        mousePos[1] = mousePos[1] // Globals.sizeofEverything * Globals.sizeofEverything

        # window.blit(
        #    Door.OpenedDoor,
        #    (
        #        mousePos[0] // 100 * 100,
        #        mousePos[1] // 100 * 100,
        #    ),
        # )
        for event in Globals.events:
            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1
                and self.isPassable(
                    int(self.pos.x) - 4 + int(mousePos[0]) // Globals.sizeofEverything,
                    int(self.pos.y) - 4 + int(mousePos[1]) // Globals.sizeofEverything,
                )
            ):
                if self.spellCooldown < 0:
                    self.addEntity(
                        Fire(
                            pygame.Vector2(
                                self.pos.x
                                - 4
                                + mousePos[0] // Globals.sizeofEverything,
                                self.pos.y
                                - 4
                                + mousePos[1] // Globals.sizeofEverything,
                            ),
                            5,
                        ),
                        1,
                    )
                    print(
                        self.pos.x - 4 + mousePos[0] // Globals.sizeofEverything,
                        self.pos.y - 4 + mousePos[1] // Globals.sizeofEverything,
                        self.cameraOffset,
                    )
                    self.spellCooldown = 20

    def spell2(self):
        mousePos = pygame.mouse.get_pos()
        mousePos = list(mousePos)
        mousePos[0] = mousePos[0] // Globals.sizeofEverything * Globals.sizeofEverything
        mousePos[1] = mousePos[1] // Globals.sizeofEverything * Globals.sizeofEverything
        for event in Globals.events:
            if self.spellCooldown < 0:
                if (
                    event.type == pygame.MOUSEBUTTONDOWN
                    and event.button == 1
                    and self.isPassable(
                        int(self.pos.x)
                        - 4
                        + int(mousePos[0]) // Globals.sizeofEverything,
                        int(self.pos.y)
                        - 4
                        + int(mousePos[1]) // Globals.sizeofEverything,
                    )
                ):
                    self.addEntity(
                        Chest(
                            self.pos.x - 4 + mousePos[0] // Globals.sizeofEverything,
                            self.pos.y - 4 + mousePos[1] // Globals.sizeofEverything,
                        ),
                        1,
                    )
                    self.spellCooldown = 20

    def spell3(self):
        # print("entered")
        mousePos = pygame.mouse.get_pos()
        mousePos = list(mousePos)
        mousePos[0] = mousePos[0] // Globals.sizeofEverything * Globals.sizeofEverything
        mousePos[1] = mousePos[1] // Globals.sizeofEverything * Globals.sizeofEverything
        for event in Globals.events:
            if event.type == pygame.MOUSEBUTTONDOWN and self.isPassable(
                int(self.pos.x) - 4 + int(mousePos[0]) // Globals.sizeofEverything,
                int(self.pos.y) - 4 + int(mousePos[1]) // Globals.sizeofEverything,
            ):
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if Globals.portalsPlaced[0] == 0:
                        p = Portal(
                            self.pos.x - 4 + mousePos[0] // Globals.sizeofEverything,
                            self.pos.y - 4 + mousePos[1] // Globals.sizeofEverything,
                            0,
                        )

                        self.addEntity(p, 1)
                        Globals.portalList[0] = p
                        Globals.portalsPlaced[0] = 1
                    # print("added portal 0")
                    else:
                        for entity in Globals.entityList:
                            if type(entity) == Portal and entity.ID == 0:
                                Globals.entityList.remove(entity)
                                break
                        p = Portal(
                            self.pos.x - 4 + mousePos[0] // Globals.sizeofEverything,
                            self.pos.y - 4 + mousePos[1] // Globals.sizeofEverything,
                            0,
                        )
                        self.addEntity(p, 1)
                        Globals.portalList[0] = p
                        Globals.portalsPlaced[0] = 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    if Globals.portalsPlaced[1] == 0:
                        p = Portal(
                            self.pos.x - 4 + mousePos[0] // Globals.sizeofEverything,
                            self.pos.y - 4 + mousePos[1] // Globals.sizeofEverything,
                            1,
                        )
                        self.addEntity(p, 1)
                        Globals.portalList[1] = p

                        Globals.portalsPlaced[1] = 1
                    # print("added portal 1")

                    else:
                        for entity in Globals.entityList:
                            if type(entity) == Portal and entity.ID == 1:
                                Globals.entityList.remove(entity)
                                break
                        p = Portal(
                            self.pos.x - 4 + mousePos[0] // Globals.sizeofEverything,
                            self.pos.y - 4 + mousePos[1] // Globals.sizeofEverything,
                            1,
                        )
                        self.addEntity(p, 1)
                        Globals.portalList[1] = p
                        Globals.portalsPlaced[1] = 1

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
                    self.potionCooldown = 25

    def selectSpell(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.spellSlot = 1
        if keys[pygame.K_2]:
            self.spellSlot = 2
        if keys[pygame.K_3]:
            self.spellSlot = 3

    def Update(self):
        if self.hp > 0:
            self.Move()
            self.movementCooldown = self.movementCooldown - 1
            self.portalCD = self.portalCD - 1
            self.spellCooldown -= 1
            self.useInventory()
            self.selectSpell()
            if self.spellSlot == 1:
                self.spell1()
            if self.spellSlot == 2:
                self.spell2()
            if self.spellSlot == 3:
                self.spell3()

    def Draw(self, window, cameraOffset):
        picture = Player.pictures[0]
        if self.hp <= 0:
            picture = Player.pictures[1]
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
        if other.type == "npc":
            if other.id == "merchant1":
                if Globals.keys[pygame.K_e]:
                    Globals.state = 2
        elif isinstance(other, Door):
            other.interacted = 1
        elif isinstance(other, Chest) and other.interacted == 0:
            other.interacted = 1
            self.inventory.append([HealthPotion(10), 1])
            Inventory.goldCount += random.randint(1, 3)
        # return super().OnCollide(other)
