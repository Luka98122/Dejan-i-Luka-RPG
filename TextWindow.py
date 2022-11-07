import pygame
from FontSheet import FontSheet

fontSheet = FontSheet()
fontSheet.getDimensions()


class TextWindow:
    textBox = pygame.image.load("textures\\TextBox1.png")

    def __init__(self, width, height, pos, text):
        self.image = pygame.transform.scale(TextWindow.textBox, (width, height))
        self.x = pos.x
        self.y = pos.y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, window):
        window.blit(self.image, pygame.Rect(self.x, self.y, self.width, self.height))
        fontSheet.drawString(
            self.text, [self.x + 10, (self.y + self.height) / 2], window
        )
