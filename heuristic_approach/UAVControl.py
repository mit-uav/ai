from Strategy import *

class UAVControl:
    def __init__():
        self.strategy = Strategy()
        self.uav = UAV()
        
    def update(self, full_state):
        (x,y,z) = stategy.act(full_state)
        self.uav.goTo(x,y,z)
        # TODO: figure out how (x,y,z) gets executed
        # publish to ROS node or directly update UAV external model class