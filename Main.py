import random
import pygame
import sys
from EnemySpawner import EnemySpawner
from Entity import Entity
from CollisionDetector import CollisionDetector
from Fire import Fire

collisionDetector = CollisionDetector()
deathCooldown = 100
cameraOffset = pygame.Vector2(0, 0)
window = pygame.display.set_mode((800, 600))  # , pygame.FULLSCREEN)
movementCooldown = 0
entityList = []
currentMap = 1
latestMove = pygame.Vector2(0, 0)
# X = zid, O = vazduh, C = coin, S = sand, W = water, D = door
gridMap = [
    # 012345678901234567890123456789012345678901234567890123456789012345678
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOX",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOX",
    "OOOOOOOOOOOSSOOOOOOOOOOOOOOOWOWOWWWOWOOWWWOOOOOOOOOOOOOOOOOOOOOOOOOOX",
    "OOOOOSSSSSSSSSOOOOOOOOOOOOOOWWWOWOWOWOOWWWOOOOOOOOOOOOOOOOOOOOOOOOOOX",
    "OOOOOOOOOOOSSSSSSSOOOOOOOOOOWOWOWWWOWWOWOWOOOOOOOOOOOOOOOOOOOOOOOOOOX",
    "OOOOOOOOOOOOOOOSSSSSSOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOX",
    "OOOOOOOOOOOOOOOOOOSSSOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOX",
    "OOOOOOOOOOOOOOOOOOOOSOOOOOOOOOOSSSSSSSSSSSSOOOOOOOOOOSSSOOOOOOOOOOOOX",
    "OOOOOOOOOOOOOOOOOOOOSSSOOOOOOOSSSSSSSSSSSSSSOOOOOOOSSSSSSSOOOOOOOOOOX",
    "OOOOOOOOOOOOOOOOOOOOOOSOOOOOOOSSWWWWWWWWWWWSSSSOOSSSSWWWWSSOOOOOOOOOX",
    "OOOOOOOOOOOOOOOOOOOOOOSSSOOOOSSSSSSSWWWWWWWWWWSSSSWWWWSSSSSOOOOOOOOOX",
    "OOOOOOOOOOOOOOOOOOOOOOOOSSSSSSSSSSWWWWWWWWWWWWWWWWWWWWWSSSOOOOOOOOOOX",
    "OOOOOOOOOOOOXXXXXXXXXXXXOOOOOOSSSWWWWWWWWWWWWWWWWWWWWWWWSSOOOOOOOOOOX",
    "OOOOOOOOOOOOXFFFFFFFFFFXOOOOOOOSSSSSWWWWWWWWWWWWWWWWWWWSSOOOOOOOOOOOX",
    "OOOOOOOOOOOOXFFFFFFFFFFXOOOOOOSSSWWWWWWWWWWWWWWWWWWWWWWSSOOOOOOOOOOOX",
    "OOOOOOOOOOOOXXXXFFFFFFFXOOOOOOOOSSSSSSSWWWWWWWWWWWWWWWSSOOOOOOOOOOOOX",
    "OOOOOOOOOOOOOOOXFFFFFFFXOOOOOOOOOOOOSSSSSWWWWWWWSSSSSSSOOOOOOOOOOOOOX",
    "OOOOOOOOOOOOOOOXFFFFFFFXOOOOOOOOOOOOOOOSSSSSSSSSSSSSSSOOOOOOOOOOOOOOX",
    "OOOOOOOOOOOOOOOXXFXXXXXXOOOOOOOOOOOOOOOOOSSSSSSSSOOOOOOOOOOOOOOOOOOOX",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOX",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOX",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOX",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOX",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOX",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOX",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOX",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOX",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOX",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOX",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]


