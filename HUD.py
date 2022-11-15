import pygame


class Hud:
    heart = pygame.image.load("Textures\Heart.png")
    heart = pygame.transform.scale(heart, (75, 75))
    quickUseSlots = pygame.image.load("Textures\QuickUseSlots.png")
    quickUseSlots = pygame.transform.scale(quickUseSlots, (440, 128))
    SpellHotbar = pygame.image.load("Textures\SpellHotbar.png")
    SpellHotbar = pygame.transform.scale(SpellHotbar, (440, 128))

    def __init__(self, window, player) -> None:
        self.window = window
        self.player = player
        pass

    def Draw(self):
        # Draw Hearts
        for i in range(self.player.hp // 10):
            self.window.blit(self.heart, (i * 75, 0))

        # Draw QuickUseSlots
        self.window.blit(self.quickUseSlots, (445, 900))
        # self.window.blit(self.quickUseSlots, (490, 525))
        # Draw Items in QuickUseSlots
        for i in range(len(self.player.inventory)):
            if self.player.inventory[i][0].uses > 0:
                pic = self.player.inventory[i][0].picture
                pic = pygame.transform.scale(pic, (120, 120))
                self.window.blit(pic, (475 + i * 130, 900))
        # Draw SpellHotbar
        self.window.blit(self.SpellHotbar, (0, 900))

    def update(self):
        pass
