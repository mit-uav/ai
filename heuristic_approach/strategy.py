# example of particular strategy classes
from FollowOneRoomba import *
from DefensiveU import *
from TopOffensive import *
import random

class Strategy:
    def __init__(self):
        self.current_strategy = 0
        self.all_strategies = []
        self.initialize_strategies()
        self.history = [] # list of previous strategies taken
        self.time_in_current_strategy = 0
        
    def initialize_strategies(self):
        follow_one_roomba = FollowOneRoomba()
        defensive_U = DefensiveU()
        top_offensive = TopOffensive()
        self.all_strategies = [follow_one_roomba, defensive_U, top_offensive]
        # 0 - follow one roomba
        # 1 - defensive U
        # 2 - top offensive
        
    def act(self, full_state):
        self.actions_in_current_strategy -= 1
        if self.actions_in_current_strategy <= 0:
            self.transition(full_state)
        action = self.all_strategies[self.current_strategy].act(full_state)
        return action
        
    def transition(self, full_state):
        # logic to transition from current stategy
        self.history.append(self.current_strategy)
        self.current_strategy = random.choice(range(len(self.all_strategies)))
        
        # Transition every 10 seconds
        self.actions_in_current_strategy = 10000
        
        
class FollowOneRoomba:
    def __init__(self):
        
    def act(self, full_state):
        return (x,y,z)
        
    