gridMap2 = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWFFFFFFFFFFFFFFFFWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWFFFFFFFFFFFFFFFFWWWWWWWWWWWWWWWWWWWWWWWFFFFFWWWWWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWFFFFFFFFFFFFFFFFWWWWWWWWWWWWWWWWWWWFFFFFFFFFFFFFFFWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWFFFFFFFFFFFFFFFFWWWWWWWWWWWWWWWWWWWWWWWFFFFFWWWWWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWFFFFFFFFFFFFFFFFWWWWWWWWWWWWWWWWWWWWWWWFFFFFWWWWWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWFFFFFFFFFFFFFFFFWWWWWWWWWWWWWWWWWWFFFFFFFFFFFFFFFFFFFFFWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWFFFFFFFFFFFFFFFFWWWWWWWWWWWWWWWWWWWWWWWFFFFFWWWWWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWFFFFFFFFFFFFFFFFWWWWWWWWWWWWWWWWWWWWWWWFFFFFWWWWWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWFFFFFFFFFFFFFFFFWWWWWWWWWWWWWWWWWWWWWWWFFFFFWWWWWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWFFFFFFFFFFFFFFFFWWWWWWWWWWWWWWWWWWWWWWWFFFFFWWWWWWWWWWWWWWWWWWWWWWWWW",
    "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
    "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
    "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
    "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
    "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
    "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXFXXXXXFFFFFFFFFSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSFFFSSSSSSSSSSSSSSSSSSS",
    "FFFFFFFFFFFFFFFFXFFFFFFFFFFFFFFFFXFFFXFFFFFFFFFSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSFFFSSSSSSSSSSSSSSSSSSS",
    "FFFFFFFFFFFFFFFFXFFFFFFFFFFFFFFFFXFFFXFFFFFFFFFSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSFFFSSSSSSSSSSSSSSSSSSS",
    "FFFFFFFFFFFFFFFFXFFFFFFFFFFFFFFFFXXXFXFFFFFFFFFSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSFFFSSSSSSSSSSSSSSSSSSS",
    "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFXFFFFFFFFFSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSFFFSSSSSSSSSSSSSSSSSSS",
    "FFFFFFFFFFFFFFFFXFFFFFFFFFFFFFFFFFFFFXFFFFFFFFFSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSFFFSSSSSSSSSSSSSSSSSSS",
    "FFFFFFFFFFFFFFFFXFFFFFFFFFFFFFFFFFFFFXFFFFFFFFFSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSFFFSSSSSSSSSSSSSSSSSSS",
    "FFFFFFFFFFFFFFFFXFFFFFFFFFFFFFFFFFFFFXFFFFFFFFFSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSFFFSFSSSSSSSSSSSSSSSSS",
    "XXXXXXXXXXXXXXXXXXFXXXXXXXXXXXXXXXXXXXFFFFFFFFFSSSSSSSSSSSSSSSSSSWWWWWWWWWWWSSSSSSSSSSSSSSSSSSSSFFFSFSSSSSSSSSSSSSSSSS",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOFFFFFFFFFSSSSSSSSSSSSSSSSWWWWWWWWWWWWWSSSSSSSSSSSSSSSSSSSSFFFFSSSSSSSSSSSSSSSSSS",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOFFFFFFFFFSSSSSSSSSSSSSSSSSSWWWWWWWWWWWSSSSSSSSSSSSSSSSSSSSSSFFSSSSSSSSSSSSSSSSSS",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOFFFFFFFFFSSSSSSSSSSSSSSSSSSWWWWWWWWWWWSSSSSSSSSSSSSSSSSSSSSSFFSSSSSSSSSSSSSSSSSS",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOFFFFFFFFFSSSSSSSSSSSSSSSSSSSSSSSSSWWWWSSSSSSSSSSSSSSSSSSSSSSFFSSSSSSSSSSSSSSSSSS",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOFFFFFFFFFSSSSSSSSSSSSSSSSSSSSSSSSSWWWWSSSSSSSSSSSSSSSSSSSSSSOOSSSSSSSSSSSSSSSSSS",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOFFFFFFFFFSSSSSSSSSSSSSSSSSSSSSSSSSWWWWWWWWWWWWSSSSSSSSSSSSSSOOSSSSSSSSSSSSSSSSSS",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOFFFFFFFFFSSSSSSSSSSSSSSSSSSSSSSSSSSSSWWWWWWWWWSSSSSSSSSSSSSSOOSSSSSSSSSSSSSSSSSS",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOFFFFFFFFFSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSWWWWSSSSSSSSSSSSSSSSOOSSSSSSSSSSSSSSSSSS",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOFFFFFFFFFSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSWWWWWWWWWWWWWWWWWWWWWFFWWWWWWWWWWWWWWWWWW",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOFFFFFFFFFSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSWWWWWWWWWWWWWWWWWWWWWFFWWWWWWWWWWWWWWWWWW",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOFFFFFFFFFSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSWWWWWWWWWWWWWWWWWWWWWFFWWWWWWWWWWWWWWWWWW",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOFFFFFFFFFSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSFFFSSSSSSSSSSSSSSSSS",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFSSSSSSSSSSSSSSSSSS",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOFFFFFFFFFSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS",
]


