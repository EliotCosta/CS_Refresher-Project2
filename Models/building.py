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
