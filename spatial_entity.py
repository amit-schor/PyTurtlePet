from typing import Tuple,Sequence
import numpy as np
from abc import ABC,abstractmethod

class SpatialEntity(ABC):
    pos: np.ndarray
    color: Sequence[int]
    angle:float
    image:object

    def __init__(self,pos: Tuple[float,float] = None, color: Sequence[int] = None,angle :float = None,image = None):
        self.pos = np.array(pos,dtype=float)
        self.color = color
        self.angle = angle
        self.image = image

    @property
    def x(self):
        return self.pos[0]

    @x.setter
    def x(self,val):
        self.pos[0] = val

    @property
    def y(self):
        return self.pos[1]

    @y.setter
    def y(self,val):
        self.pos[1] = val

    def draw(self):
        pass