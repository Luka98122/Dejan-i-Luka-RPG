import pygame
from globals import Textures


class Item:
    def __init__(self) -> None:
        self.uses = 1
        self.type = 0

    def Update(self):
        pass

    def Draw(self):
        pass
