from xml.dom.minidom import Entity
import pygame


class Portal(Entity):
    def __init__(self, pos, number) -> None:
        super().__init__(self, pos, number)
