import os
import unittest


def analyze_text(filename):
    """
    Count lines and characters in a file
    :param filename: filename
    :return: number of lines and characters in a file
    """
    lines = 0
    chars = 0
    with open(filename, mode='rt', encoding='utf-8') as file:
        for line in file:
            lines += 1
            chars += len(line)
    return lines, chars


class TextAnalysisTests(unittest.TestCase):
    """A unit test class extends unittest.TestCase"""

    def setUp(self):
        """Both setUp and teadDown overwrites the dummy ones defined in unittest.TestCase"""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Now we are engaged in a great civil war.\n'
                    'testing whether that nation,\n'
                    'or any nation so conceived and so dedicated,\n'
                    'can long endure.')

    def tearDown(self):
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function(self):
        analyze_text(self.filename)

    def test_line_count(self):
        """assertion methods are available in unittest.TestCase"""
        self.assertEqual(4, analyze_text(self.filename)[0])

    def test_char_count(self):
        self.assertEqual(131, analyze_text(self.filename)[1])

    def test_no_such_file(self):
        """assert an error should be thrown"""
        with self.assertRaises(IOError):
            analyze_text("none")

    def test_no_deletion(self):
        """assertTrue and assertFalse"""
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))


if __name__ == '__main__':
    # unittest.main() will look for all classes that extends unittest.TestCase and run them
    unittest.main()
