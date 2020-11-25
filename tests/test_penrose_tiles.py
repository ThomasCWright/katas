import unittest

import penrose.main
import penrose.penrose_tiles
import pytest
import pytest_mock


class TestPenroseTiles:
    '''
    test suite for Penrose tiles
    '''

    def test_penrose_main_init(self):
        '''test kivy app starts and keeps running'''

        # with pytest_mock.mock.patch.object(penrose, "main", return_value=42):
        #     with pytest_mock.mock.patch.object(penrose, "__name__", "__main__"):

        with pytest_mock.mock.patch.object(penrose.main, "__name__", "__main__"):
            with pytest.raises(SystemExit):
                penrose.main.init()