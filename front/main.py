from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.dropdown import DropDown
from kivy.uix.actionbar import ActionDropDown
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.treeview import TreeView

from functions import *

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
        self.rasp_list = [('1','13:00', 'A', 'Санкт-Петербург'),('2','14:00', 'B', 'Санкт-Петербург')]
        self.button_list = list()

        # Заголовок
        self.head = AviaLabel(size_hint=(.3, .1),
                          font_size=25,
                          pos_hint={'center_x': 0.15, 'center_y': .95})
        self.head.text = 'Flight'
        self.add_widget(self.head)

        # Окно поиска
        # self.search = TextInput(multiline=False,
                                # size_hint=(1, 0.1),
                                # font_size=40,
                                # pos_hint={'center_x': .5, 'center_y': .85},
                                # on_text_validate=print)
        # self.add_widget(self.search)

        #Элемент, осуществляющий прокрутку
        self.scrlV = ScrollView(do_scroll_x=False,
                                do_scroll_y=True,
                                size_hint=(1, .7),
                                pos_hint={'center_x': .5, 'center_y': .45})
        self.add_widget(self.scrlV)

        # Рисуем отделяющую линию

        #Заполнение ScrollView
        self.fillScrView()


    def fillScrView(self):
        self.scrlV.clear_widgets()
        #Процедура осуществляет заполнение ScrollView данными о рейсах
        # Сетка осуществляющая возможность добавления элементов в ScrollView
        tableLayout = GridLayout(cols=3, spacing=1, size_hint_y=None, row_default_height=50)
        tableLayout.bind(minimum_height=tableLayout.setter('height'))
        writeHorLine(tableLayout, 0)

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
            writeHorLine(tableLayout, (i+1)*100)
        self.scrlV.add_widget(tableLayout)

class MapScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super(MapScreen, self).__init__(*args, **kwargs)

        # Заголовок
        self.head = AviaLabel(size_hint=(.3, .1),
                              font_size=25,
                              pos_hint={'center_x': 0.15, 'center_y': .95})
        self.head.text = 'Карта'
        self.add_widget(self.head)

        # Окно поиска
        self.dropdown = DropDown()

        self.search = TextInput(multiline=False,
                                size_hint=(1, 0.1),
                                font_size=40,
                                pos_hint={'center_x': .5, 'center_y': .85},
                                #on_text_validate=self.dropdown.open
                                )
        self.search.bind(text = self.update_dropdown)
        #Действие в момент выбора
        #self.dropdown.bind(on_select=lambda instance, x: setattr(self.search, 'text', x))
        self.add_widget(self.search)

        # Карта
        self.airport = Image(source='airport.png',
                        size_hint=(1*4, 0.7*4),
                        pos_hint={'center_x': .5, 'center_y': .45})
        self.add_widget(self.airport, 5)

        #Кнопка приближения
        self.plus_button = Button(text="+", size_hint=(None,None), size=(80,80),
                                  pos=(Window.size[0] - 90,Window.size[1]*0.2+90))
        self.plus_button.bind(on_release=self.big_map)
        self.add_widget(self.plus_button)
        #Кнопка отдаления
        self.minus_button = Button(text="-", size_hint=(None,None), size=(80,80),
                                   pos=(Window.size[0] - 90,Window.size[1]*0.2))
        self.minus_button.bind(on_release=self.small_map)
        self.add_widget(self.minus_button)

    def change(self, event):
        global mapp
        mapp.sm.current = 'flight'

    def update_dropdown(self, struct, mes):
        self.dropdown.dismiss()
        self.dropdown=DropDown()
        self.dropdown.max_height = Window.size[1]*0.7

        #Здесь будет возвращаться список
        #Кнопки будут создавать маршрут уже до цели
        for index in range(40):
            btn = Button(text=f'{mes} %d' % index, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)

        self.dropdown.open(struct)

    def big_map(self, event):
        new_size = (self.airport.size_hint[0]*1.1, self.airport.size_hint[1]*1.1)
        self.airport.size_hint = new_size
        print(self.airport.size_hint)
    def small_map(self, event):
        new_size = (self.airport.size_hint[0] * 0.9, self.airport.size_hint[1] * 0.9)
        self.airport.size_hint = new_size
        print(self.airport.size_hint)

class AddScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super(AddScreen, self).__init__(*args, **kwargs)

        # Заголовок
        self.head = AviaLabel(size_hint=(.3, .1),
                              font_size=25,
                              pos_hint={'center_x': 0.15, 'center_y': .95})
        self.head.text = 'Add'
        self.add_widget(self.head)

        #Окно поиска
        #self.search = TextInput(multiline=False,
                                #size_hint=(1, 0.1),
                                #font_size=40,
                                #pos_hint={'center_x': .5, 'center_y': .85},
                                #on_text_validate=print)
        #self.add_widget(self.search)
        #Набор имён2
        #Необходима утилита поиска по строке
        #Находятся все имена, содержащие строку
        #name_list=["Аптека", "Магазин", "Туалет"]


        #Основной слой с сеткой
        tableLayout = GridLayout(cols=3, spacing=10,

                                 size_hint=(1, .7), pos_hint={'center_x': 0.5, 'center_y': .45})

        #Возвращаем ширину экрана
        width = Window.size[0]
        #Кнопки с типами
        tableLayout.add_widget(Button(size_hint=(None, None), size=(width*0.3, width*0.3), text="Т"))
        tableLayout.add_widget(Button(size_hint=(None, None), size=(width*0.3, width*0.3), text="А"))
        tableLayout.add_widget(Button(size_hint=(None, None), size=(width*0.3, width*0.3), text="М"))
        tableLayout.add_widget(Button(size_hint=(None, None), size=(width*0.3, width*0.3), text="Е"))
        self.add_widget(tableLayout)

class MainApp(App):

    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        Window.size = (720 / 2.2, 1520 / 2.2)
        #Window.fullscreen = True

        # Create the screen manager
        self.sm = ScreenManager()
        self.sm.add_widget(MapScreen(name='map'))
        self.sm.add_widget(FlightScreen(name='flight'))

        self.sm.add_widget(AddScreen(name='add'))

        return self.sm

    def switch_screen_to(self):
        self.sm.current='flight'


if __name__ == '__main__':
    global mapp
    mapp = MainApp()
    mapp.run()