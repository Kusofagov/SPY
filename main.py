from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        button = Button(text='Hi')

        return button

if __name__ == "__main__":
    app = TestApp()
    app.run()