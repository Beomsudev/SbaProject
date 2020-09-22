from dataclasses import dataclass

@dataclass
class Entity:
    context : str
    fname : str
    train : object
    test : object
    id : str
    label : str