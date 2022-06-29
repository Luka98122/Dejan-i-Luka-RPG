from turtle import Screen, screensize
import py
import pygame
import sys

cameraOffset = pygame.Vector2(0, 0)
prozor = pygame.display.set_mode((800, 600))  # , pygame.FULLSCREEN)
movementCooldown = 50

latestMove = pygame.Vector2(0, 0)
# X = zid, O = vazduh, C = coin, S = sand, W = water, D = door
mapa = [
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
    "OOOOOOOOOOOOOOOXXOXXXXXXOOOOOOOOOOOOOOOOOSSSSSSSSOOOOOOOOOOOOOOOOOOOO",
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


# Texture
# ====================LOAD=======================#
Chest1 = pygame.image.load("Textures\Chest1.png")
OpenedChest1 = pygame.image.load("Textures\OpenedChest1.png")
Dirt = pygame.image.load("Textures\Dirt.jpg")
StoneFloor = pygame.image.load("Textures\StoneFloor.jpg")
warrior = pygame.image.load("Textures\warrior.png")
water1 = pygame.image.load("Textures\Water1.png")
sand = pygame.image.load("Textures\sand.png")
ClosedDoor = pygame.image.load("Textures\ClosedDoor.png")
OpenedDoor = pygame.image.load("Textures\OpenedDoor1.png")
WoodFloor = pygame.image.load("Textures\WoodFloor.png")
StartButton = pygame.image.load("Textures\StartButton.png")
Village = pygame.image.load("Textures\Village.png")
# =====================SCALE=====================#
StoneFloor = pygame.transform.scale(StoneFloor, (100, 100))
Dirt = pygame.transform.scale(Dirt, (100, 100))
Chest1 = pygame.transform.scale(Chest1, (100, 100))
warrior = pygame.transform.scale(warrior, (100, 100))
OpenedChest1 = pygame.transform.scale(OpenedChest1, (100, 100))
water1 = pygame.transform.scale(water1, (100, 100))
sand = pygame.transform.scale(sand, (100, 100))
ClosedDoor = pygame.transform.scale(ClosedDoor, (100, 100))
OpenedDoor = pygame.transform.scale(OpenedDoor, (100, 100))
WoodFloor = pygame.transform.scale(WoodFloor, (100, 100))


def isPassable(
    x,
    y,
):
    # Prvo y pa x, jer prvo nadjemo visinu, i onda idemo kroz red, ovo nije bug
    if mapa[y][x] != "X" and mapa[y][x] != "W":
        return True
    else:
        return False


##### Entities (chests, enemies, missiles)
class Entity:
    def __init__(self, pos) -> None:
        self.pos = pos
        self.type = 0

    def Update(self):
        pass

    def Draw(self, picture):
        prozor.blit(
            picture,
            (
                self.pos.x * 100 - int(cameraOffset.x) * 100,
                self.pos.y * 100 - int(cameraOffset.y) * 100,
            ),
        )


class Button:
    def __init__(self, picture, pos):
        self.picture = picture
        self.pos = pos

    def draw(self):
        prozor.blit(self.picture, self.pos)


Play_Button = Button(StartButton, (275, 210))


class Chest(Entity):
    def __init__(self, x, y) -> None:
        pos = pygame.Vector2(x, y)
        super().__init__(pos)
        self.opened = 0

    def Draw(self):
        #        return super().Draw()
        # print("Did it prior")
        if self.opened == 0:
            prozor.blit(
                Chest1,
                (
                    self.pos.x * 100 - int(cameraOffset.x) * 100,
                    self.pos.y * 100 - int(cameraOffset.y) * 100,
                ),
            )
        if self.opened == 1:
            prozor.blit(
                OpenedChest1,
                (
                    self.pos.x * 100 - int(cameraOffset.x) * 100,
                    self.pos.y * 100 - int(cameraOffset.y) * 100,
                ),
            )


entityList = []


def addEntity(entity):
    entityList.append(entity)


for i in range(len(entityList)):
    print(entityList[i].pos, entityList[i].type)


class Door(Entity):
    def __init__(self, x, y) -> None:
        pos = pygame.Vector2(x, y)
        super().__init__(pos)
        self.opened = 0

    def Draw(self):
        # return super.draw()
        if self.opened == 0:
            prozor.blit(
                ClosedDoor,
                (
                    self.pos.x * 100 - int(cameraOffset.x) * 100,
                    self.pos.y * 100 - int(cameraOffset.y) * 100,
                ),
            )
        if self.opened == 1:
            prozor.blit(
                OpenedDoor,
                (
                    self.pos.x * 100 - int(cameraOffset.x) * 100,
                    self.pos.y * 100 - int(cameraOffset.y) * 100,
                ),
            )


# =========================ENTITIES========================#
addEntity(Chest(2, 1))
addEntity(Door(17, 18))
addEntity(Chest(15, 14))
addEntity(Chest(33, 11))


class Player:
    startx = 4
    starty = 4
    pos = pygame.Vector2(startx, starty)
    speed = 5
    hp = 0
    movementCooldown = 0
    defaultCooldown = 15

    def Activations(self):
        for i in range(len(entityList)):
            if self.pos.x == entityList[i].pos.x and self.pos.y == entityList[i].pos.y:
                entityList[i].opened = 1
                print(entityList[i].opened)
                # entityList[i].Draw()

    def Update(self):
        self.movementCooldown = self.movementCooldown - 1
        self.Move()
        self.Activations()

    def Draw(self):
        # pygame.draw.rect(prozor,pygame.Color("Red"),pygame.Rect(self.pos.x * 100, self.pos.y * 100, 100, 100))
        prozor.blit(warrior, (self.startx * 100, self.starty * 100))

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


player = Player()


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

        prozor.blit(Village, (0, 0))
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
        prozor.fill((255, 0, 0))

    pygame.quit()


def play():
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
        for i in range(len(mapa)):
            for j in range(len(mapa[0])):
                slika = 0
                if mapa[i][j] == "S":
                    slika = sand
                if mapa[i][j] == "O":
                    slika = Dirt
                if mapa[i][j] == "W":
                    slika = water1
                if mapa[i][j] == "X":
                    slika = StoneFloor
                if mapa[i][j] == "F":
                    slika = WoodFloor
                prozor.blit(
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
        pygame.display.flip()
        prozor.fill(pygame.Color("blue"))


main_menu()
