from cmath import e
from re import S
import pygame


prozor = pygame.display.set_mode((1000, 1000))

# X = zid, O = vazduh, C = coin, S = sanduk (chest)
mapa = [
    "XXXXXXXXXX",
    "XOOOOOOOOX",
    "XXOOOOOOOX",
    "XOOOOOXXXX",
    "XOOOXXXOOX",
    "XOOXXXOOOX",
    "XOOOOXXXOX",
    "XOOOOOOOOX",
    "XOOOOOOOOX",
    "XXXXXXXXXX",
]


# Texture
Chest1 = pygame.image.load(
    "C:\\Users\luka\\source\\repos\\Dejan-i-Luka-RPG\\Textures\\Chest1.png"
)
OpenedChest1 = pygame.image.load(
    "C:\\Users\luka\\source\\repos\\Dejan-i-Luka-RPG\\Textures\\OpenedChest1.png"
)
Dirt = pygame.image.load(
    "C:\\Users\luka\\source\\repos\\Dejan-i-Luka-RPG\\Textures\\Dirt.jpg"
)
StoneFloor = pygame.image.load(
    "C:\\Users\luka\\source\\repos\\Dejan-i-Luka-RPG\\Textures\\StoneFloor.jpg"
)
warrior = pygame.image.load(
    "C:\\Users\luka\\source\\repos\\Dejan-i-Luka-RPG\\Textures\\warrior.png"
)
StoneFloor = pygame.transform.scale(StoneFloor, (100, 100))
Dirt = pygame.transform.scale(Dirt, (100, 100))
Chest1 = pygame.transform.scale(Chest1, (100, 100))
warrior = pygame.transform.scale(warrior, (100, 100))


def isPassable(
    x,
    y,
):
    # Prvo y pa x, jer prvo nadjemo visinu, i onda idemo kroz red, ovo nije bug
    if mapa[y][x] == "O":
        return True
    else:
        return False


##### Entities (chests, enemies, missiles)
class Entity:
    x = 0
    y = 0
    type = 0
    opened = 0

    def Update(self):
        0 == 0

    def Draw(self):
        if self.type == "Chest":
            if self.opened == 0:
                prozor.blit(Chest1, (self.x * 100, self.y * 100))
            if self.opened == 1:
                prozor.blit(OpenedChest1, (self.x * 100, self.y * 100))


entityList = []


def createNewEntity(x, y, type):
    entity = Entity()
    entity.x = x
    entity.y = y
    entity.type = type
    entityList.append(entity)


createNewEntity(8, 1, "Chest")


class Player:
    x = 1
    y = 1
    dx = 5
    dy = 5
    speed = 0
    hp = 0

    def Activations(self):
        for i in range(len(entityList)):
            if self.x == entityList[i].x and self.y == entityList[i].y:
                entityList[i].opened == 1
                # print("DONE")

    def Update(self):
        self.Move()
        self.Activations()

    def Draw(self):
        # pygame.draw.rect(prozor,pygame.Color("Red"),pygame.Rect(self.x * 100, self.y * 100, 100, 100))
        prozor.blit(warrior, (self.x * 100, self.y * 100))

    def Move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and isPassable(self.x, self.y - 1) == True:
                    self.y = self.y - 1
                if (
                    event.key == pygame.K_DOWN
                    and isPassable(self.x, self.y + 1) == True
                ):
                    self.y = self.y + 1
                if (
                    event.key == pygame.K_LEFT
                    and isPassable(self.x - 1, self.y) == True
                ):
                    self.x = self.x - 1
                if (
                    event.key == pygame.K_RIGHT
                    and isPassable(self.x + 1, self.y) == True
                ):
                    self.x = self.x + 1


player = Player()
while True:
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if mapa[i][j] == "X":
                prozor.blit(StoneFloor, (j * 100, i * 100))
            if mapa[i][j] == "O":
                prozor.blit(Dirt, (j * 100, i * 100))
            if mapa[i][j] == "OS":
                prozor.blit(Dirt, (j * 100, i * 100))
                prozor.blit(Chest1, (j * 100, i * 100))

    for i in range(len(entityList)):
        entityList[i].Update()
        entityList[i].Draw()
    player.Update()
    player.Draw()
    pygame.display.flip()
