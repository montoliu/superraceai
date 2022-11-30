from Game.Action import Action


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

    def get_actions(self):
        """Return a list of actions that can be played"""
        l_actions = [Action(0), Action(1), Action(2)]
        return l_actions

    def increase_velocity(self):
        """Increase the velocity of the player"""
        self.velocity += 1
        if self.velocity > 3:
            self.velocity = 3

    def decrease_velocity(self):
        """Decrease the velocity of the player"""
        self.velocity -= 1
        if self.velocity < 1:
            self.velocity = 1

    def get_distance_to_goal(self):
        return self.track.get_distance_to_goal(self.player_position_row, self.player_position_column)

    def clone(self):
        clone = GameState()
        clone.track = self.track.clone()
        clone.player_position_row = self.player_position_row
        clone.player_position_column = self.player_position_column
        clone.velocity = self.velocity
        return clone
