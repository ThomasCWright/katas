
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import kivy

from penrose_tiles import Tile


kivy.require('2.0.0') # replace with your current kivy version !

# from kivy.uix.label import Label
# from kivy.uix.scatterlayout import ScatterLayout




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

    def add_tile(self):
        # self.ids.scatter_layout.add_widget(Tile())
        self.ids.scatter_layout.add_widget(Tile(sides=3))
        pass


class PenroseApp(App):

    def build(self):
        # return Label(text='Hello world')
        return DartScreen()

def init():
    if __name__ == '__main__':
        PenroseApp().run()
        return 42
    return 0

init()
