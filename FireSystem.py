import random
import pygame
from Entity import Entity
from Fire import Fire
from globals import Globals
from map1 import gridMap1
from map2 import gridMap2


class FireSystem:
    def __init__(self, map) -> None:
        self.map = map

        # Creates a cell list - 2D array of the map, marks the last frame a fire was in each cell
        self.mapList = []
        for i in range(31):
            self.mapList.append([])
            for j in range(69):
                self.mapList[i].append(-9999)

    def Update(self, entityList, frameCounter):
        if Globals.currentMap == 0:
            self.mapList = []
            for i in range(31):
                self.mapList.append([])
                for j in range(69):
                    self.mapList[i].append(-9999)
        if Globals.currentMap == 1:
            self.mapList = []
            for i in range(39):
                self.mapList.append([])
                for j in range(79):
                    self.mapList[i].append(-9999)

        self.UpdateCellMap(entityList, frameCounter)
        for entity in entityList:
            if isinstance(entity, Fire):
                randy = random
                dire = randy.randint(0, 3)
                rS = entity.randomSpread
                numb = randy.randint(1, 100)
                comboList = [
                    pygame.Vector2(entity.pos.x, entity.pos.y - 1),
                    pygame.Vector2(entity.pos.x, entity.pos.y + 1),
                    pygame.Vector2(entity.pos.x - 1, entity.pos.y),
                    pygame.Vector2(entity.pos.x + 1, entity.pos.y),
                ]
                place = comboList[dire]
                if (
                    numb <= entity.randomSpread
                    and self.isSpawnable(place, entityList, frameCounter)
                    and entity.generation > 0
                ):
                    entityList.append(Fire(place, entity.generation - 1))

    def UpdateCellMap(self, entityList, frameCounter):
        for i in range(len(entityList)):
            if isinstance(entityList[i], Fire):
                self.mapList[int(entityList[i].pos.y)][
                    int(entityList[i].pos.x)
                ] = frameCounter

    def isSpawnable(self, pos, entityList, frameCounter):
        mapList = self.mapList
        if (
            self.map[int(pos.y)][int(pos.x)] != "X"
            and self.map[int(pos.y)][int(pos.x)] != "W"
            and mapList[int(pos.y)][int(pos.x)] <= frameCounter - 1500
        ):
            return True
        return False
