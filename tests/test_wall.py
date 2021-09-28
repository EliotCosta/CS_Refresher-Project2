import unittest
from Models.wall import Wall

class TestWall(unittest.TestCase):
    def test_get_coordinates(self):
        wall=Wall([(0,0),(6,2)])
        
        self.assertEqual(wall.get_coordinates(), [(0,0),(6,2)])

if __name__ == '__main__':
    unittest.main()