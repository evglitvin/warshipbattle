from abc import ABC, abstractmethod


"""
Game state could be changed from the <Context> object as well as from any <BaseState> descendant
"""


class Context(ABC):
    _state = None

    def __init__(self, state):
        self.transition_to(state)

    def transition_to(self, state):
        print(f"[CONTEXT] Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def get_active_state(self):
        self._state.whoami()


class BaseState(ABC):
    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @abstractmethod
    def whoami(self) -> None:
        pass


class BeforeGameState(BaseState):
    def whoami(self):
        print(f'[STATE] I am <BeforeGameState>')


class InGameState(BaseState):
    def whoami(self):
        print(f'[STATE] I am <InGameState>')


class AfterGameState(BaseState):
    def whoami(self):
        print(f'[STATE] I am <AfterGameState>')
        # change the state from the <State> obj
        self.context.transition_to(InGameState())


if __name__ == "__main__":
    context = Context(BeforeGameState())
    context.get_active_state()
    # change the state from the <Context> obj
    context.transition_to(AfterGameState())
    context.get_active_state()
