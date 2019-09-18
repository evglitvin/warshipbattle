from abc import ABC


class BaseState(ABC):

    def __repr__(cls):
        return f'[STATE] I am {cls.__name__}'

    def draw(self):
        pass

    @classmethod
    def whoami(cls):
        return cls.__name__


class MainMenuState(BaseState):
    pass


class SetUpOnePlayerGameState(BaseState):
    pass


class SetUpMultiPlayerGameState(BaseState):
    pass


class InGameState(BaseState):
    pass


class GoToMainMenuState(BaseState):
    pass


class AfterGameState(BaseState):
    pass
