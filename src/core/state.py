from abc import ABC, abstractmethod


class BaseState(ABC):
    def __repr__(cls):
        return f'[STATE] I am {cls.__name__}'

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @abstractmethod
    def whoami(self):
        pass


class BeforeGameState(BaseState):
    @classmethod
    def whoami(cls):
        print(cls.__repr__(cls))


class InGameState(BaseState):
    @classmethod
    def whoami(cls):
        print(cls.__repr__(cls))
        # change the state from the <State> obj
        cls.context.transition_to(AfterGameState)


class AfterGameState(BaseState):
    @classmethod
    def whoami(cls):
        print(cls.__repr__(cls))
