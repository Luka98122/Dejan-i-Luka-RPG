import pygame
from globals import Globals
from globals import Textures
import Item
from HealthPotion import HealthPotion
from ArmorBoots import ArmorBoots
from ArmorChest import ArmorChest
from ArmorGloves import ArmorGloves
from ArmorHelmet import ArmorHelmet
from debugMenu import DebugMenu

dMenu = DebugMenu


class Inventory:
    inventoryPic = Textures.inventory
    inventoryPic = pygame.transform.scale(inventoryPic, (1920, 1080))
    numbers = Textures.numbers
    frame = 0
    inventory = [
        [HealthPotion(10), 1],
        [HealthPotion(10), 1],
        [HealthPotion(10), 1],
        [HealthPotion(10), 1],
    ]
    charDimensions = Globals.numberDimensions
    multiplier1 = 3.7630662020905923344947735191638
    multiplier2 = 30.5
    goldCount = 6
    equippedArmor = [
        ArmorBoots("Steel Boots", 150, [None]),
        ArmorChest("Iron Chestplate", 200, [50, 30, 20]),
        ArmorGloves("Daedric Gauntlets", 170, [50]),
        ArmorHelmet("Gold Helmet", 200, [None]),
    ]
    xOffset = 40
    yOffset = 46

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
        for i in range(len(str(number))):
            info = Globals.numberDimensions[myIndex]
            img = Textures.numbers
            img = pygame.transform.scale(img, (58 * multiplier, 7 * multiplier))
            pos = pygame.Vector2(pos[0] + i * 10, pos[1])

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
        window.blit(self.inventoryPic, pygame.Rect(0, 0, 1920, 1080))
        unique = self.unique
        x = 43
        y = 46
        multiplier1 = self.multiplier1
        if self.goldCount > 0:
            image = Textures.goldCoin
            itemCount = self.goldCount
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
            self.drawNumber(
                window,
                itemCount,
                pygame.Vector2(
                    int(60 * multiplier1),
                    int(61 * multiplier1),
                ),
            )
        for i in range(len(unique)):
            item = unique[i]
            itemCount = count[i]
            image = item.picture
            bonus = 0
            if self.goldCount > 0:
                bonus = 31
            image = pygame.transform.scale(
                image, (int(25 * multiplier1), int(25 * multiplier1))
            )
            window.blit(
                image,
                pygame.Rect(
                    int(x * multiplier1 + (bonus * multiplier1 + i * 31 * multiplier1)),
                    int(y * multiplier1),
                    int(25 * multiplier1),
                    int(25 * multiplier1),
                ),
            )
            self.drawNumber(
                window,
                itemCount + 1,
                pygame.Vector2(
                    int(
                        60 * multiplier1 + (bonus * multiplier1 + i * 31 * multiplier1)
                    ),
                    int(61 * multiplier1),
                ),
            )
        mousePos = pygame.mouse.get_pos()
        cx = int(
            (mousePos[0] - self.xOffset * multiplier1) / int(33 * self.multiplier1)
        )
        cy = int(
            (mousePos[1] - self.yOffset * multiplier1) / int(32 * self.multiplier1)
        )
        pygame.draw.rect(
            window,
            pygame.Color("Red"),
            pygame.Rect(
                self.xOffset * multiplier1 + cx * self.multiplier2 * multiplier1,
                self.yOffset * multiplier1 + cy * self.multiplier2 * multiplier1,
                self.multiplier2 * self.multiplier1,
                self.multiplier2 * self.multiplier1,
            ),
        )
        print(cx, cy)
        dMenu.Update(dMenu, cx, cy, self.multiplier1, self.multiplier2)
        if self.frame % 20 == 0:
            dMenu.Draw(dMenu)
        keys = Globals.keys
        if keys[pygame.K_1]:
            self.multiplier1 -= 0.1
        if keys[pygame.K_2]:
            self.multiplier1 += 0.1
        if keys[pygame.K_3]:
            self.multiplier2 -= 0.1
        if keys[pygame.K_4]:
            self.multiplier2 += 0.1
        if keys[pygame.K_5]:
            self.xOffset -= 1
        if keys[pygame.K_6]:
            self.xOffset += 1
        if keys[pygame.K_7]:
            self.yOffset -= 1
        if keys[pygame.K_8]:
            self.yOffset += 1

        self.frame += 1
