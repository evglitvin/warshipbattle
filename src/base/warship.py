from src.base.constants import Orientation
from src.base.gameobject import VisualObject


class Warship(VisualObject):
    def __init__(self, pos, size, orientation=Orientation.HORIZONTAL):
        super(Warship, self).__init__()
        assert 1 <= size <= 4
        self._size = size

    def draw(self, canvas):
        # TODO logic for drawing Field
        super(Warship, self).draw(canvas)