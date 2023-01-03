import random
import pygame
import sys

from globals import Globals

Globals.charDimensions = []
from FontSheet import FontSheet

fontSheet = FontSheet()
from inventory import Inventory


def act(actionParams):
    pass


FontSheet.charDimensions = []
location = "Textures\\textFontSheet.png"
fontSheet.getDimensions(location, 32)
location = "Textures\\textFontSheetLowerCase.png"
Globals.charDimensions = fontSheet.getDimensions(location, 32)
location = "Textures\\SpecialCharsFontsheet.png"
Globals.specialCharDimensions = fontSheet.getDimensions(location, 40)
from EnemySpawner import EnemySpawner
from Entity import Entity
from CollisionDetector import CollisionDetector
from Fire import Fire
from FireSystem import FireSystem
from MapDoor import MapDoor
from Player import Player
from Door import Door
from HUD import Hud
from Item import Item
from Trap import Trap
from Chest import Chest
from Enemy1 import Enemy1
from NPC import NPC
from EnemySpawner import EnemySpawner
from Portal import Portal
from DialogueSystem import DialogueSystem
from map1 import gridMap1
from map2 import gridMap2
from Shop import Shop

inventory = Inventory()
listOfClassesToScale = [
    Fire,
    Player,
    Door,
    Trap,
    Chest,
    Enemy1,
    EnemySpawner,
    Portal,
    NPC,
]

sat = pygame.time.Clock()
abc = "abcdefghijklmnopqrstuvwxyz"
collisionDetector = CollisionDetector()
deathCooldown = 100
cameraOffset = pygame.Vector2(0, 0)
window = pygame.display.set_mode(
    (Globals.screenDimensions[0], Globals.screenDimensions[1])
)  # , pygame.FULLSCREEN)

shop = Shop(window)
movementCooldown = 0
entityList = Globals.entityList

dialogueSystem = DialogueSystem()

"""dialogueSystem.addWindow(
    pygame.Vector2(100, 100),
    "ABCDEFGHIJKLMNOPQRSTVWXYZ",
    [5, 500],
    act,
    {"healthy": 2},
)

dialogueSystem.addWindow(
    pygame.Vector2(100, 200),
    "abcdefghijklmnopqrstuvwxyz",
    [5, 500],
    act,
    {"healthy": 2},
)
"""

maps = [gridMap1, gridMap2]


# sizeOfEverything = Globals.sizeofEverything

currentMap = 1
latestMove = pygame.Vector2(0, 0)
# X = zid, O = vazduh, C = coin, S = sand, W = water, D = door
currentMap = Globals.currentMap

currentMap = gridMap1
firesystem = FireSystem(currentMap)


def imgSetup(str1):
    stringy = "Textures\\" + str1
    img = pygame.image.load(stringy)
    img = pygame.transform.scale(
        img, (Globals.sizeofEverything, Globals.sizeofEverything)
    )
    return img


def PLimgSetup(img):
    img = pygame.transform.scale(
        img, (Globals.sizeofEverything, Globals.sizeofEverything)
    )
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
    x = int(x)
    y = int(y)
    if y >= len(currentMap) or y < 0:
        return False
    if x >= len(currentMap[0]) or x < 0:
        return False
    if currentMap[y][x] != "X" and currentMap[y][x] != "W":
        return True
    else:
        return False


#### Items


##### Entities (chests, enemies, missiles)

textBubble = pygame.image.load("Textures\\TextBox1.png")


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


def ScaleEverything():
    for thing in listOfClassesToScale:
        for i in range(len(thing.pictures)):
            thing.pictures[i] = pygame.transform.scale(
                thing.originalPictures[i],
                (Globals.sizeofEverything, Globals.sizeofEverything),
            )


# =========================DOOR============================#

player = Player(
    pygame.Vector2(Player.startx, Player.starty),
    isPassable,
    addEntity,
    cameraOffset,
)
entityList.append(player)
# =========================DOOR============================#

# =========================ENTITIES========================#
addEntity(Chest(2, 1), 1)
addEntity(Door(17, 18), 1)
addEntity(Chest(15, 14), 1)
addEntity(Chest(17, 13), 1)
addEntity(Chest(50, 9), 1)
addEntity(Chest(33, 11), 1)
# addEntity(MapDoor(68, 4, 1), 1) WIP
# addEntity(MapDoor(0, 4, 0), 1) WIP


