import matplotlib.pyplot as plt
from area import Area
from wall import Wall

class Building():
    def __init__(self, areas):
        """
        building constructors that takes a list of lists of Area (mostly rooms) that will define the building

        Args:
            areas (list of list of Area): list of list of areas, the index of the Area list corresponding to the floor 
        """
        self.areas = areas

    def get_nbfloors(self):
        return len(self.areas)

    def get_nb_of_areas(self):
        count = 0
        for floor in self.areas:
            for area in floor:
                count += 1
        return count
    
    def display_building(self):
        plt.figure(figsize=(18,9))
        n = self.get_nbfloors()
        for id_floor in range(len(self.areas)):
            ax = plt.subplot(1,n,id_floor+1, title=f'floor n°{id_floor+1}')

            for area in self.areas[id_floor]:
                area.display_area(ax)
                
        plt.legend()
        plt.show()
    

if __name__ == '__main__':


    A11 = Area([Wall([[0,0],[0,6]]), Wall([[0,6],[5,6]]), Wall([[5,6],[5,0]]), Wall([[5,0],[0,0]])])
    A12 = Area([Wall([[0,0],[0,3]]), Wall([[0,3],[-3,3]]), Wall([[-3,3],[-3,0]]), Wall([[-3,0],[0,0]])])
    A13 = Area([Wall([[-6,0],[-6,-4]]), Wall([[-6,-4],[5,-4]]), Wall([[5,-4],[5,0]]), Wall([[5,0],[-6,0]])])

    A21 = Area([Wall([[-6,1],[-6,4]]), Wall([[-6,4],[-2,4]]), Wall([[-2,4],[-2,1]]), Wall([[-2,1],[-6,1]])])
    A22 = Area([Wall([[-2,1],[-2,4]]), Wall([[-2,4],[2,4]]), Wall([[2,4],[2,1]]), Wall([[2,1],[-2,1]])])
    A23 = Area([Wall([[2,1],[2,4]]), Wall([[2,4],[6,4]]), Wall([[6,4],[6,1]]), Wall([[6,1],[2,1]])])
    A24 = Area([Wall([[6,1],[6,4]]), Wall([[6,4],[8,4]]), Wall([[8,4],[8,1]]), Wall([[8,1],[6,1]])])
    A25 = Area([Wall([[-6,0],[-6,1]]), Wall([[-6,1],[8,1]]), Wall([[8,1],[8,0]]), Wall([[8,0],[-6,0]])])
    A26 = Area([Wall([[-8,0],[-4,0]]), Wall([[-4,0],[-4,-4]]), Wall([[-4,-4],[-8,-4]]), Wall([[-8,-4],[-8,0]])])

    areas = [[A11, A12, A13],[A21, A22, A23, A24, A25, A26]]
    building = Building(areas)
    building.display_building()