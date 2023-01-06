import pygame
from Item import Item
from Armor import Armor


class ArmorChest(Armor):
    def __init__(self, name, defense, enchantments) -> None:
        super().__init__(name, defense, enchantments)
