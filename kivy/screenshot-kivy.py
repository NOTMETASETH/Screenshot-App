import time
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserIconView
from kivy.core.window import Window
from PIL import ImageGrab
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
import os

Window.clearcolor = (1, 1, 1, 1)

class ScreenshotBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setup_widgets()

    def setup_widgets(self):
        self.orientation = "vertical"
        self.padding = 10
        self.spacing = 10

        self.save_label = Label(text='Save location:', color=(0, 0, 0, 1))
        self.add_widget(self.save_label)

        self.save_entry = TextInput(multiline=False, text='/Users/m1/Developer/Projects/Screenshot-App/kivy/screen_files_2')
        self.add_widget(self.save_entry)

        self.browse_button = Button(text='Browse', on_release=self.open_filechooser)
        self.add_widget(self.browse_button)

        self.name_label = Label(text='File name:', color=(0, 0, 0, 1))
        self.add_widget(self.name_label)

        self.name_entry = TextInput(multiline=False, text='screenshot')
        self.add_widget(self.name_entry)

        self.delay_label = Label(text='Delay (s):', color=(0, 0, 0, 1))
        self.add_widget(self.delay_label)

        self.delay_entry = TextInput(multiline=False, text='0')
        self.add_widget(self.delay_entry)

        self.screenshot_button = Button(text='Take screenshot', background_color=(0, 0, 0, 1), color=(1, 1, 1, 1))
        self.screenshot_button.bind(on_release=self.screenshot)
        self.add_widget(self.screenshot_button)

        self.filechooser = FileChooserIconView(dirselect=True)
        self.dialog = MDDialog(title='Choose directory', type='custom', content_cls=self.filechooser, buttons=[Button(text='Select', on_release=self.select_directory)])

    def open_filechooser(self, *args):
        self.dialog.open()

    def select_directory(self, *args):
        selected_directory = self.filechooser.path
        self.save_entry.text = selected_directory
        self.dialog.dismiss()

    def screenshot(self, *args):
        try:
            delay = int(self.delay_entry.text)
            time.sleep(delay)
            name = self.name_entry.text
            save_location = self.save_entry.text
            if not os.path.exists(save_location):
                os.makedirs(save_location)
            path = f'{save_location}/{name}.png'
            img = ImageGrab.grab()
            img.save(path)
            img.show()
        except ValueError:
            print("Invalid delay input, please enter an integer.")
        except Exception as e:
            print("An error occurred while taking a screenshot:", str(e))

class ScreenshotMDApp(MDApp):
    def build(self):
        return ScreenshotBoxLayout()

if __name__ == "__main__":
    ScreenshotMDApp().run()
