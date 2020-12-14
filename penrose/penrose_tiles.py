import numpy
import math

class Tile:
    '''
    class defining regular shaped primitive tiles
    '''

    def __init__(self,fill_colour=[0,0,0,1],line_colour=[255,255,255,1]):
        '''initialise Tile'''
        self.regular = True
        self.origin=(0,0)
        self.fill_colour=fill_colour
        self.line_colour=line_colour
        self.sides = 4
        self.length = 1.0 
        self.update()

    def add_side(self):
        '''add side'''
        self.sides += 1
        self.update()

    def add_vertex(self):
        '''add vertex'''
        self.sides += 1
        self.update()

    def remove_side(self):
        '''remove side'''
        if self.sides > 3: 
            self.sides -= 1
            self.update()

    def remove_vertex(self):
        '''remove vertex'''
        if self.sides > 3: 
            self.sides -= 1
            self.update()

    def change_vertex_at_index_to_position(self, index, new_position):
        '''change vertes at index to new_position'''
        self.vertices[index] = new_position
        self.regular = False
        self.update()

    def update_angles(self):
        '''update internal angles of a shape'''
        if self.regular:
            self.angles = []

        for i, this_vertex in enumerate(self.vertices):
            if self.regular:
                self.angles.append(180-360/self.sides)
            else:
                next_vertex = self.vertices[(i+1)%len(self.vertices)]
                previous_vertex = self.vertices[i-1]

                v1 = (next_vertex[0]-this_vertex[0],next_vertex[1]-this_vertex[1])
                v2 = (previous_vertex[0]-this_vertex[0],previous_vertex[1]-this_vertex[1])

                self.angles.append(math.degrees(math.acos(numpy.dot(v1,v2)/numpy.linalg.norm(v1)/numpy.linalg.norm(v2))))

    def update_vertices(self):
        '''update coordinates of shape vertices'''
        if self.regular:
            self.vertices=[self.origin]
        
        if self.regular:
            for i in range(1,self.sides):
                theta=math.radians(i*(180-360/self.sides))
                self.vertices.append((self.vertices[i-1][0]+math.cos(theta),self.vertices[i-1][1]+math.sin(theta)))
                
    def update(self):
        '''update tile'''
        self.update_vertices()
        self.update_angles()




