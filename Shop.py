import pygame
from globals import Globals
from HealthPotion import HealthPotion
from inventory import Inventory
from FontSheet import FontSheet
import copy


class Shop:
    picture = pygame.image.load("Textures\\ShopBackground.png")
    picture = pygame.transform.scale(picture, (1920, 1080))
    multiplier1 = 5.8536585365853658536585365853659
    # multiplier1 = 3.7630662020905923344947735191638

    def __init__(self, window) -> None:
        self.window = window
        self.shop = [
            [HealthPotion(20), 3, 2],
            [HealthPotion(30), 3, 3],
            [HealthPotion(10), 3, 1],
        ]

    def drawNumber(self, window, number, pos):
        myIndex = number - 1
        multiplier = 5
        info = Globals.numberDimensions[myIndex]
        img = pygame.image.load("Textures\\InventoryNumbers.png")
        img = pygame.transform.scale(img, (58 * multiplier, 7 * multiplier))

        window.blit(
            img,
            pygame.Rect(
                pos.x,
                pos.y,
                int(multiplier * 5 * self.multiplier1),
                int(multiplier * 7 * self.multiplier1),
            ),
            pygame.Rect(
                info[1] * multiplier,
                info[0] * multiplier,
                5 * multiplier,
                7 * multiplier,
            ),
        )

    def Draw(
        self,
    ):
        window = self.window
        window.blit(self.picture, (0, 0))
        for i in range(len(self.shop)):
            image = self.shop[i][0].picture
            itemCount = self.shop[i][1]
            image = pygame.transform.scale(
                image, (int(25 * self.multiplier1), int(25 * self.multiplier1))
            )
            window.blit(
                image,
                pygame.Rect(
                    int(30 * i * self.multiplier1 + 20),
                    int(30 * (i // 10) * self.multiplier1 + 20),
                    int(25 * self.multiplier1),
                    int(25 * self.multiplier1),
                ),
            )
            self.drawNumber(
                window,
                itemCount + 1,
                pygame.Vector2(
                    int(22 * (i + 1) * self.multiplier1 + (i * 11 * self.multiplier1)),
                    int(22 * self.multiplier1),
                ),
            )

    def DisplayProductInfo(self, tiley, tilex):
        pos = tiley * 10 + tilex
        window = self.window
        if pos < len(self.shop):
            # Get Info
            price = self.shop[pos][2]
            name = str(self.shop[pos][0].shopName) + "!"
            height = 100
            width = FontSheet.getLenOfString(name) + 40
            # Prep TextWindow
            textWindow = pygame.image.load("Textures\\TextBox1.png")
            textWindow = pygame.transform.scale(textWindow, (width, height))
            mousePos = pygame.mouse.get_pos()
            # Draw TextWindow
            window.blit(textWindow, (mousePos[0], mousePos[1], width, height))
            # Write Text
            # 1. Item Name
            FontSheet.drawString(
                FontSheet,
                name,
                [mousePos[0] + 20, mousePos[1] + 10],
                window,
            )
            # 2. Price
            Inventory.drawNumber(
                Inventory,
                window,
                price,
                [mousePos[0] + 20, mousePos[1] + 50],
            )

    def Update(self):
        mousePos = pygame.mouse.get_pos()
        mousePos = list(mousePos)
        tilex = (mousePos[0]) // int(33 * self.multiplier1)
        tiley = (mousePos[1]) // int(31 * self.multiplier1)
        print(mousePos)
        print(tilex, tiley)
        tileSize = int(31 * self.multiplier1)
        # Selected tile is drawn Red for Debug purposes
        """
        pygame.draw.rect(
            self.window,
            pygame.Color("Red"),
            (
                tilex * int(33 * self.multiplier1),
                tiley * int(31 * self.multiplier1) - 10,
                tileSize,
                tileSize,
            ),
        )
        """
        self.DisplayProductInfo(tiley, tilex)
        # print("Tilex", str(tilex))
        # print(len(self.shop))
        print(Globals.events)
        for event in Globals.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = tiley * 10 + tilex
                if pos < len(self.shop):
                    if (
                        self.shop[pos][1] > 0
                        and Inventory.goldCount >= self.shop[pos][2]
                    ):
                        Inventory.inventory.append([copy.copy(self.shop[pos][0]), 1])
                        Inventory.goldCount -= self.shop[pos][2]
                        self.shop[pos][1] -= 1
