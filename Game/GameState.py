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
        s = "Position: " + str(self.get_player_position()) + "\n"
        s += "Velocity: " + str(self.velocity) + "\n"
        s += self.track.print_track(self.player_position_row, self.player_position_column)
        return s

    def is_terminal(self):
        """Return True if the game is over"""
        return self.reached_goal() or self.crashed()

    def reached_goal(self):
        """Return True if the player reached the goal"""
        return self.track.is_goal(self.player_position_row, self.player_position_column)

    def crashed(self):
        """Return True if the player crashed"""
        return self.track.is_crashed(self.player_position_row, self.player_position_column)

