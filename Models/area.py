import numpy as np
import math
import matplotlib.pyplot as plt
from wall import Wall

class Area():
    def __init__(self, walls):
        """area constructor taking in argument the walls composing the area

        Args:
            walls (list(Wall)): [description]
        """
        self.walls = walls

    def is_rectangular(self):
        """
        Returns:
            [Boolean]: return True if the area is a rectangle, False if not
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
        """
        Returns:
            [int or Boolean]: returns the surface if the area is a rectangle and False if it's not
        """
        if self.is_rectangular():

            distance1 = self.walls[0].get_distance()
            distance2 = self.walls[1].get_distance()


            return distance1*distance2
        return False

    def display_area(self, ax):
        """
        This method only only plt.plot, a plt.show() needs to be added after the call of this function

        Args:
            ax ([AxesSubplot object]): Inform on which plot the Area has to be displayed
        """
        for wall in self.walls:
            point1 = wall.get_coordinates()[0]
            point2 = wall.get_coordinates()[1]

            x_values = [point1[0], point2[0]]
            y_values = [point1[1], point2[1]]

            ax.plot(x_values, y_values, c='r')


if __name__ == '__main__':  #the display feature is hard to test with only assert test so i will do it here
    A21 = Area([Wall([[-6,1],[-6,4]]), Wall([[-6,4],[-2,4]]), Wall([[-2,4],[-2,1]]), Wall([[-2,1],[-6,1]])])
    A22 = Area([Wall([[-2,1],[-2,4]]), Wall([[-2,4],[2,4]]), Wall([[2,4],[2,1]]), Wall([[2,1],[-2,1]])])
    A23 = Area([Wall([[2,1],[2,4]]), Wall([[2,4],[6,4]]), Wall([[6,4],[6,1]]), Wall([[6,1],[2,1]])])
    A24 = Area([Wall([[6,1],[6,4]]), Wall([[6,4],[8,4]]), Wall([[8,4],[8,1]]), Wall([[8,1],[6,1]])])
    A25 = Area([Wall([[-6,0],[-6,1]]), Wall([[-6,1],[8,1]]), Wall([[8,1],[8,0]]), Wall([[8,0],[-6,0]])])
    A26 = Area([Wall([[-8,0],[-4,0]]), Wall([[-4,0],[-4,-4]]), Wall([[-4,-4],[-8,-4]]), Wall([[-8,-4],[-8,0]])])
    ax = plt.subplot(111)
    A21.display_area(ax)
    A22.display_area(ax)
    A23.display_area(ax)
    A24.display_area(ax)
    A25.display_area(ax)
    A26.display_area(ax)
    plt.show()


