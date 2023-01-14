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
from goldCoin import GoldCoin
from FontSheet import FontSheet
import copy

dMenu = DebugMenu


class Inventory:
    inventoryPic = Textures.inventory
    inventoryPic = pygame.transform.scale(inventoryPic, (1920, 1080))
    numbers = Textures.numbers
    frame = 0
    inventory = [
        [HealthPotion(10)],
        [HealthPotion(10)],
        [HealthPotion(30)],
        [HealthPotion(10)],
        [HealthPotion(20)],
        [HealthPotion(30)],
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
        shopNames = []
        for item in self.inventory:
            if type(item[0]) == GoldCoin:
                continue
            if item[0].shopName not in shopNames:
                shopNames.append(item[0].shopName)
                self.unique.append(item[0])
                self.count.append(1)
            else:
                self.count[shopNames.index(item[0].shopName)] += 1
        for i in range(len(self.count)):
            if self.count[i] > self.unique[i].maxStack:
                for j in range(self.count[i] // self.unique[i].maxStack):
                    newObj = copy.deepcopy(self.unique[i])
                    self.unique.append(newObj)
                    self.count.append(self.unique[i].maxStack)
                newObj = copy.deepcopy(self.unique[i])
                self.unique.append(newObj)
                self.count.append(self.count[i] % self.unique[i].maxStack)
                del self.unique[i]
                del self.count[i]
        a = 2

    def DisplayProductInfo(self, tilex, tiley, window):
        if tilex < 0 or tiley < 0:
            return
        pos = tiley * 10 + tilex
        bonus = 0
        didBonus = False
        if self.goldCount > 0:
            bonus = 1
        if pos != 0:
            pos = pos - bonus
            didBonus = True
        if pos < len(self.unique):
            thingy = self.unique[pos]
            # Get Info
            if self.goldCount > 0:
                if pos == 0 and didBonus == False:
                    thingy = GoldCoin()
                elif pos == 0 and didBonus == True:
                    pos = 1
            name = str(thingy.shopName)
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

    def drawNumber(self, window, number, pos):
        multiplier = 5
        if len(str(number)) > 1:
            pos.x = pos.x - len(str(number)) * 10
        for i in range(len(str(number))):
            myIndex = int(str(number)[i]) - 1
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
        multiplier1 = self.multiplier1 + 0.07
        if self.goldCount > 0:
            image = Textures.goldCoin
            itemCount = self.goldCount
            if type(self.inventory[0][0]) != GoldCoin:
                self.inventory.insert(0, [GoldCoin(), self.goldCount])
            else:
                self.inventory[0] = [GoldCoin(), self.goldCount]
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
            if type(item) == GoldCoin:
                continue
            itemCount = count[i]
            image = item.picture
            bonus = 0
            if self.goldCount > 0:
                bonus = 30
            image = pygame.transform.scale(
                image,
                (int(25 * multiplier1), int(25 * multiplier1)),
            )
            window.blit(
                image,
                pygame.Rect(
                    int(x * multiplier1 + (i * 31 * multiplier1) + bonus * multiplier1),
                    int(y * multiplier1),
                    int(25 * multiplier1),
                    int(25 * multiplier1),
                ),
            )
            self.drawNumber(
                window,
                itemCount,
                pygame.Vector2(
                    int(
                        60 * multiplier1 + (i * 30 * multiplier1) + bonus * multiplier1
                    ),
                    int(61 * multiplier1),
                ),
            )
        bonus = 0
        mousePos = pygame.mouse.get_pos()
        cx = int((mousePos[0] - self.xOffset * multiplier1) / int(33 * 3.50))
        cy = int((mousePos[1] - self.yOffset * multiplier1) / int(32 * 3.50))

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

        print(cy, cx)
        self.DisplayProductInfo(cx, cy, window)
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
            self.xOfset += 1
        if keys[pygame.K_7]:
            self.yOffset -= 1
        if keys[pygame.K_f]:
            self.inventory.append([HealthPotion(10)])

        self.frame += 1
