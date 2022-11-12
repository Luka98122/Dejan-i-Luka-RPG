import pygame
from PIL import Image
import time


class FontSheet:
    textSheetCaps = pygame.image.load("Textures\\TextFontSheet.png")
    textSheetLowerCase = pygame.image.load("Textures\\textFontSheetLowerCase.png")
    fontSheets = [textSheetCaps, textSheetLowerCase]
    charsInfo = []
    abc = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self) -> None:
        pass

    charDimensions = []

    def getDimensions(self, fontSheet):
        height = 32
        pixelCursor = pygame.Vector2(0, 0)
        image = Image.open(fontSheet)
        pixels = image.load()
        x = 0
        layer = 0
        column = 0
        lastColumn = 0
        currentCharInfo = []
        counter = 0
        while x < image.size[0]:
            switch = 0
            column = 0
            for y in range(32):
                if pixels[x, y + layer * 40][3] == 0:
                    continue
                else:
                    switch = 1
                    column = 1
                    break

            if switch == 1 and lastColumn == 0:
                currentCharInfo.append(layer)
                currentCharInfo.append(x)

            if switch == 0 and lastColumn == 1:
                currentCharInfo.append(x)
                FontSheet.charDimensions.append(currentCharInfo)
                currentCharInfo = []
                x += 1
                lastColumn = 0
                if x >= image.size[0]:
                    if layer < 1:
                        layer += 1
                    else:
                        return
                    currentCharInfo.append()
                    FontSheet.charDimensions.append(currentCharInfo)
                    currentCharInfo = []
                    column = 0
                    x = 0
                continue

            lastColumn = column
            x += 1
            if x >= image.size[0]:
                currentCharInfo.append(x)
                FontSheet.charDimensions.append(currentCharInfo)
                currentCharInfo = []
                lastColumn = 0
                column = 0
                if layer < 1:
                    layer += 1
                else:
                    return
                x = 0
            continue

        print(FontSheet.charsInfo)

    def drawChar(
        self,
        char,
        pos,
        window,
    ):
        if char == " ":
            return
        index = FontSheet.abc.index(char)
        info = FontSheet.charDimensions[index]
        window.blit(
            FontSheet.fontSheets[0],
            pygame.Rect(pos[0], pos[1], info[2] - info[1], 32),
            (info[1], info[0] * 40, info[2] - info[1], 32),
        )

    def getLenOfString(myString):
        res = 0
        for char in myString:
            if char == " ":
                res += 20
                continue
            index = FontSheet.abc.index(char)
            info = FontSheet.charDimensions[index]
            res += info[2] - info[1] + 10
        return res

    def drawString(self, string, pos, window, aditionalParameters, firstDraw):
        sofar = 0
        i = 0
        while i < len(string):
            if string[i] == " ":
                sofar += 20
                continue
            index = FontSheet.abc.index(string[i])
            info = FontSheet.charDimensions[index]
            FontSheet.drawChar(
                self,
                string[i],
                [pos[0] + sofar, pos[1]],
                window,
                aditionalParameters,
                firstDraw,
            )
            sofar += info[2] - info[1] + 10
            i += 1
