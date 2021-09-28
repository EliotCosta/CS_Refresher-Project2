import unittest
from Models.element import Element

class TestElement(unittest.TestCase):
    def test_get_coordinates(self):
        elt=Element([(0,0),(6,2)])
        
        self.assertEqual(elt.get_coordinates(), [(0,0),(6,2)])

if __name__ == '__main__':
    unittest.main()