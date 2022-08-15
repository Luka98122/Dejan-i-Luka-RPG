import pygame
from Entity import Entity
from Fire import Fire
from Door import Door


class Player(Entity):
    startx = 4
    starty = 4
    pos = pygame.Vector2(startx, starty)
    speed = 5
    hp = 100
    movementCooldown = 0
    potionCooldown = 100
    defaultCooldown = 15
    warrior = pygame.image.load("textures\\warrior.png")
    warrior = pygame.transform.scale(warrior, (100, 100))
    bloodpool = pygame.image.load("textures\\BloodPool.png")
    bloodpool = pygame.transform.scale(bloodpool, (100, 100))
    type = "player"
    isPassable = 0
    addEntity = 0

    def __init__(self, pos, isPassable, addEntity, cameraOffset) -> None:
        super().__init__(pos)
        self.type = "player"
        self.isPassable = isPassable
        self.addEntity = addEntity
        self.cameraOffset = cameraOffset
        self.inventory = (
            []
        )  # [[HealthPotion(10), 1], [HealthPotion(10), 1], [HealthPotion(10), 1]]

    def Heal(self, amount):
        self.hp = self.hp + amount

    def spell1(
        self,
    ):
        mousePos = pygame.mouse.get_pos()
        mousePos = list(mousePos)
        mousePos[0] = mousePos[0] // 100 * 100
        mousePos[1] = mousePos[1] // 100 * 100

        # window.blit(
        #    Door.OpenedDoor,
        #    (
        #        mousePos[0] // 100 * 100,
        #        mousePos[1] // 100 * 100,
        #    ),
        # )
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and self.isPassable(
                int(self.pos.x) - 4 + int(mousePos[0]) // 100,
                int(self.pos.y) - 4 + int(mousePos[1]) // 100,
            ):
                self.addEntity(
                    Fire(
                        pygame.Vector2(
                            self.pos.x - 4 + mousePos[0] // 100,
                            self.pos.y - 4 + mousePos[1] // 100,
                        ),
                        5,
                    ),
                    1,
                )
                print(
                    self.pos.x - 4 + mousePos[0] // 100,
                    self.pos.y - 4 + mousePos[1] // 100,
                    self.cameraOffset,
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

    def Update(self):
        if self.hp > 0:
            self.movementCooldown = self.movementCooldown - 1
            self.Move()
            self.useInventory()
            self.spell1()

    def Draw(self, window, cameraOffset):
        picture = self.warrior
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
        # return super().OnCollide(other)
