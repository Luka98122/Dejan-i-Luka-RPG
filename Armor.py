import pygame
from Item import Item


class Armor(Item):
    def __init__(self, name, defense, enchantments) -> None:
        self.name = name
        self.defense = defense
        self.enchantments = enchantments
        self.shopName = name
        super().__init__()
