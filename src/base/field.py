"""
@startuml
class User
User -> Field
@enduml
"""
from src.base.gameobject import VisualObject


class Field(VisualObject):
    def __init__(self, width=10, height=10):
        super(Field, self).__init__()
        self._width = width
        self._height = height

    def draw(self, canvas):
        # TODO logic for drawing Field
        super(Field, self).draw(canvas)
