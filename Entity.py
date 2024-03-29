import CheatFile
from globals import Globals


class Entity:
    sizeofEverything = CheatFile.sizeofEverything

    def __init__(self, pos) -> None:
        self.pos = pos
        self.type = "entity"
        self.interacted = 0
        self.hp = 20

    def OnCollide(self, other):
        # print(f"{self}: collision with {other}")
        pass

    # DEBUG

    def Update(self):
        self.Activate()
        # Does nohing

    def Activate(self):
        pass

    def Draw(
        self,
        picture,
        window,
        cameraOffset,
    ):

        window.blit(
            picture,
            (
                self.pos.x * Globals.sizeofEverything
                - int(cameraOffset.x) * Globals.sizeofEverything,
                self.pos.y * Globals.sizeofEverything
                - int(cameraOffset.y) * Globals.sizeofEverything,
            ),
        )

    def takeDamage(self, damage):
        self.hp -= damage
