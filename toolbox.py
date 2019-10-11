import kivy
import math

from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import *

from comicwidgets import StickMan, DraggableWidget, PacMan, Circle

class ToolButton(ToggleButton):
    def on_touch_down(self,touch):
        draw_space = self.parent.drawing_space
        if self.state == "down" and draw_space.collide_point(touch.x,touch.y):
            x = draw_space.to_widget(touch.x,touch.y)[0]
            y = draw_space.to_widget(touch.x,touch.y)[1]
            self.draw(draw_space,x,y)
            return True
        else:
            return super().on_touch_down(touch)
    
    def draw(self, draw_space,x,y):
        pass

class StickManButton(ToolButton):
    def draw(self,draw_space,x,y):
        stickman = StickMan(width = 48, height = 48)
        stickman.center_x = x
        stickman.center_y = y
        draw_space.add_widget(stickman)


class PacManButton(ToolButton):
    def draw(self, draw_space,x,y):
        pacman = PacMan(width=48,height=48)
        pacman.center_x = x
        pacman.center_y = y
        draw_space.add_widget(pacman)