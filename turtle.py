from spatial_entity import SpatialEntity
from food import Food,get_all_food_types,Strawberry,Hasa,Lemon
import arcade
from typing import Tuple, List, Generator,Type
import numpy as np
from constants import *
import random
from typing import Tuple,Sequence

class Turtle(SpatialEntity):


    name: str
    favorite_food: Type[Food]
    is_on_back: bool
    is_dancing: bool
    is_facing_right: bool
    n_hasa_ate: int
    size: float
    movement_speed: float
    update_generator: Generator
    color: Sequence[int]
    right_texture:arcade.Texture
    left_texture:arcade.Texture

    def __init__(self,sprite_list_owner, name: str = None, x: float = 1, color: Tuple[int, int, int] = None,
                 favorite_food: Food = None, is_facing_right: bool = None, size: float = 1):
        color = (np.array([179, 191, 100]) + np.random.normal(0, 10, 3).astype(int)) % 256
        self.color = color
        self.size = size
        super().__init__(pos = (x, FLOOR_HEIGHT),sprite_list_owner = sprite_list_owner)
        self.is_on_back = False
        self.is_dancing = False
        self.n_hasa_ate = 0
        self.movement_speed = 100 + np.random.normal(0, 10)
        self.is_facing_right = True
        self.update_generator = None
        if favorite_food is None:
            self.favorite_food = random.choice([Strawberry,Lemon])
        else:
            self.favorite_food = favorite_food

    def make_sprite(self):
        sprite = self.make_sprite_from_file(scale=self.size)
        self.right_texture = arcade.load_texture("images/Turtle.png", mirrored=True)
        self.left_texture = arcade.load_texture("images/Turtle.png", mirrored=False)
        return sprite

    def get_head_position(self):
        r = self.head_distance_from_pos
        if self.is_facing_right:
            return self.x + r
        else:
            return self.x - r

    def update_sprite(self):
        super().update_sprite()
        if self.is_facing_right:
            self.sprite.texture = self.right_texture
        else:
            self.sprite.texture = self.left_texture

    @property
    def head_distance_from_pos(self):
        return self.sprite.width/2

    def update(self, delta_time, foods_array: List[Food]):
        if self.update_generator is None:
            self.update_generator = self.update_generator_maker(delta_time, foods_array)
            next(self.update_generator)
        else:
            self.update_generator.send(delta_time)
        self.update_sprite()

    # contain turtle movment logic
    def update_generator_maker(self, delta_time, foods_array: List[Food]):
        while True:
            while True:
                delta_time = yield
                # find food
                targeted_eating_spot, targeted_food = self.get_optimal_eating_spot(delta_time, foods_array)
                if targeted_eating_spot is None:
                    continue
                # go to food
                b_reached_target = self.move_toward_target(targeted_eating_spot, delta_time)
                if not targeted_food in foods_array or b_reached_target:
                    break
            if targeted_food not in foods_array:
                continue

            # turn around
            if targeted_food.x > self.x:
                self.is_facing_right = True
            else:
                self.is_facing_right = False

            # eat food
            if targeted_food.is_on_floor:
                print("tziffffff")
                foods_array.remove(targeted_food)
                del targeted_food
                time_accum = 0
                while time_accum < 1:
                    delta_time = yield
                    time_accum += delta_time

    def move_toward_target(self, target_x, delta_time):
        if target_x - self.x < - 10:
            self.x -= self.movement_speed * delta_time
            self.is_facing_right = False
            return False
        elif target_x - self.x > 10:
            self.x += self.movement_speed * delta_time
            self.is_facing_right = True
            return False
        else:
            return True

    def turn_toward_dir(self,target_dir_is_facing_right:bool):
        pass

    def get_eta(self, final_x, is_facing_right_final):
        eta = abs(final_x - self.x)
        return eta

    def get_optimal_eating_spot(self, delta_time, foods_array: List[Food]):
        # find food
        all_eating_spots = self.get_list_of_eating_spots(foods_array)
        if len(all_eating_spots)==0:
            return None,None
        list_of_eating_spots_scores = [self.get_food_spot_score(eating_spot_x,is_facing_right,food) for eating_spot_x,is_facing_right,food in all_eating_spots]
        index_of_minimal_eta = int(np.argmax(list_of_eating_spots_scores))
        targeted_food = all_eating_spots[index_of_minimal_eta][2]
        targeted_eating_spot = all_eating_spots[index_of_minimal_eta][0]
        return targeted_eating_spot, targeted_food

    def get_food_spot_score(self, final_x, is_facing_right_final,food):
        eta = self.get_eta(final_x,is_facing_right_final)
        if isinstance(food,self.favorite_food):
            score = 1 / eta
        else:
            score = - eta
        return score

    def get_list_of_eating_spots(self, foods_array: List[Food]):
        spot_gap = self.head_distance_from_pos
        return [(cur_food.x + spot_gap * side, side == 1, cur_food) for cur_food in foods_array if cur_food.is_on_floor for side in [1, -1]]