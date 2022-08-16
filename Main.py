import random
import pygame
import sys
from EnemySpawner import EnemySpawner
from Entity import Entity
from CollisionDetector import CollisionDetector
from Fire import Fire
from FireSystem import FireSystem
from Player import Player
from Door import Door
from HUD import Hud
from Item import Item
from Trap import Trap
from Chest import Chest
from Enemy1 import Enemy1

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
    "OOOOOOXXXOOOOOOOOOOOSSSOOOOOOOSSSSSSSSSSSSSSOOOOOOOSSSSSSSOOOOOOOOOOX",
    "OOOOOOXOXOOOOOOOOOOOOOSOOOOOOOSSWWWWWWWWWWWSSSSOOSSSSWWWWSSOOOOOOOOOX",
    "OOOOOOXXXOOOOOOOOOOOOOSSSOOOOSSSSSSSWWWWWWWWWWSSSSWWWWSSSSSOOOOOOOOOX",
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

firesystem = FireSystem(gridMap)


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


##### Entities (chests, enemies, missiles)


class Button:
    def __init__(self, picture, pos):
        self.picture = picture
        self.pos = pos

    def draw(self):
        window.blit(self.picture, self.pos)


Play_Button = Button(StartButton, (275, 210))

# =========================CHEST===========================#


# =========================CHEST===========================#
entityList2 = []


def addEntity(entity, map):
    if map == 1:
        entityList.append(entity)
    if map == 2:
        entityList2.append(entity)


# for i in range(len(entityList)):
#    print(entityList[i].pos, entityList[i].type)
# =========================DOOR============================#


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
addEntity(Enemy1(pygame.Vector2(11, 5), isPassable), 1)
addEntity(Enemy1(pygame.Vector2(10, 5), isPassable), 1)
# addEntity(Fire(pygame.Vector2(1, 1)), 1)

# =========================PLAYER==========================#


player = Player(
    pygame.Vector2(Player.startx, Player.starty), isPassable, addEntity, cameraOffset
)
entityList.append(player)
# =========================PLAYER==========================#


# =========================HUD=============================#


hud = Hud(window, player)
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

    frameCounter = 0

    while True:
        frameCounter += 1
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

        # System update
        collisionDetector.Update(entityList)
        firesystem.Update(entityList, frameCounter)

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
        # Update all entities
        for entity in entityList:
            entity.Update()

        # Remove dead enities
        i = 0
        while i < len(entityList):
            if entityList[i].hp <= 0:
                entityList.remove(entityList[i])
                i -= 1
            i += 1

        # Draw all entities
        for entity in entityList:
            entity.Draw(window, cameraOffset)

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
        print(f"EC: {len(entityList):4}")


if __name__ == "__main__":
    main_menu()
