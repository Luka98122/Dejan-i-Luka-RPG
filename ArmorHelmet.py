import pygame
from Armor import Armor


class ArmorHelmet(Armor):
    def __init__(self, name, defense, enchantments) -> None:
        super().__init__(name, defense, enchantments)
