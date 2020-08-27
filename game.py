import arcade
from turtle import Turtle,Type
from food import Food, Hasa,Strawberry,Lemon
import math as mp
import random
from typing import List
import constants


class MyGame(arcade.Window):
    turtles_array:List[Turtle]
    foods_array:List[Food]
    food_creation_frequency_sec = 1
    food_creation_timer = 0
    sprite_list:arcade.SpriteList

    def __init__(self):
        w_size = 1920, 1000
        """ Initializer """
        # Call the parent class initializer
        super().__init__(*w_size, title="Sprite Example")
        arcade.set_background_color((255,240,240))
        self.sprite_list = arcade.SpriteList()


    def setup(self):
        # n_turt_x, n_turt_y = 10, 6
        # self.turtles_array = [Turtle(name="tzav", x=600, size=300),Turtle(name="tzavi", x=100, size=100),Turtle(name="tzavitzav", x=0, size=10),Turtle(name="tzavitzav", x=10 , size=5)]
        self.turtles_array = [Turtle(sprite_list_owner=self.sprite_list, name="tzav", x=0, size=3.0),Turtle(sprite_list_owner=self.sprite_list, name="tzavi", x=500, size=1.8),Turtle(sprite_list_owner=self.sprite_list, name="tzavitzav", x=1200, size=1),Turtle(sprite_list_owner=self.sprite_list, name="tzavitzav", x=1900 , size=2.3)]
        # self.turtles_array = [Turtle(name="tzav", x=600, size=100),Turtle(name="tzavi", x=600, size=100)]
        # self.turtles_array[0].movement_speed=self.turtles_array[1].movement_speed


        self.foods_array = []

    def update(self, delta_time):
        for turtle in self.turtles_array:
            turtle.update(delta_time,self.foods_array)
        for food in self.foods_array:
            food.update(delta_time)
        if self.food_creation_timer > 0:
            self.food_creation_timer -= delta_time
        else:
            self.food_creation_timer=self.food_creation_frequency_sec
            chosen_food:Type[Food] = random.choices([Hasa,Strawberry,Lemon],weights=(0.8,0.1,0.1))[0]
            self.foods_array.append(chosen_food(sprite_list_owner=self.sprite_list,pos=(random.uniform(0,self.get_size()[0]), 800)))
            # if random.choices([True,False],weights=(0.9,0.1))[0]:
            #     self.foods_array.append(Hasa(pos=(random.uniform(0,self.get_size()[0]), 800)))
            # else:
            #     self.foods_array.append(Strawberry(pos=(random.uniform(0, self.get_size()[0]), 800)))

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(0, self.get_size()[0], constants.FLOOR_HEIGHT, 0, [30, 150, 40])
        self.sprite_list.draw(filter=constants.GL_NEAREST)


window = MyGame()
window.setup()
arcade.run()
