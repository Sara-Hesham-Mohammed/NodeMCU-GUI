import time
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.clock import Clock
from kivy.core.window import Window
from circularprogressbar import CircularProgressBar1, CircularProgressBar2

circularProgressBar1 = CircularProgressBar1()
circularProgressBar2 = CircularProgressBar2()

class runApp(MDApp):
    Window.size = (1280, 720)
    screen_manager = ScreenManager(transition=SlideTransition(duration=6))

    def __init__(self, **kwargs):
        super(runApp, self).__init__(**kwargs)
        self.running = True
        self.splash_screen = Builder.load_file("splashScreen.kv")
        self.run_app_screen = Builder.load_file("runApp.kv")

    def build(self):
        self.title = "BUE RACING TEAM"
        self.screen_manager.add_widget(self.splash_screen)
        self.screen_manager.add_widget(self.run_app_screen)
        return self.screen_manager

    def on_start(self):
        Clock.schedule_once(self.change_screen, 1)
        Clock.schedule_interval(self.update_progress, 0.1)

    def change_screen(self, dt):
        self.screen_manager.current = "runApp"

    def update_progress(self, dt):
        progress1 = self.run_app_screen.ids.circular_progress1
        progress2 = self.run_app_screen.ids.circular_progress2
        if progress1.value < 100:
            progress1.value += 1
        else:
            progress1.value = 0

        if progress2.value > 0:
            progress2.value -= 1
        else:
            progress2.value = 100
            
if __name__ == '__main__':
    runApp().run()
