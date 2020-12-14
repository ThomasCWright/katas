import unittest

import penrose.main
from penrose.penrose_tiles import Tile
import pytest
from pytest_mock import mock


class TestPenroseTiles:
    '''
    test suite for Penrose tiles
    '''

    def test_penrose_main_init(self):
        '''test kivy app starts and keeps running'''

        with mock.patch.object(penrose, "main", return_value=42):
            with mock.patch.object(penrose, "__name__", "__main__"):
                assert penrose.main() == 42

        # with mock.patch.object(penrose.main, "__name__", "__main__"):
        #     # with pytest.raises(SystemExit):
        #     penrose.main.init()

    def test_tile_init_colour(self):
        test_tile = Tile()
        assert test_tile.fill_colour == [0,0,0,1]
        assert test_tile.line_colour == [255,255,255,1]

        test_tile = Tile(fill_colour=[255,0,255,1])
        assert test_tile.fill_colour == [255,0,255,1]
        assert test_tile.line_colour == [255,255,255,1]

        test_tile = Tile(line_colour=[255,0,255,1])
        assert test_tile.fill_colour == [0,0,0,1]
        assert test_tile.line_colour == [255,0,255,1]

        test_tile = Tile(line_colour=[255,0,255,1],fill_colour=[255,0,255,1])
        assert test_tile.fill_colour == [255,0,255,1]
        assert test_tile.line_colour == [255,0,255,1]

        test_tile = Tile([255,255,255,1],[255,0,255,1])
        assert test_tile.fill_colour == [255,255,255,1]
        assert test_tile.line_colour == [255,0,255,1]

        test_tile.fill_colour = [128,128,128,1]
        test_tile.line_colour = [0,255,0,1]

        assert test_tile.fill_colour == [128,128,128,1]
        assert test_tile.line_colour == [0,255,0,1]

    def test_tile_init_sides(self):
        '''test init for number of sides'''
        test_tile = Tile()
        assert test_tile.sides == 4

    def test_tile_sides_add(self):
        '''test side add for number of sides'''
        test_tile = Tile()
    
        test_tile.add_side()
        assert test_tile.sides == 5

    def test_tile_sides_remove(self):
        '''test side remove for number of sides'''

        test_tile = Tile()
    
        test_tile.remove_side()
        assert test_tile.sides == 3

        test_tile.remove_side()
        assert test_tile.sides == 3

    def test_tile_vertices_add(self):
        '''test tile vertices'''
        test_tile = Tile()
        assert len(test_tile.vertices) == test_tile.sides

        test_tile.add_vertex()
        assert len(test_tile.vertices) == test_tile.sides

    def test_tile_vertices_remove(self):
        '''test tile vertices'''
        test_tile = Tile()
        assert len(test_tile.vertices) == test_tile.sides

        test_tile.remove_vertex()
        assert len(test_tile.vertices) == test_tile.sides

    def test_tile_change_vertex_at_index_to_position(self):
        '''test to change vertex'''
        test_tile = Tile()
        new_position=(0.1,0.1)
        index=0
        test_tile.change_vertex_at_index_to_position(index=index,new_position=new_position)
        assert test_tile.vertices[index] == new_position

        new_position=(0.9,0.1)
        index=1
        test_tile.change_vertex_at_index_to_position(index=index,new_position=new_position)
        assert test_tile.vertices[index] == new_position

    def test_tile_internal_angle_at_vertex(self):
        '''test internal angle at vertex'''
        test_tile = Tile()
        assert test_tile.angles == [90.0,90.0,90.0,90.0]

        test_tile.add_vertex()
        assert test_tile.angles == [108.0,108.0,108.0,108.0,108.0]

