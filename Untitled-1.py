# ---------------------------"STRUKTURA"-----------------
import pygame
import sys
from pygame.math import Vector2

pygame.init()
Xres, Yres = 1280, 720
prozor = pygame.display.set_mode((Xres, Yres))
sat = pygame.time.Clock()
pygame.display.set_caption("Little Jumper")
pygame.mouse.set_visible(False)
cursor = pygame.image.load("Slike/main_menu/cursor.png")
cursor = pygame.transform.scale(cursor, (50, 50))
# -----------------KLASE-------------------------
class Dugme:
    def __init__(self, slika, pozicija):
        self.slika = slika
        self.pozicija = pozicija

    def draw(self):
        self.slika = pygame.transform.smoothscale(self.slika, (200, 150))
        prozor.blit(self.slika, self.pozicija)


class Player:
    def __init__(self, slika, pozicija: Vector2, brzina: Vector2, gravity: bool):
        self.slika = slika
        self.pozicija = pozicija
        self.brzina = brzina
        self.gravity = gravity

    def move(self):
        if self.gravity:
            self.brzina.y += 0.3
        self.pozicija += self.brzina
        dugmici = pygame.key.get_pressed()
        if dugmici[pygame.K_d]:
            self.pozicija.x += 5
        if dugmici[pygame.K_a]:
            self.pozicija.x -= 5
        # if dugmici[pygame.K_s]

    def draw(self):
        prozor.blit(self.slika, self.pozicija)
        self.move()


igrac = Player(
    pygame.image.load("Slike/tutorial/player.png"), Vector2(0, 0), Vector2(0, 0), True
)
igrac.slika = pygame.transform.scale(igrac.slika, (150, 150))

# -----------------DUGMICI----------------------------

settings_dugme = Dugme(pygame.image.load("Slike/main_menu/settings.png"), (550, 480))
backtomainmenu = Dugme(
    pygame.image.load("Slike/settings/backtomainmenu.png"), (20, 520)
)
play_button = Dugme(pygame.image.load("Slike/main_menu/playbutton.png"), (550, 300))
# --------------------GAME LOOPOVI-------------------


def main_menu():
    program_radi = True
    while program_radi:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                program_radi = False
                sys.exit()
            if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
                if (
                    settings_dugme.slika.get_rect()
                    .move(settings_dugme.pozicija)
                    .collidepoint(dogadjaj.pos)
                ):
                    settings()
                if (
                    play_button.slika.get_rect()
                    .move(play_button.pozicija)
                    .collidepoint(dogadjaj.pos)
                ):
                    tutorial()

        prozor.blit(
            pygame.image.load("Slike/main_menu/mainmenu_background.jpg"), (0, 0)
        )
        settings_dugme.draw()
        play_button.draw()
        prozor.blit(cursor, pygame.mouse.get_pos())
        """
        vas kod
        """

        pygame.display.flip()
        sat.tick(30)

    pygame.quit()


def settings():
    program_radi = True
    while program_radi:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                program_radi = False
                sys.exit()
            if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
                if (
                    backtomainmenu.slika.get_rect()
                    .move(backtomainmenu.pozicija)
                    .collidepoint(dogadjaj.pos)
                ):
                    return

        background = pygame.image.load("Slike/settings/settings_background.jpg")
        background = pygame.transform.smoothscale(background, (1280, 720))
        prozor.blit(background, (0, 0))

        backtomainmenu.draw()

        """
        vas kod
        """
        prozor.blit(cursor, pygame.mouse.get_pos())
        pygame.display.flip()
        sat.tick(30)

    pygame.quit()


def tutorial():
    program_radi = True
    while program_radi:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                program_radi = False

        prozor.fill((0, 0, 0))
        igrac.draw()

        pygame.display.flip()
        sat.tick(30)

    pygame.quit()


main_menu()
