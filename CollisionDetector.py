import globals


class CollisionDetector:
    def BuildCollisionMap(self):
        mapList = []
        if globals.Globals.currentMap == 0:
            for i in range(31):
                mapList.append([])
                for j in range(69):
                    mapList[i].append([])
        if globals.Globals.currentMap == 1:
            self.mapList = []
            for i in range(39):
                mapList.append([])
                for j in range(79):
                    mapList[i].append([])
        return mapList

    def Update(self, entityList):
        mapList = self.BuildCollisionMap()
        for i in range(len(entityList)):
            entityY = int(entityList[i].pos.y)
            entityX = int(entityList[i].pos.x)
            collisionCell = mapList[entityY][entityX]
            collisionCell.append(entityList[i])

            if len(collisionCell) > 1:
                for i in range(len(collisionCell)):
                    collisionCell[i].OnCollide(collisionCell[-1])
                    collisionCell[-1].OnCollide(collisionCell[i])
