# example of particular strategy classes
from FollowOneRoomba import *
from DefensiveU import *
from TopOffensive import *
import random
import rospy

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
        circle = Circle(self.get_time())
        self.all_strategies = [follow_one_roomba, defensive_U, top_offensive, circle]
        # 0 - follow one roomba
        # 1 - defensive U
        # 2 - top offensive
        
    def act(self, full_state):
        self.actions_in_current_strategy -= 1
        if self.actions_in_current_strategy <= 0:
            self.transition(full_state)
        action = self.all_strategies[self.current_strategy].act(full_state, self.get_time())
        # TODO:
        # Publish this action to the destination ROS node
        return action
        
    def transition(self, full_state):
        # logic to transition from current stategy
        self.history.append(self.current_strategy)
        self.current_strategy = random.choice(range(len(self.all_strategies)))
        
        # Transition every 10 seconds
        self.actions_in_current_strategy = 10000
    
    def getState(self):
        # Update with ROS msg
        
        # sort roombas by confidence and put into a list in fullstate
        return fullstate
        
    def get_time(self):
        return rospy.get_time()
    
    def distance_between(self, p1, p2):
        return math.sqrt(math.pow(p1.x-p2.x,2),math.pow(p1.t-p2.y,2),math.pow(p1.z-p2.z,2))
        
class FollowOneRoomba:
    def __init__(self, fullstate):
        self.roombas = fullstate.roombas 
        # select roomba to follow
        if self.roomba == null: # choose some roomba in sight (with high "confidence")
            self.roomba = 
        elif # if current roomba is out of sight, pick new roomba
            self.roomba = 
        self.position = fullstate.uav.position
        self.time = fullstate.time
        
    def act(self, full_state):
        
        return (x,y,z)
        
class Circle:
    
    def __init__(self, time):
        self.lastTime = time
        self.DT_THRESHOLD = 1 # second
        
        # Set up the points of the circle for the UAV to traverse
        # Move along circle at z = 2
        self.NUM_CIRCLE_POINTS = 12
        RADIUS = 5
        self.sweet_spots = []
        for i in range(self.NUM_CIRCLE_POINTS):
            angle = map(i,0,self.NUM_CIRCLE_POINTS,0,2*math.pi)
            self.sweetspots.append(Vector(RADIUS*math.cos(angle),RADIUS*math.sin(angle),2)
        self.target_index = None
        
    def act(self, full_state, newTime):
        dTime = newTime - self.lastTime
        self.lastTime = newTime
        
        if dTime > self.DT_THRESHOLD:
            # If the time has elapsed a certain amount, don't expect to be on the circular path
            self.target_index = None
        
        # Calculate the next target
        if self.next_target == None:
            # Find closest point in the sweetspots
            closest_index = 0
            closest_dist = 10000 # Arbitrarily high
            for index in range(len(self.sweet_spots)):
                dist = dist_between(full_state['uav'].position,self.sweet_spots[index])
                if  dist < closest_dist:
                    closest_index = index
                    closest_dist = dist
            
            self.target_index = closest_index
        
        if dist_between(full_state['uav'].position, self.sweet_spots[self.target_index]) < .5:
            # If the UAV is within half meter of the next sweet_spot, tell it to move to the next one
            self.target_index += 1
            self.target_index = self.target_index % (self.NUM_CIRCLE_POINTS)
        
        return self.sweet_spots[self.target_index] # Returns position Vector
    