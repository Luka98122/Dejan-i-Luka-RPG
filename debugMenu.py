import pygame
from globals import Globals
from globals import Textures
from DialogueSystem import DialogueSystem

dialogueSystem = DialogueSystem


class DebugMenu:
    def act(actionParams):
        pass

    def Update(self, cx, cy, multiplier1, multiplier2):
        if Globals.toggleDebugMenu == 0:
            return
        self.cx = cx
        self.cy = cy
        self.multiplier1 = multiplier1
        self.multiplier2 = multiplier2
        pass

    def Draw(self):
        if Globals.toggleDebugMenu == 0:
            return
        dialogueSystem.addWindow(
            dialogueSystem,
            pygame.Vector2(100, 200),
            f"cx:{self.cx}",
            [1, 5],
            self.act,
            {"healthy": 2},
        )
        dialogueSystem.addWindow(
            dialogueSystem,
            pygame.Vector2(100, 280),
            f"cy:{self.cy}",
            [1, 5],
            self.act,
            {"healthy": 2},
        )
        dialogueSystem.addWindow(
            dialogueSystem,
            pygame.Vector2(100, 360),
            f"multiplier1:{round(self.multiplier1,2)}",
            [1, 5],
            self.act,
            {"healthy": 2},
        )
        dialogueSystem.addWindow(
            dialogueSystem,
            pygame.Vector2(100, 440),
            f"multiplier2:{self.multiplier2}",
            [1, 5],
            self.act,
            {"healthy": 2},
        )
