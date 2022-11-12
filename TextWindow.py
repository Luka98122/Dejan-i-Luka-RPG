import pygame
from FontSheet import FontSheet
import random

fontSheet = FontSheet()
fontSheet.getDimensions("Textures\\TextFontSheet.png")


class TextWindow:
    textBox = pygame.image.load("textures\\TextBox1.png")

    ICON_Merchant1 = pygame.image.load("textures\\ICONS\\Merchant1ICON.png")
    ICON_Merchant1 = pygame.transform.scale(ICON_Merchant1, (120, 120))

    ICON_Unkown = pygame.image.load("textures\\ICONS\\UnknownICON.png")
    ICON_Unkown = pygame.transform.scale(ICON_Unkown, (120, 120))

    def __init__(self, width, height, pos, text, aditionalParameters, speaker):
        self.image = pygame.transform.scale(TextWindow.textBox, (width, height))
        self.x = int(pos.x)
        self.y = int(pos.y)
        self.pos = pos
        self.width = width
        self.height = height
        self.text = text
        self.aditionalParameters = aditionalParameters
        self.drawCount = 1
        self.firstDraw = 0
        self.soFar = 0
        self.frameRate = aditionalParameters[0]
        self.lifeSpan = aditionalParameters[1]
        self.currentFrame = 0
        self.curentChar = 0
        self.speaker = speaker

    def update(self):
        pass

    def draw(self, window):
        # SPEAKER
        if self.speaker == "merchant1":
            window.blit(
                TextWindow.ICON_Merchant1, pygame.Rect(self.x, self.y - 120, 120, 120)
            )

        if self.speaker == "unknown":
            window.blit(
                TextWindow.ICON_Unkown, pygame.Rect(self.x, self.y - 120, 120, 120)
            )

        window.blit(self.image, pygame.Rect(self.x, self.y, self.width, self.height))
        soFar1 = 0
        for i in range(self.curentChar):
            fontSheet.drawChar(
                self.text[i],
                [self.x + 40 + soFar1, self.y + 20],
                window,
            )
            if self.text[i] == " ":
                soFar1 += 20
                continue
            soFar1 += (
                fontSheet.charDimensions[fontSheet.abc.index(self.text[i])][2]
                - fontSheet.charDimensions[fontSheet.abc.index(self.text[i])][1]
            ) + 10
        # pygame.display.flip()
        if self.curentChar < len(self.text):
            if self.currentFrame % self.frameRate == 0:
                index = self.curentChar
                fontSheet.drawChar(
                    self.text[index],
                    [self.x + 40 + self.soFar, self.y + 20],
                    window,
                )
                self.curentChar += 1
                # pygame.display.flip()
                if self.text[index] == " ":
                    self.soFar += 20
                    return
                self.soFar += (
                    fontSheet.charDimensions[fontSheet.abc.index(self.text[index])][2]
                    - fontSheet.charDimensions[fontSheet.abc.index(self.text[index])][1]
                ) + 10
                self.lastSoFar = self.soFar
            self.currentFrame += 1
        else:
            self.soFar = 0
            for i in range(len(self.text)):
                fontSheet.drawChar(
                    self.text[i], [self.x + 40 + self.soFar, self.y + 20], window
                )
                # pygame.display.flip()
                if self.text[i] == " ":
                    self.soFar += 20
                    continue
                self.soFar += (
                    fontSheet.charDimensions[fontSheet.abc.index(self.text[i])][2]
                    - fontSheet.charDimensions[fontSheet.abc.index(self.text[i])][1]
                ) + 10
            self.lifeSpan -= 1