def imgSetup(str1):
    stringy = "Textures\\" + str1
    img = pygame.image.load(stringy)
    img = pygame.transform.scale(img, (100, 100))
    return img


Chest1 = imgSetup("Chest1.png")
OpenedChest1 = imgSetup("OpenedChest1.png")
Dirt = imgSetup("Dirt.jpg")
StoneFloor = imgSetup("StoneFloor.jpg")
water1 = imgSetup("Water1.png")
sand = imgSetup("sand.png")
WoodFloor = imgSetup("WoodFloor.png")


Village = pygame.image.load("Textures\Village.png")
StartButton = pygame.image.load("Textures\StartButton.png")


def isPassable(
    x,
    y,
):

    # Prvo y pa x, jer prvo nadjemo visinu, i onda idemo kroz red, ovo nije bug
    if currentMap == 1:
        if gridMap[y][x] != "X" and gridMap[y][x] != "W":
            return True
        else:
            return False
    if currentMap == 2:
        if gridMap2[y][x] != "X" and gridMap2[y][x] != "W":
            return True
        else:
            return False


#### Items
class Item:
    def __init__(self) -> None:
        self.uses = 1

    def Update(self):
        pass

    def Draw(self):
        pass


class HealthPotion(Item):
    healthPot = pygame.image.load("Textures\healthPotion.png")
    healthPot = pygame.transform.scale(healthPot, (75, 75))
    picture = healthPot

    def __init__(self, heal):
        # super().__init__()
        self.uses = 1
        self.heal = heal
        self.type = "HealthPotion"

    def Update(self):
        super().Update()
        if self.uses > 0:
            player.takeDamage(-self.heal)

    def Draw(self):
        super().Draw()


inventory = [[HealthPotion(10), 1], [HealthPotion(10), 1], [HealthPotion(10), 1]]
##### Entities (chests, enemies, missiles)


class Enemy1(Entity):
    picture = imgSetup("slime.png")

    def __init__(self, pos) -> None:
        super().__init__(pos)
        self.hp = 20
        self.pos = pygame.Vector2(pos[0], pos[1])
        self.alive = 1
        self.type = "Enemy1"
        self.movementCooldown = 100

    def Update(self):
        # return super().Update()
        if self.hp > 0:
            self.Movement()

    def Draw(self, window, cameraOffset):
        picture = self.picture
        if self.hp > 0:
            return super().Draw(picture, window, cameraOffset)

    def Movement(self):
        self.movementCooldown -= 1
        pos2 = [0, 0]
        r = random.SystemRandom()
        direct = r.randint(1, 4)
        if self.movementCooldown <= 0:
            print("entered")
            if direct == 1:
                pos2 = [self.pos.x - 1, self.pos.y]
            if direct == 2:
                pos2 = [self.pos.x + 1, self.pos.y]
            if direct == 3:
                pos2 = [self.pos.x, self.pos.y - 1]
            if direct == 4:
                pos2 = [self.pos.x, self.pos.y + 1]
            if isPassable(int(pos2[0]), int(pos2[1])):
                self.pos = pygame.Vector2(pos2[0], pos2[1])
                self.movementCooldown = 100

    def takeDamage(self, damage):
        return super().takeDamage(damage)

    def OnCollide(self, other):
        if isinstance(other, Door):
            other.interacted = 1


class Enemy2(Entity):
    def __init__(self, pos) -> None:
        super().__init__(pos)

    def Update(self):
        return super().Update()

    def Draw(self, window, cameraOffset):
        return super().Draw(picture, window, cameraOffset)

    def takeDamage(self, damage):
        return super().takeDamage(damage)


class Trap(Entity):
    explosiveBarrel = imgSetup("ExplosiveBarrel.png")
    oilSpill = imgSetup("OilSpill.png")
    type = "trap"

    def __init__(self, x, y) -> None:
        pos = pygame.Vector2(x, y)
        super().__init__(pos)
        self.damage = 20
        self.interacted = 0
        self.type = "trap"

    def Activate(self):
        return super().Activate()

    def Update(self):
        self.Activate()
        return super().Update()

    def Draw(self, window, cameraOffset):
        picture = self.explosiveBarrel
        if self.interacted == 1:
            picture = self.oilSpill
        return super().Draw(picture, window, cameraOffset)


class Button:
    def __init__(self, picture, pos):
        self.picture = picture
        self.pos = pos

    def draw(self):
        window.blit(self.picture, self.pos)


