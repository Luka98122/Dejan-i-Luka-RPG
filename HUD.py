import pygame


class Hud:
    heart = pygame.image.load("Textures\Heart.png")
    heart = pygame.transform.scale(heart, (50, 50))
    quickUseSlots = pygame.image.load("Textures\quickUseSlots.png")
    quickUseSlots = pygame.transform.scale(quickUseSlots, (220, 64))

    def __init__(self, window, player) -> None:
        self.window = window
        self.player = player
        pass

    def Draw(self):
        for i in range(self.player.hp // 10):
            self.window.blit(self.heart, (i * 50, 0))
        self.window.blit(self.quickUseSlots, (0, 525))
        for i in range(len(self.player.inventory)):
            if self.player.inventory[i][0].uses > 0:
                self.window.blit(self.player.inventory[i][0].picture, (5 + i * 65, 520))

    def update(self):
        pass