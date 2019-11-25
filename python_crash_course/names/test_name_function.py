import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    '''Test for name_function.py'''

    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('j', 'hoover', 'edgar')
        self.assertEqual(formatted_name, 'J Edgar Hoover')


unittest.main()
