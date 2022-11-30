import math
import random

from Game.ForwardModel import ForwardModel
from Heuristics.Hueristic import Heuristic


class Player:
    def __init__(self):
        self.forward_model = ForwardModel()
        self.heuristic = Heuristic()

    # def think(self, game_state):
    #     l_actions = game_state.get_actions()
    #     if len(l_actions) == 0:
    #         return None
    #
    #     return random.choice(l_actions)

    def think(self, game_state):
        """One Step Looking Ahead (OSLA)"""
        l_actions = game_state.get_actions()
        best_score = -math.inf
        best_action = None

        for action in l_actions:
            new_game_state = game_state.clone()
            self.forward_model.play(new_game_state, action)
            score = self.heuristic.get_score(new_game_state)
            if score > best_score:
                best_score = score
                best_action = action

        return best_action
