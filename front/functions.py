from kivy.core.window import Window
from kivy.graphics import *

def writeHorLine(object, y):
    """
    Рисует горизонтальную линию в объекте
    :param object:
    :return:
    """
    with object.canvas:
        # Add a red color
        Color(0, 0, 0)

        # Add a rectangle
        Rectangle(pos=(0, y), size=(Window.size[0], 1))