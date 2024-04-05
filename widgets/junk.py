
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.clock import Clock
from random import randint
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.properties import NumericProperty
class Junk(Widget):
    ball_speed_x = NumericProperty(5)
    ball_speed_y = NumericProperty(5)

    def __init__(self, **kwargs):
        super(Junk, self).__init__(**kwargs)
        self.ball = Label(text='o', font_size='40sp')
        self.score = 0
        self.junk_speed = 1
        self.create_junk()
        self.update_label()
        self.add_widget(self.ball)
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def create_junk(self):
        self.junk = Image(source='space_junk.png', pos=(randint(0, self.width - 50), self.height), size=(50, 50))
        self.add_widget(self.junk)

    def update_label(self):
        self.label = Label(text=f'Score: {self.score}', pos=(0, self.height - 30))
        self.add_widget(self.label)

    def on_touch_down(self, touch):
        if self.junk.collide_point(*touch.pos):
            self.score += 1
            self.remove_widget(self.junk)
            self.create_junk()
            self.remove_widget(self.label)
            self.update_label()

    def update(self, dt):
        self.junk.y -= self.junk_speed
        if self.junk.y < 0:
            self.remove_widget(self.junk)
            self.create_junk()
            self.score -= 1
            if self.score < 0:
                self.score = 0
            self.remove_widget(self.label)
            self.update_label()

    # def update(self, dt):
    #     self.ball.x += self.ball_speed_x
    #     self.ball.y += self.ball_speed_y

    #     # Bounce off the walls
    #     if (self.ball.x < 0) or (self.ball.x + self.ball.width > self.width):
    #         self.ball_speed_x *= -1
    #     if (self.ball.y < 0) or (self.ball.y + self.ball.height > self.height):
    #         self.ball_speed_y *= -1
