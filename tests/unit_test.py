import unittest
from Models.wall import Wall
from Models.element import Element
from Models.area import Area

class TestWall(unittest.TestCase):
    def test_get_coordinates(self):
        wall = Wall([[0,0],[6,2]])
        self.assertEqual(wall.get_coordinates(), [[0,0],[6,2]])

    def test_get_distance(self):
        wall=Wall([[5,6],[5,0]])
        
        self.assertEqual(wall.get_distance(), 6)

class TestElement(unittest.TestCase):
    def test_get_coordinates(self):
        elt=Element([[0,0],[6,2]])
        
        self.assertEqual(elt.get_coordinates(), [[0,0],[6,2]])

class TestArea(unittest.TestCase):
    def test_area_surface(self):
        walls = [Wall([[0,0],[0,6]]), Wall([[0,6],[5,6]]), Wall([[5,6],[5,0]]), Wall([[5,0],[0,0]])]
        area = Area(walls)
        self.assertEqual(area.get_surface(), 30)
    def test_is_rectangular(self):
        walls1 = [Wall([[0,0],[0,6]]), Wall([[0,6],[5,6]]), Wall([[5,6],[5,0]]), Wall([[5,0],[0,0]])]
        walls2 = [Wall([[0,2],[0,6]]), Wall([[0,6],[5,6]]), Wall([[5,6],[5,0]]), Wall([[5,0],[0,2]])]
        area_rect = Area(walls1)
        area_not_rect = Area(walls2)

        self.assertTrue(area_rect.is_rectangular())
        self.assertFalse(area_not_rect.is_rectangular())        


if __name__ == '__main__':
    unittest.main()