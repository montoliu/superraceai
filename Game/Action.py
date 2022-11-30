class Action:
    def __init__(self, action):
        self.action = action

    def is_left(self):
        return self.action == 0

    def is_up(self):
        return self.action == 1

    def is_right(self):
        return self.action == 2

    def get_action(self):
        return self.action

    def __eq__(self, other):
        return self.action == other.action

    def __str__(self):
        if self.is_left():
            return "LEFT "
        elif self.is_up():
            return "UP   "
        elif self.is_right():
            return "RIGHT"
