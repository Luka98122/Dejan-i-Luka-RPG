import pygame


class Hud:
    heart = pygame.image.load("Textures\Heart.png")
    heart = pygame.transform.scale(heart, (50, 50))
    quickUseSlots = pygame.image.load("Textures\QuickUseSlots.png")
    quickUseSlots = pygame.transform.scale(quickUseSlots, (220, 64))
    SpellHotbar = pygame.image.load("Textures\SpellHotbar.png")
    SpellHotbar = pygame.transform.scale(SpellHotbar, (220, 64))

    def __init__(self, window, player) -> None:
        self.window = window
        self.player = player
        pass

    def Draw(self):
        # Draw Hearts
        for i in range(self.player.hp // 10):
            self.window.blit(self.heart, (i * 50, 0))

        # Draw QuickUseSlots
        self.window.blit(self.quickUseSlots, (245, 525))
        # self.window.blit(self.quickUseSlots, (490, 525))
        # Draw Items in QuickUseSlots
        for i in range(len(self.player.inventory)):
            if self.player.inventory[i][0].uses > 0:
                self.window.blit(
                    self.player.inventory[i][0].picture, (250 + i * 65, 520)
                )
        # Draw SpellHotbar
        self.window.blit(self.SpellHotbar, (0, 525))

    def update(self):
        pass
