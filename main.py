
from kivy.app import App
# kivy.require("1.8.0")
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.core.image import Image
from kivy.uix.button import Button
from kivy.clock import Clock

import os
import time

from kivy.config import Config
#Config.set('graphics', 'width', '700')
#Config.set('graphics', 'height', '700')
#Config.write()

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from os.path import join

# changing color to white
from kivy.core.window import Window
from kivy.graphics import Color
Window.clearcolor = (1, 1, 1, 1)
# mode rgba
# time_start = time.time() # in class
# timing_ms = time.time() - self.time_start # in method

class MainScreen(Screen):  
        
    username = ObjectProperty(None)
    test_type = ObjectProperty(None)
    test_date = ObjectProperty(None)

    def reset(self):
        self.username.text = ""
        self.test_type.text = ""
        self.test_date.text = ""
        
class SecondScreen(Screen):
    pass     
class AnotherScreen(Screen):
    pass
class ScreenManagement(ScreenManager):
    pass
                                
class DrawInput(Widget):
        
    filename = StringProperty("")
    test_type = StringProperty("")
    now = time.localtime(time.time())
    t = str(now[0]) + "/"+ str(now[1]) + "/" + str(now[2]) + "_"+ str(now[3]) + ":" + str(now[4]) + ":" + str(now[5])

    def btn_save(self):
        Window.screenshot(self.filename+self.test_type+".png")
        
    def on_touch_down(self, touch):
        
        timing_ms = ApplePenApp.get_running_app().sw_seconds
    
                  
        with self.canvas:
            Color(0, 0, 0)
            touch.ud["line"] = Line(points = (touch.x, touch.y))

        if 'pressure' in touch.profile:
            ud['pressure'] = touch.pressure
            #print(touch.pressure)

        
        
    def on_touch_move(self, touch):

        timing_ms = ApplePenApp.get_running_app().sw_seconds


        touch.ud["line"].points += (touch.x, touch.y)

    def on_touch_up(self, touch):     

        timing_ms = ApplePenApp.get_running_app().sw_seconds

presentation = Builder.load_file("applepen_kivy.kv")

class ApplePenApp(App):

    sw_started = False
    sw_seconds = 0
    
    def update_clock(self, nap):
        if self.sw_started:
            self.sw_seconds += nap
        #print(self.sw_seconds)
            
    def start_stop(self):
        self.sw_started = True

    def reset(self):
        if self.sw_seconds:
            self.sw_seconds = 0
        else:
            pass

    def stop_clock(self):
        self.sw_started = False

    def on_start(self):
        Clock.schedule_interval(self.update_clock, 0)

    def build(self):
        return presentation
       
if __name__=="__main__":
    ApplePenApp().run()


