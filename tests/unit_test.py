import unittest
from Models.building import Building
from Models.wall import Wall
from Models.element import Element
from Models.area import Area

A11 = Area([Wall([[0,0],[0,6]]), Wall([[0,6],[5,6]]), Wall([[5,6],[5,0]]), Wall([[5,0],[0,0]])])
A12 = Area([Wall([[0,0],[0,3]]), Wall([[0,3],[-3,3]]), Wall([[-3,3],[-3,0]]), Wall([[-3,0],[0,0]])])
A13 = Area([Wall([[-6,0],[-6,4]]), Wall([[-6,4],[6,6]]), Wall([[6,6],[6,0]]), Wall([[6,0],[-6,0]])])

A21 = Area([Wall([[-6,1],[-6,4]]), Wall([[-6,4],[-2,4]]), Wall([[-2,4],[-2,1]]), Wall([[-2,1],[-6,1]])])
A22 = Area([Wall([[-2,1],[-2,4]]), Wall([[-2,4],[2,4]]), Wall([[2,4],[2,1]]), Wall([[2,1],[-2,1]])])
A23 = Area([Wall([[2,1],[2,4]]), Wall([[2,4],[6,4]]), Wall([[6,4],[6,1]]), Wall([[6,1],[2,1]])])
A24 = Area([Wall([[6,1],[6,4]]), Wall([[6,4],[8,4]]), Wall([[8,4],[8,1]]), Wall([[8,1],[6,1]])])
A25 = Area([Wall([[-6,0],[-6,1]]), Wall([[-6,1],[8,1]]), Wall([[8,1],[8,0]]), Wall([[8,0],[-6,0]])])
A26 = Area([Wall([[-8,0],[-4,0]]), Wall([[-4,0],[-4,-4]]), Wall([[-4,-4],[-8,-4]]), Wall([[-8,-4],[-8,0]])])



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
        walls1 = [Wall([[0,0],[0,6]]), Wall([[0,6],[5,6]]), Wall([[5,6],[5,0]]), Wall([[5,0],[0,0]])]
        walls2 = [Wall([[0,2],[0,6]]), Wall([[0,6],[5,6]]), Wall([[5,6],[5,0]]), Wall([[5,0],[0,2]])]
        area_rect = Area(walls1)
        area_not_rect = Area(walls2)

        self.assertEqual(area_rect.get_surface(), 30)
        self.assertFalse(area_not_rect.get_surface())

    def test_is_rectangular(self):
        walls1 = [Wall([[0,0],[0,6]]), Wall([[0,6],[5,6]]), Wall([[5,6],[5,0]]), Wall([[5,0],[0,0]])]
        walls2 = [Wall([[0,2],[0,6]]), Wall([[0,6],[5,6]]), Wall([[5,6],[5,0]]), Wall([[5,0],[0,2]])]
        area_rect = Area(walls1)
        area_not_rect = Area(walls2)

        self.assertTrue(area_rect.is_rectangular())
        self.assertFalse(area_not_rect.is_rectangular())

class TestBuilding(unittest.TestCase):
    def test_nbfloors(self):
        areas = [[A11, A12, A13],[A21, A22, A23, A24, A25, A26]]
        building = Building(areas)
        self.assertEqual(building.get_nbfloors(), 2)

if __name__ == '__main__':
    unittest.main()