from kivy.app import App
from kivy.uix.checkbox import CheckBox

class MeuApp(App):
    def build(self):
        return CheckBox(active = False)

if __name__ == "__main__":
    MeuApp().run()