import pygame
from globals import Globals
import Item
import HealthPotion


class Inventory:
    inventory = pygame.image.load("Textures\\rpgInventory - copy.png")
    inventory = pygame.transform.scale(inventory, (1920, 1080))
    charDimensions = Globals.numberDimensions

    def Update(self):
        self.unique = []
        self.count = []
        for item in Globals.entityList[0].inventory:
            if type(item[0]) not in self.unique:
                self.unique.append(type(item[0]))
                self.count.append(0)
            else:
                self.count[self.unique.index(type(item[0]))] += 1

    def draw(self, window):
        unique = self.unique
        count = self.count
        window.blit(self.inventory, pygame.Rect(0, 0, 1920, 1080))
        unique = self.unique
        x = 43
        y = 46
        multiplier1 = 3.7630662020905923344947735191638
        multiplier2 = 32
        for item in unique:
            image = item.picture
            image = pygame.transform.scale(
                image, (int(25 * multiplier1), int(25 * multiplier1))
            )
            window.blit(
                image,
                pygame.Rect(
                    int(x * multiplier1),
                    int(y * multiplier1),
                    int(25 * multiplier1),
                    int(25 * multiplier1),
                ),
            )
