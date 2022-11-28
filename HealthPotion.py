import pygame
from Item import Item
from globals import Globals


class HealthPotion(Item):
    healthPot = pygame.image.load("Textures\healthPotion.png")
    healthPot = pygame.transform.scale(healthPot, (75, 75))
    picture = healthPot

    def __init__(
        self,
        heal,
    ):
        # super().__init__()
        self.uses = 1
        self.heal = heal
        self.type = "HealthPotion"

    def Update(self):
        super().Update()
        if self.uses > 0:
            Globals.entityList[0].takeDamage(-self.heal)

    def Draw(self):
        super().Draw()
