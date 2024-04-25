from kivy.app import App
from kivy.uix.button import Button

def botao_pressionado(instence):
    print("Botão pressionado")

class MinhaApp(App):
    def build(self):
        btn = Button(text= 'Clique Aqui')
        btn.bind(on_press=botao_pressionado)
        return btn
    
if __name__ == "__main__":
    MinhaApp().run()