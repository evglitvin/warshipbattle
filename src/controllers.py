class UserController:
    """
    Class is responsible for:
    - provide opponents (a human or a bot)
    - switch active user
    - users queue
    """"
    def __init__():
        self.players = []
        pass

    def create_opponent(self, bot=True):
        if bot == True:
            player = selt.create_bot()
        else:
            player = self.create_human()
        self.players.append(player)


