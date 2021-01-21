from State import State


class Fire(State):
    def __init__(self, time_of_action, dmg):
        super().__init__(time_of_action)
        self.dmg = dmg

    def get_state(self):
        self.time_of_action -= 5
        if self.time_of_action >= 0:
            print('Fire stop!')
        return 'Fire' if self.time_of_action >= 0 else 0

    def __del__(self):
        del self

    def __str__(self):
        return 'Fire'
