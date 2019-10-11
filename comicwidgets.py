from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Line

class DraggableWidget(RelativeLayout):
    def __init__(self):
        self.selected = None
        super().__init__()

    def select(self):
        if self.selcted == False:
            self.ix = self.center_x
            self.iy = self.center_y
            with self.canvas:
                self.selected = Line(rectangle=(0,0,self.width,slef.height),dash_offset=2)

    def on_touch_down(self,touch):
        x = self.parent.to_parent(touch.x, touch.y)[0]
        y = self.parent.to_parent(touch.x, touch.y)[1]
        if self.selected == True and self.parent.collide_point(x-self.width/2, y-self.heght/2):
            self.translate(touch.x-self.ix,touch.y-self.iy)
            return True
        return super().on_touch_move(touch)

    def translate(self,x,y):
        self.center_x = self.ix
        self.center_y = self.iy
        self.ix += x
        self.iy += y

    def on_touch_up(self,touch):
        if self.selected == True:
            self.unselect()
            return True
        return super().on_touch_up(touch)

    def unselect(self):
        if self.selected == True:
            self.canvas.remove(self.selected)
            self.selected = None

class StickMan(DraggableWidget):
    pass
