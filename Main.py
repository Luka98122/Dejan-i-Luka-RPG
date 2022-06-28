import pygame
import sys

prozor = pygame.display.set_mode((1000, 1000))
movementCooldown = 1000
# X = zid, O = vazduh, C = coin, S = sanduk (chest)
mapa = [
    "XXXXXXXXXXO",
    "XOOOOOOOOXO",
    "XXOOOOOOOXO",
    "XOOOOOXXXXO",
    "XOOOXXXOOXO",
    "XOOXXXOOOXO",
    "XOOOOXXXOXO",
    "XOOOOOOOOXO",
    "XOOOOOOOOXO",
    "XXXXXXXXXXO",
]


# Texture
Chest1 = pygame.image.load("Textures\Chest1.png")
OpenedChest1 = pygame.image.load("Textures\OpenedChest1.png")
Dirt = pygame.image.load("Textures\Dirt.jpg")
StoneFloor = pygame.image.load("Textures\StoneFloor.jpg")
warrior = pygame.image.load("Textures\warrior.png")
StoneFloor = pygame.transform.scale(StoneFloor, (100, 100))
Dirt = pygame.transform.scale(Dirt, (100, 100))
Chest1 = pygame.transform.scale(Chest1, (100, 100))
warrior = pygame.transform.scale(warrior, (100, 100))
OpenedChest1 = pygame.transform.scale(OpenedChest1, (100, 100))


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
            # print("Did it prior")
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
    pos = pygame.Vector2(1, 1)
    speed = 5
    hp = 0
    movementCooldown = 0
    defaultCooldown = 50

    def Activations(self):
        for i in range(len(entityList)):
            if self.pos.x == entityList[i].x and self.pos.y == entityList[i].y:
                entityList[i].opened = 1

    def Update(self):
        self.movementCooldown = self.movementCooldown - 1
        self.Move()
        self.Activations()

    def Draw(self):
        # pygame.draw.rect(prozor,pygame.Color("Red"),pygame.Rect(self.pos.x * 100, self.pos.y * 100, 100, 100))
        prozor.blit(warrior, (self.pos.x * 100, self.pos.y * 100))

    def Move(
        self,
    ):
        if self.movementCooldown < 0:
            keys = pygame.key.get_pressed()
            if (
                keys[pygame.K_UP]
                and isPassable(int(self.pos.x), int(self.pos.y - 1)) == True
            ):
                self.pos.y = self.pos.y - 1
                self.movementCooldown = self.defaultCooldown
            if (
                keys[pygame.K_DOWN]
                and isPassable(int(self.pos.x), int(self.pos.y + 1)) == True
            ):
                self.pos.y = self.pos.y + 1
                self.movementCooldown = self.defaultCooldown
            if (
                keys[pygame.K_LEFT]
                and isPassable(int(self.pos.x - 1), int(self.pos.y)) == True
            ):
                self.pos.x = self.pos.x - 1
                self.movementCooldown = self.defaultCooldown
            if (
                keys[pygame.K_RIGHT]
                and isPassable(int(self.pos.x + 1), int(self.pos.y)) == True
            ):
                self.pos.x = self.pos.x + 1
                self.movementCooldown = self.defaultCooldown


player = Player()
while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        sys.exit()

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