Play_Button = Button(StartButton, (275, 210))

# =========================CHEST===========================#
class Chest(Entity):
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
        picture = Chest1
        if self.interacted == 1:
            picture = OpenedChest1
        return super().Draw(picture, window, cameraOffset)


# =========================CHEST===========================#
entityList2 = []


def addEntity(entity, map):
    if map == 1:
        entityList.append(entity)
    if map == 2:
        entityList2.append(entity)


for i in range(len(entityList)):
    print(entityList[i].pos, entityList[i].type)
# =========================DOOR============================#


class Door(Entity):
    ClosedDoor = imgSetup("ClosedDoor.png")
    OpenedDoor = imgSetup("OpenedDoor.png")

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


# =========================DOOR============================#

# =========================ENTITIES========================#
addEntity(Chest(2, 1), 1)
addEntity(Door(17, 18), 1)
addEntity(Chest(15, 14), 1)
addEntity(Chest(33, 11), 1)
addEntity(Trap(8, 5), 1)
addEntity(Trap(13, 20), 1)

addEntity(Trap(1, 5), 1)
addEntity(Trap(2, 5), 1)
addEntity(Trap(3, 5), 1)
addEntity(Trap(4, 5), 1)
addEntity(Trap(5, 5), 1)


addEntity(Door(32, 16), 2)
addEntity(Door(16, 42), 2)
addEntity(Door(18, 24), 2)
addEntity(Door(33, 19), 2)
# =========================ENTITIES========================#
addEntity(Enemy1(pygame.Vector2(11, 5)), 1)
addEntity(Enemy1(pygame.Vector2(10, 5)), 1)
addEntity(Fire(pygame.Vector2(1, 1)), 1)

# =========================PLAYER==========================#
class Player(Entity):
    startx = 4
    starty = 4
    pos = pygame.Vector2(startx, starty)
    speed = 5
    hp = 100
    movementCooldown = 0
    potionCooldown = 100
    defaultCooldown = 15
    warrior = imgSetup("warrior.png")
    bloodPool = imgSetup("BloodPool.png")
    type = "player"

    def __init__(self, pos) -> None:
        super().__init__(pos)
        self.type = "player"

    def Heal(self, amount):
        self.hp = self.hp + amount

    def spell1(self):
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                addEntity(
                    Fire(
                        pygame.Vector2(
                            player.pos.x - 4 + mousePos[0] // 100,
                            player.pos.y - 4 + mousePos[1] // 100,
                        )
                    ),
                    currentMap,
                )
                print(
                    player.pos.x - 4 + mousePos[0] // 100,
                    player.pos.y - 4 + mousePos[1] // 100,
                    cameraOffset,
                )

    def Activations(self):
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
        if len(inventory) == 0:
            return
        if inventory[-1][0].uses == 0:
            del inventory[-1]
        if len(inventory) == 0:
            return
        if keys[pygame.K_r]:
            if inventory[-1][0].uses >= 1:
                if (
                    inventory[-1][0].type == "HealthPotion"
                    and inventory[-1][0].uses > 0
                    and self.potionCooldown <= 0
                ):
                    self.Heal(inventory[-1][0].heal)
                    inventory[-1][0].uses -= 1
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
            picture = self.bloodPool
        return super().Draw(picture, window, cameraOffset)

    def Move(
        self,
    ):
        global cameraOffset
        global latestMove
        if self.movementCooldown < 0:
            keys = pygame.key.get_pressed()
            if (
                keys[pygame.K_w]
                and isPassable(int(self.pos.x), int(self.pos.y - 1)) == True
            ):
                self.pos.y = self.pos.y - 1
                self.movementCooldown = self.defaultCooldown
                cameraOffset.y -= 1
                print(self.pos)
            if (
                keys[pygame.K_s]
                and isPassable(int(self.pos.x), int(self.pos.y + 1)) == True
            ):
                self.pos.y = self.pos.y + 1
                self.movementCooldown = self.defaultCooldown
                cameraOffset.y += 1
                print(self.pos)
            if (
                keys[pygame.K_a]
                and isPassable(int(self.pos.x - 1), int(self.pos.y)) == True
            ):
                self.pos.x = self.pos.x - 1
                self.movementCooldown = self.defaultCooldown
                cameraOffset.x -= 1
                print(self.pos)
            if (
                keys[pygame.K_d]
                and isPassable(int(self.pos.x + 1), int(self.pos.y)) == True
            ):
                self.pos.x = self.pos.x + 1
                self.movementCooldown = self.defaultCooldown
                cameraOffset.x += 1
                print(self.pos)

    def takeDamage(self, damage):
        return super().takeDamage(damage)

    def OnCollide(self, other):
        if isinstance(other, Door):
            other.interacted = 1
        # return super().OnCollide(other)


