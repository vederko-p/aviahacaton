from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.core.window import Window


from functools import partial

Builder.load_file("base.kv")

class AviaLabel(Label):
    def __init__(self, *args, **kwargs):
        super(AviaLabel, self).__init__(*args, **kwargs)
        self.color = 255, 255, 255, 1

class BaseScreen(Screen):
    """
    Базовая сцена с основными кнопками, которые не меняются в различных интерфейсах
    Записано в 'base.kv'
    """
    pass

class FlightScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super(FlightScreen, self).__init__(*args, **kwargs)
        """
        Важны следующие переменные, осуществляющие возможность показа расписания:
        rasp_list - список полётов. формат
        (номер, время отправления, гейт, куда)
        Важно правильно(удобно) обрабатывать куда.
        Надо указывать обозначение из 3-х букв аэропорта, наверное.
        """
        self.rasp_list = [('1','13:00', 'A', 'Санкт-Петербург')]
        self.button_list = list()

        # Заголовок
        self.head = AviaLabel(size_hint=(.3, .1),
                          font_size=25,
                          pos_hint={'center_x': 0.15, 'center_y': .95})
        self.head.text = 'Flight'
        self.add_widget(self.head)

        #Элемент, осуществляющий прокрутку
        self.scrlV = ScrollView(do_scroll_x=False,
                                do_scroll_y=True,
                                size_hint=(1, .8),
                                pos_hint={'center_x': .5, 'center_y': .40})
        self.add_widget(self.scrlV)

        #Заполнение ScrollView
        self.fillScrView()



    def fillScrView(self):
        self.scrlV.clear_widgets()
        #Процедура осуществляет заполнение ScrollView данными о рейсах
        # Сетка осуществляющая возможность добавления элементов в ScrollView
        tableLayout = GridLayout(cols=3, spacing=1, size_hint_y=None, row_default_height=50)
        tableLayout.bind(minimum_height=tableLayout.setter('height'))

        for i in range(len(self.rasp_list)):
            #Номер
            tableLayout.add_widget(AviaLabel(size_hint_x=None, width=50,
                                             text=self.rasp_list[i][0]))

            #Пустой виджет, чтобы всё было красиво
            tableLayout.add_widget(AviaLabel())

            # Время
            tableLayout.add_widget(AviaLabel(size_hint_x=None, width=100,
                                             text=self.rasp_list[i][1]))
            # Гейт
            tableLayout.add_widget(AviaLabel(size_hint_x=None, width=50,
                                             text=self.rasp_list[i][2]))

            # Куда
            tableLayout.add_widget(AviaLabel(#size_hint_x=None, width=100,
                                             text=self.rasp_list[i][3]))

            btn = Button(size_hint_x=None, width=100,
                         text='Маршрут')
            btn.number = i
            #btnfunc = partial(self.patient_update, btn.number)
            #btn.bind(on_press=btnfunc)
            self.button_list.append(btn)
            tableLayout.add_widget(btn)
        self.scrlV.add_widget(tableLayout)



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

class MainApp(App):

    def build(self):
        # Create the screen manager
        Window.clearcolor = (1, 1, 1, 1)
        sm = ScreenManager()
        sm.add_widget(FlightScreen(name='flight'))
        sm.add_widget(MapScreen(name='map'))
        sm.add_widget(AddScreen(name='add'))
        return sm

if __name__ == '__main__':
    MainApp().run()