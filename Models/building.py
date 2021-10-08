import matplotlib.pyplot as plt
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
        plt.figure(figsize=(9,9))
        ax = plt.subplot(2)
        for floor in self.areas:
            for area in floor:
                pass
                # TO DO : plot the area on the corresponding subplot(=floor)
    

