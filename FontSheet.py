import pygame
from PIL import Image


class FontSheet:
    textSheetCaps = pygame.image.load("Textures\\TextFontSheet.png")
    fontSheets = [textSheetCaps]
    charsInfo = [[0, 24, 0]]
    abc = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self) -> None:
        pass

    charDimensions = [[], [], [], []]

    def getDimensions(self):
        height = 32
        pixelCursor = pygame.Vector2(0, 0)
        image = Image.open("Textures\\TextFontSheet.png")
        pixels = image.load()
        j = 0
        layer = 0
        for z in range(1, 26):
            currentLength = 0
            switch = 1
            while j < image.size[0]:
                for i in range(32):
                    if pixels[j, i + layer * 40][3] != 0:
                        switch = 0
                        j += 1
                        break
            if switch == 1:
                print(j)
                FontSheet.charsInfo.append([j + 8, currentLength, layer])
                j += 8
                print("")
                continue
            j += 1
            if j >= image.size[0]:
                print(j)
                FontSheet.charsInfo.append([j + 8, currentLength + 1, layer])
                j = 0
                layer += 1
                currentLength = -1
            if layer == 2:
                break
            currentLength += 1
        print(FontSheet.charsInfo)

    def drawChar(self, char, pos, window):
        index = FontSheet.abc.index(char)
        info = FontSheet.charsInfo[index]
        window.blit(
            FontSheet.textSheetCaps,
            pygame.Rect(pos[0], pos[1], info[1], 32),
            (info[0], info[2] * 40, info[1], 32),
        )

    def drawString(self, string, pos, window):
        for i in range(len(string)):
            if string[i] == " ":
                continue
            FontSheet.drawChar(self, string[i], [pos[0] + 30 * i, pos[1]], window)
