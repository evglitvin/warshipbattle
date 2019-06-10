from src.base.field import Field


class Player:
    def __init__(self, field=None):
        self._field = field or Field()

    def get_field(self):
        return self._field