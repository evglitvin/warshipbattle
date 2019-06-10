from src.core.ship.orientation import Orientation
from src.core.ship.ship_state import ShipState
from src.core.visual import Visual


class Ship(Visual):
    def __init__(self, initial_position, size, orientation):
        super(Ship, self).__init__()
        self.orientation: Orientation = orientation
        self.size: int = size
        # need to create position type
        # (complex object of initial_point + orientation?)
        self._position = initial_position
        self.state = ShipState.unknown

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    def draw(self, field):
        pass