player = Player(pygame.Vector2(Player.startx, Player.starty))
entityList.append(player)
# =========================PLAYER==========================#


# =========================HUD=============================#
class Hud:
    heart = pygame.image.load("Textures\Heart.png")
    heart = pygame.transform.scale(heart, (50, 50))
    quickUseSlots = pygame.image.load("Textures\quickUseSlots.png")
    quickUseSlots = pygame.transform.scale(quickUseSlots, (220, 64))

    def __init__(self) -> None:
        pass

    def Draw(self):
        for i in range(player.hp // 10):
            window.blit(self.heart, (i * 50, 0))
        window.blit(self.quickUseSlots, (0, 525))
        for i in range(len(inventory)):
            if inventory[i][0].uses > 0:
                window.blit(inventory[i][0].picture, (5 + i * 65, 520))

    def update(self):
        pass


hud = Hud()
# =========================HUD=============================#


def main_menu():
    program_radi = True
    while program_radi:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                program_radi = False
            if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
                if (
                    Play_Button.picture.get_rect()
                    .move(Play_Button.pos)
                    .collidepoint(dogadjaj.pos)
                ):
                    play()

        window.blit(Village, (0, 0))
        Play_Button.draw()

        pygame.display.flip()

    pygame.quit()


def pause():
    program_radi = True
    while program_radi:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                program_radi = False
            if dogadjaj.type == pygame.KEYDOWN:
                if dogadjaj.key == pygame.K_p:
                    return
        window.fill((255, 0, 0))

    pygame.quit()


player.hp = 100


def play():
    global deathCooldown
    global currentMap
    global window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            sys.exit()
        score = 0

        collisionDetector.Update(entityList)

        for i in range(len(entityList)):
            if entityList[i].type == "chest" and entityList[i].interacted == 1:
                score += 1
        if keys[pygame.K_p]:
            pause()
        if keys[pygame.K_m] and score == 3:
            currentMap = 2
            player.pos.x = 0
            player.pos.y = 19
            cameraOffset.x = -3
            cameraOffset.y = 16
        if currentMap == 1:
            for i in range(len(gridMap)):
                for j in range(len(gridMap[0])):
                    slika = 0
                    if gridMap[i][j] == "S":
                        slika = sand
                    if gridMap[i][j] == "O":
                        slika = Dirt
                    if gridMap[i][j] == "W":
                        slika = water1
                    if gridMap[i][j] == "X":
                        slika = StoneFloor
                    if gridMap[i][j] == "F":
                        slika = WoodFloor
                    window.blit(
                        slika,
                        (
                            j * 100 - int(cameraOffset.x) * 100,
                            i * 100 - int(cameraOffset.y) * 100,
                        ),
                    )
        if currentMap == 2:
            for i in range(len(gridMap2)):
                for j in range(len(gridMap2[0])):
                    slika = 0
                    if gridMap2[i][j] == "S":
                        slika = sand
                    if gridMap2[i][j] == "O":
                        slika = Dirt
                    if gridMap2[i][j] == "W":
                        slika = water1
                    if gridMap2[i][j] == "X":
                        slika = StoneFloor
                    if gridMap2[i][j] == "F":
                        slika = WoodFloor
                    window.blit(
                        slika,
                        (
                            j * 100 - int(cameraOffset.x) * 100,
                            i * 100 - int(cameraOffset.y) * 100,
                        ),
                    )
        for i in range(len(entityList)):
            if currentMap == 1:
                entityList[i].Update()
                entityList[i].Draw(window, cameraOffset)
        for i in range(len(entityList2)):
            if currentMap == 2:
                entityList2[i].Update()
                entityList2[i].Draw(window, cameraOffset)
        if player.hp >= 1:
            player.Update()
        player.Draw(window, cameraOffset)
        hud.Draw()
        if player.hp <= 0:
            deathCooldown -= 1
        pygame.display.flip()
        if deathCooldown <= 0:
            pygame.quit()
            sys.exit()
        window.fill(pygame.Color("blue"))


if __name__ == "__main__":
    main_menu()
