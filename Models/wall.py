from Models.element import Element
import math

class Wall(Element):
    def __init__(self, coordinates):
        """wall constructor taking coordinates of two diagonally opposed points of the wall
        we consider that the width is null
        Args:
            coordinates (list of two two-item list): [description]
        """
        self.coordinates = coordinates
    
    def get_distance(self):
        p1 = self.get_coordinates()[0]
        p2 = self.get_coordinates()[1]

        return math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

