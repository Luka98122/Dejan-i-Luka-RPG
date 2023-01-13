import pygame
from globals import Textures
from goldCoin import GoldCoin


class Hud:
    heart = Textures.heart
    heart = pygame.transform.scale(heart, (75, 75))
    quickUseSlots = Textures.quickUseSlots
    quickUseSlots = pygame.transform.scale(quickUseSlots, (440, 128))
    SpellHotbar = Textures.SpellHotbar
    SpellHotbar = pygame.transform.scale(SpellHotbar, (440, 128))

    def __init__(self, window, player) -> None:
        self.window = window
        self.player = player
        pass

    def Draw(self):
        # Draw Hearts
        x = 0
        y = 0
        i = 0
        while i < (self.player.hp // 10):
            self.window.blit(self.heart, (x * 75, y * 75))
            i += 1
            x += 1
            if x > 24:
                x = 0
                y += 1

        # Draw QuickUseSlots
        self.window.blit(self.quickUseSlots, (445, 900))
        # self.window.blit(self.quickUseSlots, (490, 525))
        # Draw Items in QuickUseSlots
        starter = 0
        if type(self.player.inventory[0][0]) == GoldCoin:
            starter = 1
        for i in range(starter, len(self.player.inventory)):
            if self.player.inventory[i][0].uses > 0:
                pic = self.player.inventory[i][0].picture
                pic = pygame.transform.scale(pic, (120, 120))
                self.window.blit(pic, (475 + (i - starter) * 130, 900))
            # Only 3 inventory slots, so just break to not draw everything
            if (i - starter) == 2:
                break
        # Draw SpellHotbar
        self.window.blit(self.SpellHotbar, (0, 900))

    def update(self):
        pass
