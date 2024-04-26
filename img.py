from kivy.app import App
from kivy.uix.image import Image

class MeuApp(App):
    def build(self):
        return Image(source= "C:\SystemUserK\perfil-coelho.jpg")

if __name__ == "__main__":
    MeuApp().run()