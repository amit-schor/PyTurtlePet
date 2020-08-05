from spatial_entity import SpatialEntity
from abc import ABC,abstractmethod
import arcade
import numpy as np
from typing import Tuple,Sequence
from constants import *

class Food(SpatialEntity,ABC):
    has_moustache: bool
    velocity:np.ndarray


    def __init__(self,sprite_list_owner,pos: Tuple[float,float] = None,angle :float = None):
        super().__init__(sprite_list_owner= sprite_list_owner,pos = pos,angle = angle)
        self.velocity=np.array([0,0])

    def update(self, delta_time):
        self.velocity = self.velocity + GRAVITY_CONSTANT/delta_time
        self.pos+=self.velocity*delta_time
        if self.y < FLOOR_HEIGHT:
            self.y = FLOOR_HEIGHT
        self.update_sprite()

    @property
    def is_on_floor(self):
        return self.y == FLOOR_HEIGHT


class Hasa(Food):
    def make_sprite(self):
        return self.make_sprite_from_file("images/Lettuce.png")


class Strawberry(Food):
    def make_sprite(self):
        return self.make_sprite_from_file("images/Strawberry.png")


class Lemon(Food):
    def make_sprite(self):
        return self.make_sprite_from_file("images/Lemon.png")


def get_all_food_types():
    return Hasa,Strawberry,Lemon


