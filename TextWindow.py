import pygame
from FontSheet import FontSheet
import random
from globals import Globals

fontSheet = FontSheet()


class TextWindow:
    textBox = pygame.image.load("textures\\TextBox1.png")

    def __init__(
        self, width, height, pos, text, aditionalParameters, action, actionParams
    ):
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
        self.action = action
        self.actionParams = actionParams

    def update(self):
        pass

    def draw(self, window):
        # SPEAKER

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
            if self.text[i] in Globals.specialChars:
                soFar1 += (
                    Globals.specialCharDimensions[
                        Globals.specialChars.index(self.text[i])
                    ][2]
                    - Globals.specialCharDimensions[
                        Globals.specialChars.index(self.text[i])
                    ][1]
                ) + 10
            elif self.text[i].isnumeric() == False:
                soFar1 += (
                    fontSheet.charDimensions[Globals.abc.index(self.text[i])][2]
                    - fontSheet.charDimensions[Globals.abc.index(self.text[i])][1]
                ) + 10
            else:
                soFar1 += (
                    fontSheet.charDimensions[Globals.numbers.index(self.text[i])][2]
                    - fontSheet.charDimensions[Globals.numbers.index(self.text[i])][1]
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
                if self.text.isnumeric() == False:
                    if self.text[index] in Globals.abc:
                        self.soFar += (
                            fontSheet.charDimensions[
                                Globals.abc.index(self.text[index])
                            ][2]
                            - fontSheet.charDimensions[
                                Globals.abc.index(self.text[index])
                            ][1]
                        ) + 10
                    if self.text[index] in Globals.specialChars:
                        self.soFar += (
                            Globals.specialCharDimensions[
                                Globals.specialChars.index(self.text[index])
                            ][2]
                            - Globals.specialCharDimensions[
                                Globals.specialChars.index(self.text[index])
                            ][1]
                        ) + 10
                else:
                    self.soFar += (
                        fontSheet.charDimensions[
                            Globals.numbers.index(self.text[index])
                        ][2]
                        - fontSheet.charDimensions[
                            Globals.numbers.index(self.text[index])
                        ][1]
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
                if self.text[i] in Globals.specialChars:
                    return
                    soFar1 += (
                        Globals.specialCharDimensions[
                            Globals.specialChars.index(self.text[i])
                        ][2]
                        - Globals.specialCharDimensions[
                            Globals.specialChars.index(self.text[i])
                        ][1]
                    ) + 10
                elif self.text[i].isnumeric() == False:
                    self.soFar += (
                        fontSheet.charDimensions[Globals.abc.index(self.text[i])][2]
                        - fontSheet.charDimensions[Globals.abc.index(self.text[i])][1]
                    ) + 10
                else:
                    self.soFar += (
                        fontSheet.charDimensions[Globals.numbers.index(self.text[i])][2]
                        - fontSheet.charDimensions[Globals.numbers.index(self.text[i])][
                            1
                        ]
                    ) + 10
            self.lifeSpan -= 1
