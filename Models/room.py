from Models.area import Area

class Room(Area):
    def __init__(self, walls):
        super().__init__(walls)

# can add things that describes a room
# but not an area : windows, doors, ...