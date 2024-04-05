from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import NumericProperty
from widgets.junk import Junk

class Junkster(App):
    def build(self):
        game = Junk()
        Window.bind(on_key_down=self.on_key_down)
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

    def on_key_down(self, instance, keyboard, keycode, text, modifiers):
        # Quit the game when the escape key is pressed
        if keycode == 27:  # 27 is the keycode for the escape key
            App.get_running_app().stop()
            return True  # Override the key event

if __name__ == '__main__':
    Junkster().run()
