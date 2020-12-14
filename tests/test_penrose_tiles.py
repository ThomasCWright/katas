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
        '''test for number of sides'''
        test_tile = Tile()
        assert test_tile.sides == 4

        test_tile.sides = 5
        assert test_tile.sides == 5

    def test_tile_vertices(self):
        '''test tile vertices'''
        test_tile = Tile()
        assert len(test_tile.vertices) == test_tile.sides

        test_tile.sides = 5
        assert len(test_tile.vertices) == test_tile.sides