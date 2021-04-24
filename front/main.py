from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition

Builder.load_file("base.kv")

class BaseScreen(Screen):
    """
    Базовая сцена с основными кнопками, которые не меняются в различных интерфейсах
    Записано в 'base.kv'
    """
    pass

class FlightScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super(FlightScreen, self).__init__(*args, **kwargs)

        # Заголовок
        self.txt1 = Label(size_hint=(.5, None),
                          height=40,
                          font_size=25,
                          pos_hint={'center_x': .35, 'center_y': .90})
        self.txt1.text = 'Flight'
        self.add_widget(self.txt1)

class MapScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super(MapScreen, self).__init__(*args, **kwargs)

        # Заголовок
        self.txt1 = Label(size_hint=(.5, None),
                          height=40,
                          font_size=25,
                          pos_hint={'center_x': .35, 'center_y': .90})
        self.txt1.text = 'Map'
        self.add_widget(self.txt1)

class AddScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super(AddScreen, self).__init__(*args, **kwargs)

        # Заголовок
        self.txt1 = Label(size_hint=(.5, None),
                          height=40,
                          font_size=25,
                          pos_hint={'center_x': .35, 'center_y': .90})
        self.txt1.text = 'Add'
        self.add_widget(self.txt1)

class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(FlightScreen(name='flight'))
        sm.add_widget(MapScreen(name='map'))
        sm.add_widget(AddScreen(name='add'))
        return sm

if __name__ == '__main__':
    TestApp().run()