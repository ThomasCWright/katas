import numpy
import math
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.graphics import Canvas, Color, Rectangle, Line

class Tile(Scatter):
    '''Enclosinf layout for Tiles'''
    
    instance_num = 0

    def __init__(self, **kwargs):
        super().__init__()
        self.do_scale = False
        self.do_translation = True
        self.do_rotation = True

        self.add_widget(TileShape(**kwargs))

class TileShape(Widget):
    '''
    class defining regular shaped primitive tiles
    '''


    def __init__(self,
                 fill_colour=(0,0,0,1),
                 line_colour=(1,1,1,1),
                 regular = True,
                 sides = 4,
                 length = 100.0):

        '''initialise Tile'''  
        super(TileShape, self).__init__()

        self.regular = True
        # self.origin=(0,0)
        self.fill_colour=fill_colour
        self.line_colour=line_colour
        self.sides = sides
        self.length = length
        Tile.instance_num += 1
        self.instance_num = Tile.instance_num
        self.vertices = []
        self.angles = []
        self.id=ObjectProperty(str(self.instance_num))
        self.update()
        # self.update_vertices()
        # self.update_canvas()
        


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
        default_vertices = [(0.0,0.0),(0.0,100.0),(100.0,100.0),(100.0,0.0)]

        if self.regular:
            theta = math.radians(180-360/self.sides)
            self.vertices.clear()
            self.vertices.append((0.0,0.0))
            v = (self.length,0) # x-axis
            for i in range(1,self.sides):
                next_vertex = (math.cos(theta)*v[0] - math.sin(theta)*v[1] + self.vertices[i-1][0] ,
                               math.sin(theta)*v[0] + math.cos(theta)*v[1] + self.vertices[i-1][1] ) 
                self.vertices.append(next_vertex)
                v = (self.vertices[i-1][0]-self.vertices[i][0],self.vertices[i-1][1]-self.vertices[i][1])
                
    def update_canvas(self):
        '''update canvas'''
        self.canvas.clear()
        with self.canvas.after:
            Color(self.line_colour[0],self.line_colour[1],self.line_colour[2],1)
            p = [sum(self.vertices,())]
            Line(points=p, close=True)       
            Color(self.fill_colour[0],self.fill_colour[1],self.fill_colour[2],1)
            Rectangle(pos=self.pos,size=self.size)
    
    def update(self):
        '''update tile'''
        self.update_vertices()
        self.update_angles()
        self.update_canvas()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print(f"self.descendants: {self.descendants()} ")


    def descendants(self,level=0):
        '''returns string of descendants'''
        list_of_children=""
        
        if self.children:
            for child in self.children:
                list_of_children += f"\n{'|'*(level != 0)}{'  '*level}{' '*(level > 1)}|--{child.descendants(level+1)}"
            return f"{self.instance_num}{list_of_children}"
        else:
            return f"{self.instance_num}"