addEntity(Door(32, 16), 2)
addEntity(Door(16, 42), 2)
addEntity(Door(18, 24), 2)
addEntity(Door(33, 19), 2)
addEntity(
    NPC(
        pygame.Vector2(20, 17),
        "merchant1",
        ["Hello Adventurer", "!\"£$%^&*()-_+=|\\\{\}[]:;@'~#<>?/,."],
        isPassable,
    ),
    1,
)

# =========================ENTITIES========================#


addEntity(Enemy1(pygame.Vector2(11, 5), isPassable), 1)
addEntity(Enemy1(pygame.Vector2(10, 5), isPassable), 1)
addEntity(EnemySpawner(pygame.Vector2(1, 1), isPassable, addEntity), 1)

# =========================PLAYER==========================#


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


def play():
    global deathCooldown
    global currentMap
    global window
    global sizeOfEverything
    global firesystem
    frameCounter = 0
    dialogueString = ""
    while True:
        pygame.event.pump()
        Globals.keys = pygame.key.get_pressed()
        Globals.events = pygame.event.get()
        if Globals.state == 0:
            frameCounter += 1
            currentMap = maps[Globals.currentMap]
            for event in Globals.events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    print("DOWN")
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEWHEEL:
                    if event.y > 0 and Globals.sizeofEverything != 100:
                        Globals.sizeofEverything = Globals.sizeofEverything * 2
                        ScaleEverything()
                    if event.y < 0 and Globals.sizeofEverything != 25:
                        Globals.sizeofEverything = Globals.sizeofEverything / 2
                        ScaleEverything()
                    print(
                        event.x,
                        event.y,
                    )
            if Globals.keys[pygame.K_ESCAPE]:
                sys.exit()
            # System update
            collisionDetector.Update(entityList)
            firesystem.Update(entityList, frameCounter)

            if Globals.keys[pygame.K_p]:
                Globals.state = 1
                continue
            if Globals.keys[pygame.K_o]:
                Globals.state = 2
                continue
            if Globals.keys[pygame.K_m]:
                currentMap = gridMap2
                firesystem = FireSystem(currentMap)
            for i in range(len(currentMap)):
                for j in range(len(currentMap[0])):
                    slika = 0
                    if currentMap[i][j] == "S":
                        slika = PLimgSetup(sand)
                    if currentMap[i][j] == "O":
                        slika = PLimgSetup(Dirt)
                    if currentMap[i][j] == "W":
                        slika = PLimgSetup(water1)
                    if currentMap[i][j] == "X":
                        slika = PLimgSetup(StoneFloor)
                    if currentMap[i][j] == "F":
                        slika = PLimgSetup(WoodFloor)
                    window.blit(
                        slika,
                        (
                            j * Globals.sizeofEverything
                            - int(cameraOffset.x) * Globals.sizeofEverything,
                            i * Globals.sizeofEverything
                            - int(cameraOffset.y) * Globals.sizeofEverything,
                        ),
                    )
            # Update all entities
            for entity in entityList:
                entity.Update()

            # Remove dead enities
            i = 0
            while i < len(entityList):
                if entityList[i].hp <= 0:
                    if type(entityList[i]) == Portal:
                        Globals.portalsPlaced[entityList[i].ID] = 0
                        Globals.portalList[entityList[i].ID] = 0
                        print("did it")
                    entityList.remove(entityList[i])
                    i -= 1
                i += 1

            # Draw all entities
            for entity in entityList:
                # if type(entity) == Fire:
                #    print("gotem")
                entity.Draw(window, cameraOffset)

            if player.hp >= 1:
                player.Update()
                player.Draw(window, cameraOffset)
            dialogueSystem.update()
            # player.Draw(window, cameraOffset)
            hud.Draw()
            dialogueSystem.draw(window)
            if player.hp <= 0:
                deathCooldown -= 1
            pygame.display.flip()
            if deathCooldown <= 0:
                pygame.quit()
                sys.exit()
            window.fill(pygame.Color("blue"))
            # print(f"EC: {len(entityList):4}")
            # print(Globals.sizeofEverything)
            # print(cameraOffset)
            # sat.tick(60)
            # print(sat)
        elif Globals.state == 1:
            if Globals.keys[pygame.K_TAB]:
                Globals.state = 0
                continue
            inventory.Update()
            inventory.draw(window)
            pygame.display.flip()
        elif Globals.state == 2:
            if Globals.keys[pygame.K_TAB]:
                Globals.state = 0
                continue
            shop.Draw()
            shop.Update()
            pygame.display.flip()


if __name__ == "__main__":
    main_menu()
