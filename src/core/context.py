from abc import ABC
"""
Game state could be changed from the <Context> object 
as well as from any <BaseState> descendant
"""


class Context(ABC):
    _state = None

    def __init__(self, state):
        self.transition_to(state)

    def transition_to(self, state):
        print(f"[CONTEXT] Transition to {state.__name__}")
        self._state = state
        self._state.context = self
        self._state.whoami()
