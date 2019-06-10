

class VisualObject:
    def __init__(self):
        self._children = []

    def add_child(self, obj):
        self._children.append(obj)

    def remove_child(self, obj):
        self._children.remove(obj)

    def draw(self, canvas):
        for obj in self._children:
            obj.draw(canvas)
