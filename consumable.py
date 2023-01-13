import pygame
from Item import Item


class Consumable(Item):
    def __init__(self) -> None:
        self.uses = 0
        super().__init__()
