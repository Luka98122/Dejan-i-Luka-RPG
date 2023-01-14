import pygame
from globals import Globals
from globals import Textures
from Item import Item


class GoldCoin(Item):
    def __init__(self) -> None:
        super().__init__()
        self.shopName = "Gold Coin"
        self.picture = Textures.goldCoin
        self.maxStack = 2147483646
