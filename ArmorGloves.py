import pygame
from Armor import Armor


class ArmorGloves(Armor):
    def __init__(self, name, defense, enchantments) -> None:
        super().__init__(name, defense, enchantments)
