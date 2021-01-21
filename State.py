from __future__ import annotations
from abc import abstractmethod


@abstractmethod
class State:
    def __init__(self, time_of_action):
        self.time_of_action = time_of_action

    def get_state(self):
        return

    def __str__(self):
        return
