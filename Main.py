from cmath import e
from re import S
import pygame


prozor = pygame.display.set_mode((1000, 1000))

# X = zid, O = vazduh, C = coin, S = sanduk (chest)
mapa = [
    "XXXXXXXXXX",
    "XOOOOOOOOX",
    "XOOOOOOOOX",
    "XOOOOOXXXX",
    "XOOOXXXOOX",
    "XOOXXXOOOX",
    "XOOOOXXXOX",
    "XOOOOOOOOX",
    "XOOOOOOOOX",
    "XXXXXXXXXX",
]

entityList = [[6, 5, "Chest"]]

# Texture
Chest1 = pygame.image.load(
    "C:\\Users\luka\\source\\repos\\Dejan-i-Luka-RPG\\Textures\\Chest1.png"
)
Dirt = pygame.image.load(
    "C:\\Users\luka\\source\\repos\\Dejan-i-Luka-RPG\\Textures\\Dirt.jpg"
)
StoneFloor = pygame.image.load(
    "C:\\Users\luka\\source\\repos\\Dejan-i-Luka-RPG\\Textures\\StoneFloor.jpg"
)
StoneFloor = pygame.transform.scale(StoneFloor, (100, 100))
Dirt = pygame.transform.scale(Dirt, (100, 100))
Chest1 = pygame.transform.scale(Chest1, (100, 100))


class Player:
    x = 1
    y = 1
    dx = 5
    dy = 5
    speed = 0
    hp = 0

    def Update(self):
        self.Move()

    def Draw(self):
        pygame.draw.rect(
            prozor,
            pygame.Color("Red"),
            pygame.Rect(self.x * 100, self.y * 100, 100, 100),
        )

    def Move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and mapa[player.x][player.y - 1] != "X":
                    player.y = player.y - 1
                    # print(player.x, player.y)
                    # exit()
                if event.key == pygame.K_DOWN and mapa[player.x][player.y + 1] != "X":
                    player.y = player.y + 1
                    # print(player.x, player.y)
                    # exit()
                if event.key == pygame.K_LEFT and mapa[player.x - 1][player.y] != "X":
                    player.x = player.x - 1
                    # print(player.x, player.y)
                    # exit()
                if event.key == pygame.K_RIGHT and mapa[player.x + 1][player.y] != "X":
                    player.x = player.x + 1
                    # print(player.x, player.y)
                    # exit()


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
        if entityList[i][2] == "Chest":
            prozor.blit(Chest1, (entityList[i][0] * 100, entityList[i][1] * 100))
    player.Update()
    player.Draw()
    pygame.display.flip()
