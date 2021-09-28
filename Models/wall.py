from Models.element import Element

class Wall(Element):
    def __init__(self, coordinates):
        """wall constructor taking coordinates of two diagonally opposed points of the wall
        we consider that the width is null
        Args:
            coordinates (list of two couple): [description]
        """
        self.coordinates = coordinates

