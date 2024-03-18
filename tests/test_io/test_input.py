import unittest
import pandas as pd
from app.io import input

path_to_test_file = "test_data\\test.txt"
path_to_csv_file = "test_data\\addresses.csv"


class TestReadFromFile(unittest.TestCase):
    def test_file_existence(self):
        result = input.read_from_file(path_to_test_file)
        self.assertNotEqual(result, "File not found.")

    def test_file_content(self):
        expected_content = "test"
        result = input.read_from_file(path_to_test_file)
        self.assertEqual(result, expected_content)

    def test_nonexistent_file(self):
        result = input.read_from_file("nonexistent_file.txt")
        self.assertEqual(result, "File not found.")


class TestReadWithPandas(unittest.TestCase):

    def test_file_existence(self):
        result = input.read_with_pandas(path_to_csv_file)
        self.assertNotEqual(result.to_string(), "File not found.")

    def test_dataframe_type(self):
        result = input.read_with_pandas(path_to_csv_file)
        self.assertIsInstance(result, pd.DataFrame)

    def test_dataframe_columns(self):
        result = input.read_with_pandas(path_to_csv_file)
        expected_columns = ["First Name", "Last Name", "Address", "City", "State", "Zip"]
        self.assertEqual(result.columns.tolist(), expected_columns)


if __name__ == '__main__':
    unittest.main()
