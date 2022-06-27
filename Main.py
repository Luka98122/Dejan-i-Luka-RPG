from cmath import e
from re import S
import pygame


prozor = pygame.display.set_mode((1000, 1000))

# X = zid, O = vazduh, C = coin, S = sanduk (chest)
mapa = [
    "XXXXXXXXXX",
    "XOOOOOOOOO",
    "XOOOOOOOOO",
    "XOOOOOXXXO",
    "XOOOXXXOOO",
    "XOOXXXOOXO",
    "XOOOOXXXXO",
    "XOOOOOOOOO",
    "XOOOOOOOOO",
    "XXXXXXXXXX",
]

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
    x = 0
    y = 0
    dx = 5
    dy = 5
    speed = 0
    hp = 0

    def Update(self):
        0 == 0

    def Draw(self):
        pygame.draw.rect(
            prozor, pygame.Color("Red"), pygame.Rect(self.x, self.y, 100, 100)
        )


for i in range(len(mapa)):
    for j in range(len(mapa[0])):
        if mapa[i][j] == "X":
            prozor.blit(StoneFloor, (j * 100, i * 100))
        if mapa[i][j] == "O":
            prozor.blit(Dirt, (j * 100, i * 100))
        if mapa[i][j] == "OS":
            prozor.blit(Dirt, (j * 100, i * 100))
            prozor.blit(Chest1, (j * 100, i * 100))


player = Player()
player.Draw()
pygame.display.flip()
pygame.time.wait(5000)
