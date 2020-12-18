
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter
from kivy.core.window import Window
import kivy

from penrose_tiles import Tile


kivy.require('2.0.0') # replace with your current kivy version !

# from kivy.uix.label import Label
# from kivy.uix.scatterlayout import ScatterLayout

class DartScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(DartScreen, self).__init__(**kwargs)
        Window.bind(mouse_pos=self.mouse_pos)


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
        a = Scatter()
        a.add_widget(Tile())
        self.ids.scatter_layout.add_widget(a)
        b = Scatter()
        b.add_widget(Tile(sides=8))
        self.ids.scatter_layout.add_widget(b)
        pass

    def on_motion(self, etype, motionevent):
        # will receive all motion events.
        self.ids.lab_status.text = motionevent.pos
        pass

    def mouse_pos(self, window, pos):
        all_widgets=[]
        for k,v in self.ids.items():
            if hasattr(v,'collide_point'):
                if v.collide_point(*pos):
                    # self.ids.lab_status.text = f"{str(pos)}  {k}"
                    all_widgets.append(k)
        self.ids.lab_status.text = f"{str(pos)} {all_widgets}"
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
