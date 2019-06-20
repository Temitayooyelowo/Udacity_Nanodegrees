import unittest

from os import getcwd

from problem_2 import FileFinder
class Problem2(unittest.TestCase):

    def test_invalid_directory(self):
        file_finder = FileFinder()
        result = file_finder.find_files(".c", f"{getcwd()}/invalid_dir")
        self.assertEqual(len(result), 0)
    
    def test_valid_directory(self):
        file_finder = FileFinder()
        result = file_finder.find_files(".c", f"{getcwd()}/testdir")
        expected_result = ['b.c', 't1.c', 'a.c', 'a.c']

        self.assertEqual(len(result), len(expected_result))
        for expected_value in expected_result:
            self.assertTrue(expected_value in result)

if __name__ == '__main__':
    unittest.main()