import pygame
from TextWindow import TextWindow
from FontSheet import FontSheet
from globals import Globals


class DialogueSystem:
    listOfTextWindows = []

    def __init__(self) -> None:
        pass

    def draw(self, window):
        for i in range(len(DialogueSystem.listOfTextWindows)):
            DialogueSystem.listOfTextWindows[i].draw(window)
        pygame.display.flip()

    def update(self):
        i = 0
        while i < len(DialogueSystem.listOfTextWindows):
            if DialogueSystem.listOfTextWindows[i].lifeSpan <= 0:
                DialogueSystem.listOfTextWindows.remove(
                    DialogueSystem.listOfTextWindows[i]
                )
                i -= 1
            i += 1
        i = 0
        for i in range(len(DialogueSystem.listOfTextWindows)):
            DialogueSystem.listOfTextWindows[i].update()
        self.clickedOn()

    def addWindow(self, pos, text, additionalParameters, speaker):
        width = FontSheet.getLenOfString(text) + 70
        height = 80
        textWindow = TextWindow(width, height, pos, text, additionalParameters, speaker)
        DialogueSystem.listOfTextWindows.append(textWindow)

    def addChoice(self, poss, texts, additionalParameters, speakers):
        pos1 = poss[0]
        pos2 = poss[1]
        text1 = texts[0]
        text2 = texts[1]
        additionalParameters1 = additionalParameters[0]
        additionalParameters2 = additionalParameters[1]
        speaker1 = speakers[0]
        speaker2 = speakers[1]
        DialogueSystem.addWindow(pos1, text1, additionalParameters1, speaker1)
        DialogueSystem.addWindow(pos2, text2, additionalParameters2, speaker2)

    def clickedOn(self):
        for txtWindow in self.listOfTextWindows:
            print(Globals.events)
            for event in Globals.events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if (
                        mouse[0] > txtWindow.pos.x
                        and mouse[0] < txtWindow.pos.x + txtWindow.width
                    ):
                        if (
                            mouse[1] > txtWindow.pos.y
                            and mouse[1] < txtWindow.pos.y + txtWindow.height
                        ):
                            Globals.entityList[0].hp += 10
