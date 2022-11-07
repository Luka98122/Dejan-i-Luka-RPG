import pygame
from TextWindow import TextWindow


class DialogueSystem:
    listOfTextWindows = []

    def __init__(self) -> None:
        pass

    def draw(self, window):
        for i in range(len(DialogueSystem.listOfTextWindows)):
            DialogueSystem.listOfTextWindows[i].draw(window)

    def addWindow(self, width, height, pos, text):
        textWindow = TextWindow(width, height, pos, text)
        DialogueSystem.listOfTextWindows.append(textWindow)
