from spatial_entity import SpatialEntity
from abc import ABC,abstractmethod
import arcade
import numpy as np
from typing import Tuple,Sequence
from constants import *

class Food(SpatialEntity,ABC):
    has_moustache: bool
    velocity:np.ndarray


    def __init__(self,pos: Tuple[float,float] = None, color: Sequence[int] = None,angle :float = None,image = None):
        super().__init__(pos = pos,color = color,angle = angle,image = image)
        self.velocity=np.array([0,0])

    def update(self, delta_time):
        #x=x_0-0.5gt^2
        #v+=g/dt
        self.velocity = self.velocity + GRAVITY_CONSTANT/delta_time
        self.pos+=self.velocity*delta_time
        if self.y < FLOOR_HEIGHT:
            self.y = FLOOR_HEIGHT

    def draw_general(self,color) -> object:
        x, y = self.pos
        arcade.draw_circle_filled(x,y+20,20,color)

    @property
    def is_on_floor(self):
        return self.y == FLOOR_HEIGHT

class Hasa(Food):
    def draw(self) -> object:
        self.draw_general([0,255,0])

class Strawberry(Food):
    def draw(self) -> object:
        self.draw_general([250, 0,0])

class Lemon(Food):
      def draw(self) -> object:
        self.draw_general([250, 250,0])

def get_all_food_types():
    return Hasa,Strawberry,Lemon


