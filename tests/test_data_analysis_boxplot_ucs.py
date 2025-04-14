import unittest
import pandas as pd
import sys
import os

dir_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_root)

from data_analysis_boxplot_ucs import (
    is_dataframe, exist_column_in_dataframe,
    column_type_is_float, ensure_directory_exists)

class TestIsDataframe(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame({'Column1': [1, 2, 3]})

    def test_is_dataframe(self):
        self.assertTrue(is_dataframe(self.data))
    
    def test_is_not_dataframe(self):
        data = [1, 2, 3]
        self.assertFalse(is_dataframe(data))

    def test_none(self):
        data = None
        self.assertFalse(is_dataframe(data))

    def test_string(self):
        data = "This is not a dataframe"
        self.assertFalse(is_dataframe(data))


class TestExistColumnInDataframe(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame({'Column1': [1, 2, 3]})

    def test_exist_column_in_dataframe(self):
        self.assertTrue(exist_column_in_dataframe(self.data, 'Column1'))
    
    def test_column_not_exist(self):
        self.assertFalse(exist_column_in_dataframe(self.data, 'Column2'))


class TestColumnTypeIsFloat(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame({'Column1': [1.0, 2.0, 3.0]})

    def test_column_type_is_float(self):
        self.assertTrue(column_type_is_float(self.data, 'Column1'))

class TestEnsureDirectoryExists(unittest.TestCase):

    def test_ensure_directory_exists(self):
        directory = 'boxplot_images'
        ensure_directory_exists(directory)
        self.assertTrue(os.path.exists(directory)) 


if __name__ == '__main__':
    unittest.main(verbosity=2)