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
        for i in range(len(self.player.inventory)):
            if self.player.inventory[i][0].uses > 0:
                pic = self.player.inventory[i][0].picture
                pic = pygame.transform.scale(pic, (120, 120))
                self.window.blit(pic, (475 + i * 130, 900))
        # Draw SpellHotbar
        self.window.blit(self.SpellHotbar, (0, 900))

    def update(self):
        pass
