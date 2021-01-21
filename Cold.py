from State import State


class Cold(State):
    def __init__(self, time_of_action):
        super().__init__(time_of_action)

    def get_state(self):
        self.time_of_action -= 1
        if self.time_of_action == 0:
            print('Cold finish!')
        return 'Cold' if self.time_of_action >= 0 else False

    def __del__(self):
        del self

    def __str__(self):
        return 'Cold'
