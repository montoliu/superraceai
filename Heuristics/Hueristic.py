class Heuristic:
    def __init__(self):
        self.worst = -10000
        self.best = 10000

    def get_score(self, game_state):
        """Returns a score for the given game state."""
        if game_state.reached_goal():
            return self.best
        if game_state.crashed():
            return self.worst
        return -1.0 * game_state.get_distance_to_goal()


