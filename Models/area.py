import numpy as np
import math

class Area():
    def __init__(self, walls):
        """area constructor taking in argument the walls composing the area

        Args:
            walls (list(Wall)): [description]
        """
        self.walls = walls

    def is_rectangular(self):
        """
        return True if the area is a rectangle and False if not
        """
        if len(self.walls) == 4:  # check that there are 4 sides
            d1 = self.walls[0].get_distance()
            d2 = self.walls[1].get_distance()
            d3 = self.walls[2].get_distance()
            d4 = self.walls[3].get_distance()

            if d1 == d3 and d2 == d4: # check that opposite sides are equal

                v1 = np.array(self.walls[0].get_coordinates()[1]) - np.array(self.walls[0].get_coordinates()[0])
                v2 = np.array(self.walls[1].get_coordinates()[1]) - np.array(self.walls[1].get_coordinates()[0])

                if np.inner(v1, v2) == 0: # check if one of the angle is a right angle
                    return True
        return False


    
    def get_surface(self):
        """we suppose firstly that all area are rectangular
        """
        if self.is_rectangular():

            distance1 = self.walls[0].get_distance()
            distance2 = self.walls[1].get_distance()


            return distance1*distance2
        return False