from Entity import Entity


class EnemySpawner(Entity):
    def __init__(self, pos) -> None:
        super().__init__(pos)

    def Draw(self, picture, window, cameraOffset):
        return super().Draw(picture, window, cameraOffset)

    def Update(self):
        return super().Update()

    def OnCollide(self, other):
        return super().OnCollide(other)
