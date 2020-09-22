from service import Service
from entity import Entity


class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()

    
    def preprocessing(self):
        pass

    def modeling(self):
        pass

    def learning(self): # + evaluation
        pass

    def submit(self):   # 파일로 저장
        pass    