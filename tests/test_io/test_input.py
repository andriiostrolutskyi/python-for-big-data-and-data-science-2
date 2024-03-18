import unittest
import pandas as pd
from app.io import input


class TestReadFromFile(unittest.TestCase):

    def test_file_existence(self):
        result = input.read_from_file("C:\\Users\\user\\PycharmProjects\\Ostrolutskyi_python\\data\\test.txt")
        self.assertNotEqual(result, "File not found.")

    def test_file_content(self):
        expected_content = "test"
        result = input.read_from_file("C:\\Users\\user\\PycharmProjects\\Ostrolutskyi_python\\data\\test.txt")
        self.assertEqual(result, expected_content)

    def test_nonexistent_file(self):
        result = input.read_from_file("nonexistent_file.txt")
        self.assertEqual(result, "File not found.")


class TestReadWithPandas(unittest.TestCase):

    def test_file_existence(self):
        result = input.read_with_pandas("C:\\Users\\user\\PycharmProjects\\Ostrolutskyi_python\\data\\addresses.csv")
        self.assertNotEqual(result.to_string(), "File not found.")

    def test_dataframe_type(self):
        result = input.read_with_pandas("C:\\Users\\user\\PycharmProjects\\Ostrolutskyi_python\\data\\addresses.csv")
        self.assertIsInstance(result, pd.DataFrame)

    def test_dataframe_columns(self):
        result = input.read_with_pandas("C:\\Users\\user\\PycharmProjects\\Ostrolutskyi_python\\data\\addresses.csv")
        expected_columns = ["First Name", "Last Name", "Address", "City", "State", "Zip"]
        self.assertEqual(result.columns.tolist(), expected_columns)


if __name__ == '__main__':
    unittest.main()
