from kivy.app import App 
from kivy.uix.image import Image, AsyncImage

class MinhaApp(App):
    def build(self):
        return AsyncImage(source='https://cdn.meutimao.com.br/_upload/noticia/2024/04/28/wesley-driblou-felipe-melo-antes-de-anotar-um-9d.jpg')
 
 
if __name__=="__main__":
    MinhaApp().run()              