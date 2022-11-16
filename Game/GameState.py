class GameState:
    def __init__(self):
        self.track = None
        self.player_position_row = 0
        self.player_position_column = 0
        self.velocity = 1

    def reset(self, track):
        """Initialize the game state"""
        self.track = track
        self.player_position_row, self.player_position_column = track.get_initial_position()
        self.velocity = 1

    def get_player_position(self):
        """Return the current position of the player"""
        return self.player_position_row, self.player_position_column

    def set_player_position(self, row, column):
        """Set the current position of the player"""
        self.player_position_row = row
        self.player_position_column = column

    def __str__(self):
        """Return a string representation of the game state"""
        s = "Player position: " + str(self.get_player_position())
        s += "Velocity: " + str(self.velocity)
        s += self.track.print_track(self.player_position_row, self.player_position_column)
        return s
