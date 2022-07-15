class CollisionDetector:
    def BuildCollisionMap(self):
        mapList = []
        for i in range(31):
            mapList.append([])
            for j in range(69):
                mapList[i].append([])
        return mapList

    def Update(self, entityList):
        mapList = self.BuildCollisionMap()

        for i in range(len(entityList)):
            entityY = int(entityList[i].pos.y)
            entityX = int(entityList[i].pos.x)
            collisionCell = mapList[entityY][entityX]
            collisionCell.append(i)

            if len(collisionCell) > 1:
                for i in range(len(collisionCell)):
                    entityList[collisionCell[i]].OnCollide(
                        entityList[collisionCell[-1]]
                    )
                    entityList[collisionCell[-1]].OnCollide(
                        entityList[collisionCell[i]]
                    )
