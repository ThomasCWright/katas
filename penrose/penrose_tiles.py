

class Tile:
    '''
    class defining tiles
    '''

    def __init__(self,fill_colour=[0,0,0,1],line_colour=[255,255,255,1]):
        '''initialise Tile'''
        self.fill_colour=fill_colour
        self.line_colour=line_colour
        self.sides = 4 
        self.vertices = [(0,0),(0,1),(1,1),(1,0)]

    def add_side(self):
        '''add side'''
        self.sides += 1
        self.add_vertex()

    def add_vertex(self):
        '''add vertex'''
        new_vertex = ((self.vertices[0][0] + self.vertices[-1][0]) / 2, 
                      (self.vertices[0][1] + self.vertices[-1][1]) / 2)

        self.vertices.append(new_vertex)
        self.sides = len(self.vertices)

    def remove_side(self):
        '''remove side'''
        if self.sides > 3: 
            self.sides -= 1
            self.remove_vertex()

    def remove_vertex(self):
        '''remove vertex'''
        if self.sides > 3: 
            self.vertices.remove(self.vertices[-1])
            self.sides = len(self.vertices)

    def change_vertex_at_index_to_position(self, index, new_position):
        '''change vertes at index to new_position'''
        self.vertices[index] = new_position
