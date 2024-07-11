from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.clock import Clock
from kivy.core.window import Window

class runApp(MDApp):
    Window.size = (1280, 720)
    screen_manager = ScreenManager(transition=SlideTransition(duration=1.5))

    def __init__(self, **kwargs):
        super(runApp, self).__init__(**kwargs)
    def build(self):
        # ... (rest of the build function)
        self.title = "BUE RACING TEAM"
        self.splash_screen = Builder.load_file("splashScreen.kv")
        self.run_app_screen = Builder.load_file("runApp.kv")
        self.screen_manager.add_widget(self.splash_screen)
        self.screen_manager.add_widget(self.run_app_screen)
        return self.screen_manager

    def on_start(self):
        # Delay time for splash screen before transitioning to main screen
        Clock.schedule_once(self.change_screen, 3)
        # Update progress bars directly on the main thread (no thread pool needed)
        Clock.schedule_interval(self.update_progress, 0.01)
        # Leverage signals from mediator for efficient updates

    def update_progress(self, dt):
        progress1 = self.run_app_screen.ids.circular_progress1
        progress2 = self.run_app_screen.ids.circular_progress2
        if progress1.value < 100 or progress2.value < 100:
            progress1.value += 1
            progress2.value += 1
        else:
            progress1.value = 0
            progress2.value = 0

    def change_screen(self, dt):
        self.screen_manager.current = "runApp"

if __name__ == '__main__':
    runApp().run()
