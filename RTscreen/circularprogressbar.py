from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty
from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_string('''
<CircularProgressBar1>:
    canvas:
        Color:
            rgba: self.color[0], self.color[1], self.color[2], 0.05
        Line:
            circle: (self.center_x, self.center_y, self.radius + 8, 180, 180 + self.angle)
            width: self.line_width + 16
        Color:
            rgba: self.color[0], self.color[1], self.color[2], 0.1
        Line:
            circle: (self.center_x, self.center_y, self.radius + 6, 180, 180 + self.angle)
            width: self.line_width + 12
        Color:
            rgba: self.color[0], self.color[1], self.color[2], 0.2
        Line:
            circle: (self.center_x, self.center_y, self.radius + 4, 180, 180 + self.angle)
            width: self.line_width + 8
        Color:
            rgba: self.color[0], self.color[1], self.color[2], 0.4
        Line:
            circle: (self.center_x, self.center_y, self.radius + 2, 180, 180 + self.angle)
            width: self.line_width + 4
        Color:
            rgba: self.color
        Line:
            circle: (self.center_x, self.center_y, self.radius, 180, 180 + self.angle)
            width: self.line_width

<CircularProgressBar2>:
    canvas:
        Color:
            rgba: self.color[0], self.color[1], self.color[2], 0.05
        Line:
            circle: (self.center_x, self.center_y, self.radius + 8, 0, self.angle)
            width: self.line_width + 16
        Color:
            rgba: self.color[0], self.color[1], self.color[2], 0.1
        Line:
            circle: (self.center_x, self.center_y, self.radius + 6, 0, self.angle)
            width: self.line_width + 12
        Color:
            rgba: self.color[0], self.color[1], self.color[2], 0.2
        Line:
            circle: (self.center_x, self.center_y, self.radius + 4, 0, self.angle)
            width: self.line_width + 8
        Color:
            rgba: self.color[0], self.color[1], self.color[2], 0.4
        Line:
            circle: (self.center_x, self.center_y, self.radius + 2, 0, self.angle)
            width: self.line_width + 4
        Color:
            rgba: self.color
        Line:
            circle: (self.center_x, self.center_y, self.radius, 0, self.angle)
            width: self.line_width
''')

class CircularProgressBar1(Widget):
    value = NumericProperty(0)
    line_width = NumericProperty(2)
    radius = NumericProperty(163)
    angle = NumericProperty(0)
    color = ListProperty([0.98, 0.058, 0.75, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_angle, 0.1)

    def update_angle(self, *args):
        self.angle = (self.value / 100) * 360

class CircularProgressBar2(Widget):
    value = NumericProperty(100)
    line_width = NumericProperty(2)
    radius = NumericProperty(163)
    angle = NumericProperty(0)
    color = ListProperty([0.98, 0.058, 0.75, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_angle, 0.1)

    def update_angle(self, *args):
        self.angle = (self.value / 100) * 360
    