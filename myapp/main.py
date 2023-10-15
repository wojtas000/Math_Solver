# main.py
import kivy
from kivy import Config
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.camera import Camera
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar

from utils import get_text, ask_openai

kivy.require('1.11.1')
Config.set('graphics', 'multisamples', '0')
Builder.load_string('''

<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Welcome to the Math Teacher App'
            size_hint_y: None
            height: '48dp'
        Button:
            text: 'Take a photo'
            on_press: root.manager.current = 'camera_screen'
            size_hint_y: None
            height: '48dp'
        Button:
            text: 'Open a file'
            on_press: root.manager.current = 'file_chooser_screen'
            size_hint_y: None
            height: '48dp'
                    
<FileChooserScreen>:
    BoxLayout:
        orientation: 'vertical'
        FileChooserListView:
            id: filechooser
            path: '.'
            on_selection: root.selected(filechooser.selection)
        Button:
            text: 'Back to Main'
            on_press: root.manager.current = 'main_screen'
            size_hint_y: None
            height: '48dp'
        Button:
            text: 'Solve'
            on_press: root.manager.current = 'response_screen'
            size_hint_y: None
            height: '48dp'
                    

<CameraScreen>:
    Camera:
        id: camera
        resolution: (1280, 960)
        play: False

    BoxLayout:
        orientation: 'vertical'
        ToggleButton:
            text: 'Play'
            on_press: camera.play = not camera.play
            size_hint_y: None
            height: '48dp'

        Button:
            text: 'Capture'
            on_press: root.capture()
            size_hint_y: None
            height: '48dp'

        Button:
            text: "Solve"
            on_press: root.manager.current = 'response_screen'
            size_hint_y: None
            height: '48dp'

<ResponseScreen>:
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            id: response_label
            color: 0, 0, 0, 1
            text: ""
            size_hint: None, None
            size: 300, 100
            pos_hint: {'center_x': .5, 'top': 1}
        
        Button:
            text: 'Back to Main Screen'
            on_press: 
                root.manager.current = 'main_screen'
            size_hint_y: None
            height: '48dp'
''')

SELECTED_FILE = None

class MyKivyApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoadingScreen(name='loading_screen'))
        sm.add_widget(CameraScreen(name='camera_screen'))
        sm.add_widget(ResponseScreen(name='response_screen'))
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(FileChooserScreen(name='file_chooser_screen'))
        sm.current = 'main_screen'
        
        return sm
    

class LoadingScreen(Screen):
    pass

class CameraScreen(Screen):
    
    def capture(self):
        camera = self.ids['camera']
        camera.export_to_png('captured_image.png')
        global SELECTED_FILE
        SELECTED_FILE = 'captured_image.png'
        not camera.play


class ResponseScreen(Screen):
    # get the text from the camera screen

    def on_enter(self):
        self.analyze_text()

    def analyze_text(self):
        global SELECTED_FILE
        if SELECTED_FILE:
            ocr_text = get_text(SELECTED_FILE)
            chat_gpt_answer = ask_openai(f"Jesteś nauczycielem matematyki. Rozwiąż powyższe zadanie, rozpisując w punktach twój tok rozumowania: \n {ocr_text}")
            self.ids.response_label.text = f" Rozwiązanie: \n {chat_gpt_answer}"
        else:
            self.ids.response_label.text = "Nie wybrano pliku"

class MainScreen(Screen):
    pass

class FileChooserScreen(Screen):
    def selected(self, filename):
        global SELECTED_FILE
        SELECTED_FILE = filename[0]

if __name__ == '__main__':
    MyKivyApp().run()
