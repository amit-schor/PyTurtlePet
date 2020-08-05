from typing import Tuple,Sequence
import numpy as np
from abc import ABC,abstractmethod
import arcade

class SpatialEntity(ABC):
    pos: np.ndarray
    angle:float
    sprite:arcade.Sprite

    def __init__(self,pos: Tuple[float,float],sprite_list_owner:arcade.SpriteList,angle :float = 0):
        self.pos = np.array(pos,dtype=float)
        self.angle = angle
        self.sprite = self.make_sprite()
        sprite_list_owner.append(self.sprite)

    def __del__(self):
        self.sprite.remove_from_sprite_lists()

    @abstractmethod
    def make_sprite(self) -> arcade.Sprite:
        pass

    def make_sprite_from_file(self,file_name=None,**kwargs):
        return arcade.Sprite(file_name, center_x=self.x, center_y=self.y,**kwargs)

    def update_sprite(self):
        self.sprite.center_x = self.x
        self.sprite.center_y = self.y + self.sprite.height/2

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

    # def draw(self):
    #     pass