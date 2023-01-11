import pygame
from Armor import Armor
from globals import Textures


class ArmorHelmet(Armor):
    def __init__(self, name, defense, enchantments) -> None:
        self.type = "equipment"
        super().__init__(name, defense, enchantments)
