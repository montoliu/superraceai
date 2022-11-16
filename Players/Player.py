from Game.Action import Action


class Player:
    def __init__(self):
        print("Player is initialized")

    def think(self, game_state):
        print("Player is thinking")
        return Action()
