from Game.ForwardModel import ForwardModel
from Game.GameState import GameState
from Heuristics.Hueristic import Heuristic


class Game:
    def __init__(self):
        self.game_state = GameState()
        self.forward_model = ForwardModel()
        self.heuristic = Heuristic()

    def run(self, track, player):
        """Runs the game."""
        self.game_state.reset(track)                           # Initialize the game state

        while not self.game_state.is_terminal():
            print(self.game_state)
            action = player.think(self.game_state)             # Player thinks the action to play given the game state
            if action is None:
                break
            self.forward_model.play(self.game_state, action)   # ForwardModel plays the action and update the game_state
            score = self.heuristic.get_score(self.game_state)  # Heuristic calculates score

        if self.game_state.reached_goal():
            print("You won!")
        else:
            print("You lost!")
