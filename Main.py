from glob import glob
from turtle import Screen, screensize
import py
import pygame
import sys

deathCooldown = 50
cameraOffset = pygame.Vector2(0, 0)
window = pygame.display.set_mode((800, 600))  # , pygame.FULLSCREEN)
movementCooldown = 50
entityList = []
latestMove = pygame.Vector2(0, 0)
# X = zid, O = vazduh, C = coin, S = sand, W = water, D = door
gridMap = [
    # 012345678901234567890123456789012345678901234567890123456789012345678
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "OOOOOOOOOOOSSOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "OOOOOSSSSSSSSSOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "OOOOOOOOOOOSSSSSSSOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "OOOOOOOOOOOOOOOSSSSSSOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "OOOOOOOOOOOOOOOOOOSSSOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "OOOOOOOOOOOOOOOOOOOOSOOOOOOOOOOSSSSSSSSSSSSOOOOOOOOOOSSSOOOOOOOOOOOOO",
    "OOOOOOOOOOOOOOOOOOOOSSSOOOOOOOSSSSSSSSSSSSSSOOOOOOOSSSSSSSOOOOOOOOOOO",
    "OOOOOOOOOOOOOOOOOOOOOOSOOOOOOOSSWWWWWWWWWWWSSSSOOSSSSWWWWSSOOOOOOOOOO",
    "OOOOOOOOOOOOOOOOOOOOOOSSSOOOOSSSSSSSWWWWWWWWWWSSSSWWWWSSSSSOOOOOOOOOO",
    "OOOOOOOOOOOOOOOOOOOOOOOOSSSSSSSSSSWWWWWWWWWWWWWWWWWWWWWSSSOOOOOOOOOOO",
    "OOOOOOOOOOOOXXXXXXXXXXXXOOOOOOSSSWWWWWWWWWWWWWWWWWWWWWWWSSOOOOOOOOOOO",
    "OOOOOOOOOOOOXFFFFFFFFFFXOOOOOOOSSSSSWWWWWWWWWWWWWWWWWWWSSOOOOOOOOOOOO",
    "OOOOOOOOOOOOXFFFFFFFFFFXOOOOOOSSSWWWWWWWWWWWWWWWWWWWWWWSSOOOOOOOOOOOO",
    "OOOOOOOOOOOOXXXXFFFFFFFXOOOOOOOOSSSSSSSWWWWWWWWWWWWWWWSSOOOOOOOOOOOOO",
    "OOOOOOOOOOOOOOOXFFFFFFFXOOOOOOOOOOOOSSSSSWWWWWWWSSSSSSSOOOOOOOOOOOOOO",
    "OOOOOOOOOOOOOOOXFFFFFFFXOOOOOOOOOOOOOOOSSSSSSSSSSSSSSSOOOOOOOOOOOOOOO",
    "OOOOOOOOOOOOOOOXXFXXXXXXOOOOOOOOOOOOOOOOOSSSSSSSSOOOOOOOOOOOOOOOOOOOO",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
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
    if gridMap[y][x] != "X" and gridMap[y][x] != "W":
        return True
    else:
        return False


##### Entities (chests, enemies, missiles)
class Entity:
    def __init__(self, pos) -> None:
        self.pos = pos
        self.type = 0
        self.interacted = 0
        self.hp = 0

    def Update(self):
        self.Activate()

    def Activate(self):
        for i in range(len(entityList)):
            if (
                self.pos.x == entityList[i].pos.x
                and self.pos.y == entityList[i].pos.y
                and self.interacted == 0
                and entityList[i].type != self.type
            ):
                self.interacted = 1
                if self.type == "trap":
                    entityList[i].takeDamage(self.damage)

    def Draw(self, picture):
        window.blit(
            picture,
            (
                self.pos.x * 100 - int(cameraOffset.x) * 100,
                self.pos.y * 100 - int(cameraOffset.y) * 100,
            ),
        )

    def takeDamage(self, damage):
        self.hp -= damage


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

    def Draw(self):
        picture = self.explosiveBarrel
        if self.interacted == 1:
            picture = self.oilSpill
        return super().Draw(picture)


class Button:
    def __init__(self, picture, pos):
        self.picture = picture
        self.pos = pos

    def draw(self):
        window.blit(self.picture, self.pos)


Play_Button = Button(StartButton, (275, 210))


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

    def Draw(self):
        picture = Chest1
        if self.interacted == 1:
            picture = OpenedChest1
        return super().Draw(picture)


def addEntity(entity):
    entityList.append(entity)


for i in range(len(entityList)):
    print(entityList[i].pos, entityList[i].type)


class Door(Entity):
    ClosedDoor = imgSetup("ClosedDoor.png")
    OpenedDoor = imgSetup("OpenedDoor.png")

    def __init__(self, x, y) -> None:
        pos = pygame.Vector2(x, y)
        super().__init__(pos)
        self.interacted = 0

    def Draw(self):
        slika = self.ClosedDoor
        if self.interacted == 1:
            slika = self.OpenedDoor
        return super().Draw(slika)


# =========================ENTITIES========================#
addEntity(Chest(2, 1))
addEntity(Door(17, 18))
addEntity(Chest(15, 14))
addEntity(Chest(33, 11))
addEntity(Trap(8, 5))
addEntity(Trap(13, 20))

addEntity(Trap(14, 21))
addEntity(Trap(15, 25))
addEntity(Trap(8, 20))


class Player(Entity):
    startx = 4
    starty = 4
    pos = pygame.Vector2(startx, starty)
    speed = 5
    hp = 100
    movementCooldown = 0
    defaultCooldown = 15
    warrior = imgSetup("warrior.png")
    type = "player"

    def __init__(self, pos) -> None:
        super().__init__(pos)
        self.type = "player"

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

    def Update(self):
        self.movementCooldown = self.movementCooldown - 1
        self.Move()

    def Draw(self):
        picture = self.warrior
        return super().Draw(picture)

    def Move(
        self,
    ):
        global cameraOffset
        global latestMove
        if self.movementCooldown < 0:
            keys = pygame.key.get_pressed()
            if (
                keys[pygame.K_UP]
                and isPassable(int(self.pos.x), int(self.pos.y - 1)) == True
            ):
                self.pos.y = self.pos.y - 1
                self.movementCooldown = self.defaultCooldown
                cameraOffset.y -= 1
                print(self.pos)
            if (
                keys[pygame.K_DOWN]
                and isPassable(int(self.pos.x), int(self.pos.y + 1)) == True
            ):
                self.pos.y = self.pos.y + 1
                self.movementCooldown = self.defaultCooldown
                cameraOffset.y += 1
                print(self.pos)
            if (
                keys[pygame.K_LEFT]
                and isPassable(int(self.pos.x - 1), int(self.pos.y)) == True
            ):
                self.pos.x = self.pos.x - 1
                self.movementCooldown = self.defaultCooldown
                cameraOffset.x -= 1
                print(self.pos)
            if (
                keys[pygame.K_RIGHT]
                and isPassable(int(self.pos.x + 1), int(self.pos.y)) == True
            ):
                self.pos.x = self.pos.x + 1
                self.movementCooldown = self.defaultCooldown
                cameraOffset.x += 1
                print(self.pos)

    def takeDamage(self, damage):
        return super().takeDamage(damage)


player = Player(pygame.Vector2(Player.startx, Player.starty))
entityList.append(player)


class Hud:
    heart = pygame.image.load("Textures\Heart.png")
    heart = pygame.transform.scale(heart, (50, 50))

    def __init__(self) -> None:
        pass

    def Draw(self):
        for i in range(player.hp // 10):
            window.blit(self.heart, (i * 50, 0))

    def update(self):
        pass


hud = Hud()


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
        if keys[pygame.K_p]:
            pause()
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
        for i in range(len(entityList)):
            entityList[i].Update()
            entityList[i].Draw()
        player.Update()
        player.Draw()
        hud.Draw()
        if player.hp <= 0:
            deathCooldown -= 1
        pygame.display.flip()
        if deathCooldown <= 0:
            pygame.quit()
            sys.exit()
        window.fill(pygame.Color("blue"))


main_menu()
