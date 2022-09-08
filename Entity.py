import CheatFile
from globals import Globals


class Entity:
    sizeofEverything = CheatFile.sizeofEverything

    def __init__(self, pos) -> None:
        self.pos = pos
        self.type = 0
        self.interacted = 0
        self.hp = 20

    def OnCollide(self, other):
        print(f"{self}: collision with {other}")

    # DEBUG

    def Update(self):
        self.Activate()

    def Activate(self):
        pass
        # for i in range(len(entityList)):
        #    if (
        #        self.pos.x == entityList[i].pos.x
        #        and self.pos.y == entityList[i].pos.y
        #        and self.interacted == 0
        #        and entityList[i].type != self.type
        #    ):
        #        self.interacted = 1
        #        if self.type == "trap":
        #            entityList[i].takeDamage(self.damage)
        #        if self.type == "chest":
        #            inventory.append([HealthPotion(10), 1])

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
