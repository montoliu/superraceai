import random


class Player:
    def __init__(self):
        pass

    def think(self, game_state):
        l_actions = game_state.get_actions()
        if len(l_actions) == 0:
            return None

        return random.choice(l_actions)

