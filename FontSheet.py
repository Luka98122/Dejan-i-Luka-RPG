import pygame
from PIL import Image
import time
from globals import Globals
from globals import Textures


class FontSheet:
    textSheetCaps = Textures.textSheetCaps
    textSheetLowerCase = Textures.textSheetLowerCase
    numberFontSheet = Textures.numberFontSheet
    specialCharsFontsheet = Textures.specialCharsFontsheet
    fontSheets = [textSheetCaps, textSheetLowerCase, numberFontSheet]
    charsInfo = []
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self) -> None:
        pass

    charDimensions = []
    allDims = []

    def getDimensions(self, fontSheet, height):
        pixelCursor = pygame.Vector2(0, 0)
        image = Image.open(fontSheet)
        pixels = image.load()
        x = 0
        layer = 0
        column = 0
        lastColumn = 0
        currentCharInfo = []
        counter = 0
        lastone = 0
        while x < image.size[0]:
            if len(FontSheet.charDimensions) == 20:
                a1 = 2
            switch = 0
            column = 0
            bonus = 0
            if fontSheet != "Textures\\InventoryNumbers.png":
                bonus = 8
            if fontSheet == "Textures\\SpecialCharsFontsheet.png":
                bonus = 0
                charInfo = []
            for y in range(height):
                if pixels[x, y + layer * height + bonus][3] == 0:
                    continue
                else:
                    switch = 1
                    column = 1
                    break

            if switch == 1 and lastColumn == 0:
                if fontSheet == "Textures\\SpecialCharsFontsheet.png":
                    if x - lastone > 4 or lastone == 0:
                        currentCharInfo.append(layer)
                        currentCharInfo.append(x)
                else:
                    currentCharInfo.append(layer)
                    currentCharInfo.append(x)

            if switch == 0 and lastColumn == 1:
                if fontSheet == "Textures\\SpecialCharsFontsheet.png":
                    if x - lastone > 4:
                        currentCharInfo.append(x)
                        Globals.specialCharDimensions.append(currentCharInfo)
                        currentCharInfo = []
                else:
                    currentCharInfo.append(x)
                    FontSheet.charDimensions.append(currentCharInfo)
                    currentCharInfo = []
                x += 1
                lastColumn = 0
                if x >= image.size[0]:
                    if fontSheet == "Textures\\InventoryNumbers.png":
                        return FontSheet.charDimensions
                    if layer < 1:
                        layer += 1
                    else:
                        return
                    currentCharInfo.append()
                    if fontSheet == "Textures\\SpecialCharsFontsheet.png":
                        Globals.specialCharDimensions.append(currentCharInfo)
                    else:
                        FontSheet.charDimensions.append(currentCharInfo)
                    currentCharInfo = []
                    column = 0
                    x = 0
                continue

            lastColumn = column
            x += 1
            if switch == 1:
                lastone = x
            if x >= image.size[0]:
                if fontSheet == "Textures\\InventoryNumbers.png":
                    return FontSheet.charDimensions
                currentCharInfo.append(x)
                if fontSheet == "Textures\\SpecialCharsFontsheet.png":
                    Globals.specialCharDimensions.append(currentCharInfo)
                else:
                    FontSheet.charDimensions.append(currentCharInfo)
                currentCharInfo = []
                lastColumn = 0
                column = 0
                if layer < 1:
                    layer += 1
                else:
                    return FontSheet.charDimensions
                x = 0
            continue
        return FontSheet.charDimensions

        print(FontSheet.charsInfo)

    def drawChar(
        self,
        char,
        pos,
        window,
    ):
        if char == " ":
            return
        if char in Globals.abc:
            index = Globals.abc.index(char)
        if char in Globals.specialChars:
            index = Globals.specialChars.index(char)
            spec = 0
            multiplier = 52
            height = 40
            info = Globals.specialCharDimensions[index]
            window.blit(
                FontSheet.specialCharsFontsheet,
                pygame.Rect(pos[0], pos[1] - spec, info[2] - info[1], height),
                (info[1], info[0] * multiplier, info[2] - info[1], height),
            )
            return
        sheetNumber = 0
        height = 32
        multiplier = 40
        spec = 0

        if index > 25:
            sheetNumber = 1
            height = 36
            multiplier = 45
            if char == "t":
                multiplier = 41
                height = 40
                spec = 4
        if char == "g" and sheetNumber == 1:
            height = 44

        info = Globals.charDimensions[index]
        if char in ["p", "q", "y"] and sheetNumber == 1:
            height = 44

        window.blit(
            FontSheet.fontSheets[sheetNumber],
            pygame.Rect(pos[0], pos[1] - spec, info[2] - info[1], height),
            (info[1], info[0] * multiplier, info[2] - info[1], height),
        )

    def getLenOfString(myString):
        res = 0
        for char in myString:
            if char == " ":
                res += 20
                continue
            if char in Globals.abc:
                index = Globals.abc.index(char)
                info = Globals.charDimensions[index]
            if char in Globals.specialChars:
                index = Globals.specialChars.index(char)
                len(Globals.specialCharDimensions)
                len(Globals.specialChars)
                info = Globals.specialCharDimensions[index]
                print(
                    "Char: "
                    + char
                    + "/Info: "
                    + str(info[0])
                    + ","
                    + str(info[1])
                    + ","
                    + str(info[2])
                    + "."
                    + " Index:"
                    + str(index)
                )
            res += info[2] - info[1] + 10
        return res

    def drawString(
        self,
        string,
        pos,
        window,
    ):
        sofar = 0
        i = 0
        while i < len(string):
            if string[i] == " ":
                sofar += 20
                i += 1
                continue
            if string[i] in Globals.abc:
                index = Globals.abc.index(string[i])
                info = Globals.charDimensions[index]
            if string[i] in Globals.specialChars:
                index = Globals.specialChars.index(string[i])
                info = Globals.specialCharDimensions[index]
            FontSheet.drawChar(self, string[i], [pos[0] + sofar, pos[1]], window)
            sofar += info[2] - info[1] + 10
            i += 1
