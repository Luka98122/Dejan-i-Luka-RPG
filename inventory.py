import pygame
from globals import Globals
import Item
import HealthPotion


class Inventory:
    inventory = pygame.image.load("Textures\\rpgInventory - copy.png")
    inventory = pygame.transform.scale(inventory, (1920, 1080))
    numbers = pygame.image.load("Textures\\InventoryNumbers.png")
    charDimensions = Globals.numberDimensions
    multiplier1 = 3.7630662020905923344947735191638
    multiplier2 = 32

    def Update(self):
        self.unique = []
        self.count = []
        for item in Globals.entityList[0].inventory:
            if type(item[0]) not in self.unique:
                self.unique.append(type(item[0]))
                self.count.append(0)
            else:
                self.count[self.unique.index(type(item[0]))] += 1

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

    def draw(self, window):
        unique = self.unique
        count = self.count
        window.blit(self.inventory, pygame.Rect(0, 0, 1920, 1080))
        unique = self.unique
        x = 43
        y = 46
        multiplier1 = self.multiplier1

        for i in range(len(unique)):
            item = unique[i]
            itemCount = count[i]
            image = item.picture
            image = pygame.transform.scale(
                image, (int(25 * multiplier1), int(25 * multiplier1))
            )
            window.blit(
                image,
                pygame.Rect(
                    int(x * multiplier1 + (i * 31 * multiplier1)),
                    int(y * multiplier1),
                    int(25 * multiplier1),
                    int(25 * multiplier1),
                ),
            )
            self.drawNumber(
                window,
                itemCount + 1,
                pygame.Vector2(
                    int(60 * multiplier1 + (i * 31 * multiplier1)),
                    int(61 * multiplier1),
                ),
            )
