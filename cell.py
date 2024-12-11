from grid_object import GridObject


class Cell(GridObject):
    def __init__(self, pos):
        super().__init__(pos, (0, 0, 0))

    