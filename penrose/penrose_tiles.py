

class Tile:
    '''
    class defining tiles
    '''

    fill_colour = [0,0,0,1]         # RGBA
    line_colour = [255,255,255,0]   # RGBA  

    def __init__(self,fill_colour=[0,0,0,1],line_colour=[255,255,255,1]):
        self.fill_colour=fill_colour
        self.line_colour=line_colour

