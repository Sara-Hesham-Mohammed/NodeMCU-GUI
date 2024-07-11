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

kv = '''
MDScreen:
    orientation: 'vertical'
    padding: 10
    md_bg_color: 0, 0, 0, 1
    name:"runApp"
    
    MDFloatLayout: 
        
        Image:
            source:'Images/bckg.jpg'
            allow_stretch: True
            keep_ratio: True
        
    MDFloatLayout:
        CircularProgressBar1:
            id: circular_progress1
            size_hint: None, None
            size: dp(300), dp(300)
            pos_hint: {'center_x': .19, 'center_y': .525}
            line_width: dp(2)
            color: [252/255, 15/255, 192/255, 1]  # Pink color in RGBA
        CircularProgressBar2:
            id: circular_progress2
            size_hint: None, None
            size: dp(300), dp(300)
            pos_hint: {'center_x': .815, 'center_y': .525}
            line_width: dp(2)
            color: [252/255, 15/255, 192/255, 1]  # Pink color in RGBA

    MDFloatLayout:

        Image:
            id: seatBelt
            source: 'Images/seatBelt.png'
            size_hint: None, None
            size: 40, 40
            pos_hint: {'top':0.945, 'x':0.135}
        Image:
            id: door
            source: 'Images/door.png'
            size_hint: None, None
            size: 50, 40
            pos_hint: {'top':0.945, 'x':0.205}
        Image:
            id: highBeam
            source: 'Images/highBeam.png'
            size_hint: None, None
            size: 40, 40
            pos_hint: {'top':0.945, 'x':0.275}
        Image:
            id: lowBeam
            source: 'Images/lowBeam.png'
            size_hint: None, None
            size: 40, 40
            pos_hint: {'top':0.945, 'x':0.345}
        Image:
            id: battery
            source: 'Images/battery.png'
            size_hint: None, None
            size: 55, 55
            pos_hint: {'top':0.950, 'x':0.415}
        Image:
            id: temp
            source: 'Images/temp.png'
            size_hint: None, None
            size: 55, 55
            pos_hint: {'top':0.950, 'x':0.485}
        Image:
            id: volts
            source: 'Images/volts.png'
            size_hint: None, None
            size: 50, 50
            pos_hint: {'top':0.7, 'x':0.455}
        Label:
            id: voltsID
            text: '$$VOLTAGE$$ V'
            font_size: "15sp"
            pos_hint: {'top':1.175, 'x':0.03}
        Label:
            id: currentID
            text: '$$CURRENT$$ A'
            font_size: "15sp"
            pos_hint: {'top':1.145, 'x':0.03}
        Image:
            id: smoke
            source: 'Images/smoke.png'
            size_hint: None, None
            size: 50, 50
            pos_hint: {'top':0.945, 'x':0.555}
        Image:
            id: stWheel
            source: 'Images/stWheel.png'
            size_hint: None, None
            size: 40, 40
            pos_hint: {'top':0.945, 'x':0.625}
        Image:
            id: seat
            source: 'Images/seat.png'
            size_hint: None, None
            size: 90, 90
            pos_hint: {'top':0.976, 'x':0.675}
        Image:
            id: sun
            source: 'Images/sun.png'
            size_hint: None, None
            size: 50, 50
            pos_hint: {'top':0.945, 'x':0.765}
        Image:
            id: moon
            source: 'Images/moon.png'
            size_hint: None, None
            size: 45, 45
            pos_hint: {'top':0.945, 'x':0.835}



    MDFloatLayout:
        Image:
            source: 'Images/left.png'
            size_hint: None, None
            size: 65, 65
            pos_hint: {"center_x":0.39, "center_y": 0.67}
        Image:
            source: 'Images/right.png'
            size_hint: None, None
            size: 65, 65
            pos_hint: {"center_x":0.61, "center_y": 0.67}
        Label:
            id: batteryID
            text: 'BATTERY %'
            font_size: "35sp"
            size: self.texture_size
            pos_hint: {"center_x": .8,"center_y": .525}
        Image: 
            source: "Images/middle.png"
            pos_hint: {"center_x":0.5, "center_y": 0.45}
            size_hint: None,None
            size: 495,495
        Label:
            id: speedID
            text: '$$SPEED$$ KM/H'
            font_size: "35sp"
            size: self.texture_size
            pos_hint: {"center_x": .2, "center_y": .525}


    MDFloatLayout:

        Label:
            id: rangeID
            text: 'Range: $$RANGE$$ KM'
            font_size: "30sp"
            pos_hint: {"center_x": 0.5, "y": -0.35}
        Label:
            id: distanceTravelledID
            text: 'Distance Travelled: $$DISTANCETRAVELLED$$ KM'
            font_size: "30sp"
            pos_hint: {"center_x": 0.5, "y": -0.45}
'''

class runApp(MDApp):
    Window.size = (1280, 720)
    screen_manager = ScreenManager(transition=SlideTransition(duration=1.5))

    def __init__(self, **kwargs):
        super(runApp, self).__init__(**kwargs)
        self.running = True
        self.splash_screen = Builder.load_file("splashScreen.kv")
        self.run_app_screen = Builder.load_string(kv)

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
