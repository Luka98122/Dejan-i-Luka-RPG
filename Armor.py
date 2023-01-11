import pygame
from Item import Item
from globals import Textures


class Armor(Item):
    def __init__(self, name, defense, enchantments) -> None:
        self.name = name
        self.defense = defense
        self.enchantments = enchantments
        self.shopName = name
        self.type = "equipment"
        super().__init__()
