class Entity:
    def __init__(self, pos) -> None:
        self.pos = pos
        self.type = 0
        self.interacted = 0
        self.hp = 0

    def Update(self):
        self.Activate()
        self.Draw()

    def Activate(self):
        for i in range(len(entityList)):
            if (
                self.pos.x == entityList[i].pos.x
                and self.pos.y == entityList[i].pos.y
                and self.interacted == 0
                and entityList[i].type != self.type
            ):
                self.interacted = 1
                if self.type == "trap":
                    entityList[i].takeDamage(self.damage)
                if self.type == "chest":
                    inventory.append([HealthPotion(10), 1])

    def Draw(self, picture):
        window.blit(
            picture,
            (
                self.pos.x * 100 - int(cameraOffset.x) * 100,
                self.pos.y * 100 - int(cameraOffset.y) * 100,
            ),
        )

    def takeDamage(self, damage):
        self.hp -= damage
