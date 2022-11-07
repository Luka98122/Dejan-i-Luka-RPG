import pygame
from TextWindow import TextWindow
from FontSheet import FontSheet


class DialogueSystem:
    listOfTextWindows = []

    def __init__(self) -> None:
        pass

    def draw(self, window):
        for i in range(len(DialogueSystem.listOfTextWindows)):
            DialogueSystem.listOfTextWindows[i].draw(window)

    def addWindow(self, pos, text):
        width = FontSheet.getLenOfString(text) + 70
        height = 100
        textWindow = TextWindow(width, height, pos, text)
        DialogueSystem.listOfTextWindows.append(textWindow)
