from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button

class greetings_screen(Screen):
    def __init__(self, **kw):
        super(greetings_screen, self).__init__(**kw)
        bt = Button()
        self.add_widget(bt)

class menu_screen(Screen):
    def __init__(self, **kw):
        super(menu_screen, self).__init__(**kw)
        bl = BoxLayout()
        pic_game = Image(source = '/path/C:/Users/svyab/PycharmProjects/pythonProject/Kivy_logo.png', size_hint=(1, .5),
                    pos_hint={'center_x':.5, 'center_y':.5})
        name_game = Label(text='The Agents')
        bl.add_widget(pic_game)
        bl.add_widget(name_game)
        self.add_widget(bl)

def set_screen(name_screen):
    sm.current = name_screen

sm = ScreenManager()
#sm.add_widget(greetings_screen(name='greetings'))
sm.add_widget(menu_screen(name='menu'))
# sm.add_widget(AddFood(name='add_food'))

class TestApp(App):
    def build(self):
      return sm

if __name__ == "__main__":
    app = TestApp()
    app.run()