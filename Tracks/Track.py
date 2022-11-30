import math


class Track:
    def __init__(self):
        self.track = [[0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                      [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                      [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                      [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                      [0, 0, 1, 1, 1, 1, 1, 0, 0, 0]]
        self.number_of_rows = len(self.track)
        self.number_of_columns = len(self.track[0])

    def get_initial_position(self):
        """Return the initial position of the player"""
        return 5, 4

    def is_goal(self, row, column):
        """Return True if the given position is the goal position"""
        return row <= 0 and column in [2, 3, 4, 5]

    def is_crashed(self, row, column):
        """Return True if the player is crashed"""
        return self.track[row][column] == 0

    def print_track(self, row, column):
        """Return a string representation of the track"""
        s = ""
        for r in range(self.number_of_rows):
            for c in range(self.number_of_columns):
                if r == row and c == column:
                    s += "X"
                elif self.track[r][c] == 1:
                    s += " "
                else:
                    s += "#"
            s += "\n"
        return s

    def get_goals(self):
        return [[0, 2], [0, 3], [0, 4], [0, 5], [0, 6]]

    def get_distance_to_goal(self, row, column):
        l_goals = self.get_goals()
        best_distance = math.inf
        for goal in l_goals:
            distance = math.sqrt((row - goal[0])**2 + (column - goal[1])**2)  # euclidean distance
            if distance < best_distance:
                best_distance = distance
        return best_distance

    def clone(self):
        clone = Track()
        for row in range(self.number_of_rows):
            for col in range(self.number_of_columns):
                clone.set_cell(row, col, self.get_cell(row, col))
        return clone

    def set_cell(self, row, col, value):
        self.track[row][col] = value

    def get_cell(self, row, col):
        return self.track[row][col]