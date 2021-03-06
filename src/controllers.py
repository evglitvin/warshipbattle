class UserController:
    """
    Class is responsible for:
    - provide opponents (a human or a bot)
    - switch active user
    - users queue
    - bot player behaviour
    """
    def __init__(self):
        self.players = []
        pass

    def create_opponent(self, bot=True):
        if bot:
            player = self.create_bot()
        else:
            player = self.create_human()
        self.players.append(player)

    def init_field(self):
        pass

