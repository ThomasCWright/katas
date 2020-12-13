import kivy

kivy.require('2.0.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout



class DartScreen(BoxLayout):

    def build(self):
        pass


    def change_source(self):
        if self.ids.tile_image.source == 'penrose_dart.png':
            self.ids.tile_image.source = 'penrose_kite.png'
        else:
            self.ids.tile_image.source = 'penrose_dart.png'
        print(self.ids.tile_image.source)
        self.ids.tile_image.reload()
        pass


class PenroseApp(App):

    def build(self):
        # return Label(text='Hello world')
        return DartScreen()

def init():
    if __name__ == '__main__':
        PenroseApp().run()
        return 42

init()