from src.core.player.bot import BotPlayer
from src.core.player.human import HumanPlayer
from src.core.state import MainMenuState, SetUpOnePlayerGameState, SetUpMultiPlayerGameState, InGameState, \
    GoToMainMenuState, AfterGameState


class Game:

    def __init__(self):
        self._state = MainMenuState()
        self._previous_state = None

        self._player_one = None
        self._player_two = None
        self._field = None

    @property
    def player_one(self):
        return self._player_one

    @player_one.setter
    def player_one(self, player):
        self._player_one = player

    @property
    def player_two(self):
        return self._player_two

    @player_two.setter
    def player_two(self, player):
        self._player_two = player

    @property
    def field(self):
        return self._field

    @field.setter
    def field(self, field):
        self._field = field

    @property
    def previous_state(self):
        return self._previous_state

    @previous_state.setter
    def previous_state(self, previous_state):
        self._previous_state = previous_state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    def setup_one_player_game(self):
        # TODO: we should think how, when, where should be set up _field
        self.player_one(HumanPlayer())
        self.player_two(BotPlayer())
        self.previous_state = self.state
        self.state = SetUpOnePlayerGameState()
        self.state.draw()

    def setup_multi_player_game(self):
        # TODO: we should think how, when, where should be set up _field
        self.player_one(HumanPlayer())
        self.player_two(HumanPlayer())
        self.previous_state = self.state
        self.state = SetUpMultiPlayerGameState()
        self.state.draw()

    def start_game(self):
        # TODO: some requirements should be checked here before starting game
        self.previous_state = self.state
        self.state = InGameState()
        self.state.draw()

    def exit_game(self):
        self.previous_state = self.state
        self.state = GoToMainMenuState()
        self.state.draw()

    def finish_game(self):
        self.previous_state = self.state
        self.state = AfterGameState()
        self.state.draw()
