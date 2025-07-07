import unittest
import main
import tempfile
import os
from unittest import mock

class TestMainFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(main.add(2, 3), 5)
        self.assertEqual(main.add(-1, -1), -2)
        self.assertEqual(main.add(2.5, 3.1), 5.6)
        self.assertNotEqual(main.add(2, 2), 5)

    def test_is_even(self):
        self.assertTrue(main.is_even(4))
        self.assertFalse(main.is_even(3))
        self.assertTrue(main.is_even(0))
        with self.assertRaises(TypeError):
            main.is_even(2.2)
        with self.assertRaises(TypeError):
            main.is_even("2")

    def test_get_largest(self):
        self.assertEqual(main.get_largest([1, 2, 3]), 3)
        self.assertEqual(main.get_largest([-5, -1, -10]), -1)
        self.assertEqual(main.get_largest([7]), 7)
        with self.assertRaises(ValueError):
            main.get_largest([])

    def test_reverse_string(self):
        self.assertEqual(main.reverse_string("hello"), "olleh")
        self.assertEqual(main.reverse_string(""), "")
        self.assertEqual(main.reverse_string("a"), "a")
        with self.assertRaises(TypeError):
            main.reverse_string(123)

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, mode="w+")
        self.temp_file.write("Test line\nSecond line")
        self.temp_file.close()

    def tearDown(self):
        os.remove(self.temp_file.name)

    def test_read_file_content(self):
        def read_file(path):
            with open(path, "r") as f:
                return f.read()
        content = read_file(self.temp_file.name)
        self.assertIn("Test line", content)

    def test_mocked_add(self):
        with mock.patch('main.add', return_value=100):
            self.assertEqual(main.add(5, 6), 100)

    def test_add_multiple_cases(self):
        test_cases = [
            (1, 2, 3),
            (-1, -2, -3),
            (0, 0, 0),
            (2.5, 2.5, 5.0),
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(main.add(a, b), expected)

if __name__ == '__main__':
    unittest.main()
