from titanic.service import Service
from titanic.entity import Entity


class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()

        