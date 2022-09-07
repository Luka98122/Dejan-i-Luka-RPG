import pygame
from Item import Item


class HealthPotion(Item):
    healthPot = pygame.image.load("Textures\healthPotion.png")
    healthPot = pygame.transform.scale(healthPot, (75, 75))
    picture = healthPot

    def __init__(self, heal, player):
        # super().__init__()
        self.uses = 1
        self.heal = heal
        self.player = player
        self.type = "HealthPotion"

    def Update(self):
        super().Update()
        if self.uses > 0:
            self.player.takeDamage(-self.heal)

    def Draw(self):
        super().Draw()
