from kivy.uix.widget import Widget
from kivy.graphics import Color, Line

class DrawingWidget(Widget):
  def on_touch_down(self, touch):
    with self.canvas:
        Color(1, 0, 0)  # Set color to red
        touch.ud['line'] = Line(points=(touch.x, touch.y))

  def on_touch_move(self, touch):
    touch.ud['line'].points += [touch.x, touch.y]
