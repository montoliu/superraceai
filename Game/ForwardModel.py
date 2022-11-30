class ForwardModel:
    def __init__(self):
        pass

    def play(self, game_state, action):
        """Plays the action and updates the game state."""
        if action.is_left():
            game_state.decrease_velocity()
            game_state.set_player_position(game_state.player_position_row - game_state.velocity,
                                           game_state.player_position_column - 1)

        elif action.is_right():
            game_state.decrease_velocity()
            game_state.set_player_position(game_state.player_position_row - game_state.velocity,
                                           game_state.player_position_column + 1)
        else:
            game_state.increase_velocity()
            game_state.set_player_position(game_state.player_position_row - game_state.velocity,
                                           game_state.player_position_column)
