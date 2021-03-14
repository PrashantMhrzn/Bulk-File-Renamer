import unittest
import os
from utils import Renamer


class TestUtils(unittest.TestCase):

    def test_rename(self):
        r = Renamer()
        before_files = os.listdir('./test_folder')
        r.rename('./test_folder', 'test')
        after_files = os.listdir('./test_folder')
        self.assertIsInstance(r, Renamer)
        self.assertEqual(after_files[0], 'test1.txt')
        self.assertEqual(after_files[1], 'test2.txt')
        self.assertNotEqual(before_files, after_files)


if __name__ == '__main__':
    unittest.main()
