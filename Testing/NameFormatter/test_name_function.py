import unittest
from name_function import formatName


class TestNameFunction(unittest.TestCase):
    def test_fist_last(self):
        formated_name = formatName('aloys', 'aboge')
        self.assertEqual(formated_name, 'Aloys Aboge')


    def test_first_middle_last(self):
        formated_name = formatName('aloys', 'aboge', 'junior')
        self.assertEqual(formated_name, 'Aloys Junior Aboge')    

if __name__ == '__main__':
    unittest.main()        