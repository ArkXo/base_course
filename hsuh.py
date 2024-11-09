import math
import numpy as np
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window

def tupper_formula(x, y):
    return ((y//17)//(2 ** (17*x+(y % 17)))) % 2

class TupperView(Widget):
    def __init__ (self, **kwargs):
        super (TupperView, self)._init_(**kwargs)

    def draw(self, k):
        with self.canvas:
            self.canvas.clear()

            m = Window.size[0] // 106

            tupper = np.array([tupper_formula(x,y) for x in range(106) for y in range(k, k+17)])

            for x in range(106):
                for y in range(0, 17):
                    print(x, "-", y)
                    print(tupper_formula(x, y + k))
                    if tupper_formula(x, y+k):
                        Rectangle(pos=(x*m,y*m + Window.size[1]//2), size=(m, m))

class TupperApp(App):
    def build(self):
        self.root = BoxLayout(orientation="vertical")
        self.menu = BoxLayout(orientation="horizontal")

        self.menu.add_widget(TextInput(text_hint="Впишите сюда k"))
        self.menu.add_widget(Button(text="Нарисовать!", on_press=self.draw))

        self.tupper_view = TupperView()

        self.root.add_widget(self.tupper_view)
        self.root.add_widget(self.menu)

        return self.root

def draw(self, instance):
    k = int(self.menu.children[0].text)
    self.tupper_view.draw(k)

if __name__ == "__main__":
    TupperApp().run()
