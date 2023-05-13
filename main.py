from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

kv = """
<Content>:
    Screen:
        BoxLayout:
            Label:
                texf:'sure do you want to exit'
Screen:
    BoxLayout:
        orientation:'vertical'
        pos_hint:{"center_x":.5,"center_y":.5}
        TextInput
        TextInput
"""
Window.clearcolor = (50,0,10,0.30)
class Content(Screen):
    pass
class My(App):
    
    def build(self):
        Window.bind(on_keyboard=self.key)
        return Builder.load_string(kv)
    def key(self,window,key,*args):
        if key == 27:
            self.p = Popup(
                title='exit',
            ).open()
            
            return True
            
My().run()