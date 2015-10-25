from __future__ import division
import math
import numpy

class IARC_simulator():
    # Board Description:
    #
    # Board is a GRID_DIM_X width by GRID_DIM_Y height board with each unit representing one meter.
    # The coordinate (0,0) will be placed in the center of the board (GRID_DIM_X/2, GRID_DIM_Y/2)
    # Similar to a cartesian coordinate system, moving "up / North" on the screen or board will indicate positive Y values
    # and moving "right / East" on the screen or board will indicate a positive X value
    
	ROOMBA_SPEED = 0.33 # normal speed of the roomba (m/s)
	UAV_MAX_SPEED = 3 # maximum speed of UAV (m/s)
	ROOMBA_COUNT = 10 # number of roombas
	OBSTACLE_ROOMBA_COUNT = 4 # number of obstacle roombas
	GRID_SIZE = 20 # length and width of grid
	DELTA_TIME = 0.1 # timestep
	MAX_TIME = 600 # seconds
	MAX_TAP = 6 # maximum number of taps
	

	def __init__(self):
		# required instance variables: 
		# 	statespace_limits, continuous_dims, DimNames, episodeCap, actions_num, discount_factor
		self.external_state_struct = None
		self.state_vec = None
		
		uav_loc_lims = [[0,GRID_SIZE], [0,GRID_SIZE]]
		uav_vel_lims = [[0,UAV_MAX_SPEED], [0,GRID_SIZE]]
		roomba_loc_lims = [[0,GRID_SIZE] of roomba in range(ROOMBA_COUNT)]
		roomba_dirs_lims = [[0,2*math.pi] of roomba in range(ROOMBA_COUNT)]
		roomba_conf_lims = [[0,1] of roomba in range(ROOMBA_COUNT)]
		time_dims = [[0,MAX_TIME]]
		roomba_speed_dims = [[0,ROOMBA_SPEED] for roomba in range(ROOMBA_COUNT)]
		
		self.statespace_limits = uav_loc_lims + uav_vel_lims + roomba_loc_lims + roomba_dirs_lims +
		    roomba_conf_lims + time_dims + roomba_speed_dims
		
		total_continuous_dims = 4+3*ROOMBA_COUNT
		self.continuous_dims = [i for i in range(total_continuous_dims)]
		
		uav_loc_name = ['UAV_LOC_X', 'UAV_LOC_Y']
		uav_vel_name = ['UAV_SPEED','UAV_DIRECTION']
		roomba_loc_name, roomba_dir_name, roomba_conf_name = [], [], []
		for i in range(ROOMBA_COUNT):
	    	roomba_loc_name.append('ROOMBA_'+str(i)+'_'+'X')
	    	roomba_loc_name.append('ROOMBA_'+str(i)+'_'+'Y')
	    	roomba_dir_name.append('ROOMBA_'+str(i)+'_'+'DIR')
	    	roomba_conf_name.append('ROOMBA_'+str(i)+'_'+'CONFIDENCE')
	    time_name = ['CURRENT_TIME']
	    roomba_speed_name = ['ROOMBA_SPEED']
	    
	    self.DimNames = uav_loc_name + uav_vel_name + roomba_loc_name + roomba_dir_name + 
	        roomba_conf_name + time_name + roomba_speed_name
		self.episodeCap = MAX_TIME/DELTA_TIME
		
		self.actions_num = ROOMBA_COUNT*MAX_TAP
		
		self.discount_factor = 0.9
		
		self.time = 0
		
		self.roombas = [] #list of n roomba object
		self.uav = None
		
    # required function, initializes internal/external structure
    def s0(self):
        # uav state features
        uav_loc = [0,0] # start uav in center of board
        uav_vel = [0,0] # start uav with no velocity
        
        self.uav = UAV(uav_loc, uav_vel) # UAV object
        
        # creates n roomba objects and with differnt initial locations and directions
        theta = 2*math.pi/ROOMBA_COUNT
        for i in range(ROOMBA_COUNT):
            roomba_loc = [math.cos(theta*i), math.sin(theta*i)]
            roomba_vel = [ROOMBA_SPEED, theta*i]
            self.roombas.append(Roomba(roomba_loc, roomba_vel))
        
        # roomba state features
        roomba_locs = [roomba.get_x(),roomba.get_y() for roomba in self.roombas]
        roomba_dirs = [roomba.get_vel()[1] for roomba in self.roombas]
        roomba_confs = [1 for roomba in self.roombas]
        roomba_speeds = [roomba.get_vel()[0] for roomba in self.roombas]
        
        # create insstance of External State Structure
        self.external_state_struct = ExternalStructure(
            self.uav.get_location(),
            self.uav.get_velocity(),
            roomba_locs,
            roomba_dirs,
            roomba_confs,
            self.time,
            roomba_speeds)
        
        self.state_vec = self.external_state_struct.struct_to_vector()
        return self.state_vec, self.isTerminal()
    
    def possibleActions(self):
        # TODO
        
        
            
    def isTerminal(self):
        for roomba in self.roombas:
            if abs(roomba.get_x()) < GRID_SIZE/2 and abs(roomba.get_y()) < GRID_SIZE/2:
                return False
        return True
    
    # required function, updates internal/external structure
    def step(self, action):
        # ACTION DEFINITION:
        #
        # Action a = [roomba_index, tap_count]
        # where the roomba index is the index of a roomba in play,
        # and the number of taps is [1,6]
        self.time += DELTA_TIME
        
        #TODO (map action to [roomba_index, tap_count])
        
        roomba_index, tap_count = action
        roomba = self.roombas[roomba_index]
        if numpy.linalg.norm(uav.get_location()-roomba.get_location) <= 0.05:
            # TODO
            self.tap(roomba_index, tap_count)
        else:
            # TODO
            walk()
    # TODO
    def tap(self, roomba_index, tap_count)
        #update self.roombas[roomba_index]
    
     # TODO
    def walk(self, roomba_index, tap_count)
        #update self.roombas[roomba_index]
        


# defines features of the state exposed to agent
class ExternalStructure():
	'''
		:param uav_loc = [x,y]
		:param uav_vel = [speed, dir] - dir is between 0 and TWO_PI)
		:roomba_locs = [x_1,y_1,...,x_n,y_n]
		:roomba_dirs = [dir1,...,dir_n]
		:roomba_confs = [conf1,...,confn]
		:time = time
		:roomba_speeds = [s_1, s_2,..., s_n] - s is either 0 or .3333
	'''
	def __init__(self, uav_loc, uav_vel, roomba_locs, roomba_dirs, roomba_confs, time, roomba_speeds):
		self.uav_loc = uav_loc
		self.uav_vel = uav_vel
		self.roomba_locs = roomba_locs
		self.roomba_dirs = roomba_dirs
		self.roomba_confs = roomba_confs
		self.time = [time]
		self.roomba_speeds = roomba_speeds

	# combines features to get state vector
	def state_to_vector(self):
		return self.uav_loc + self.uav_vel + self.roomba_locs + roomba_dirs + roomba_confs + time
	
	# setter functions
	def set_uav_loc(self, uav_x, uav_y):
        self.uav_loc = [uav_x, uav_y]
        
    def set_uav_vel(self, vel_x, vel_y):
        self.uav_vel = [vel_x, vel_y]
        
    def set_roomba_locs(self, roomba_locs):
        self.roomba_locs = roomba_locs
        
    def set_roomba_dirs(self, roomba_dirs):
        self.roomba_dirs = roomba_dirs
        
    def set_roomba_confs(self, roomba_confs):
        self.roomba_confs = roomba_confs
        
    def set_time(self, t):
        self.time = [t]
        
    def set_roomba_speed(self, roomba_speeds):
        self.roomba_speed = roomba_speeds


# # defines features of the internal state
# class InternalStructure():
# 	'''
# 		:param uav_loc = [x,y]
# 		:param uav_vel = [speed, dir]
# 		:roomba_locs = [x_1,y_1,...,x_n,y_n]
# 		:roomba_dirs = [dir1,...,dir_n]
# 		:roomba_confs = [conf1,...,confn]
# 		:time = time
# 		:current_
# 	'''
# 	def __init__(self, uav_loc, uav_vel, roomba_locs, roomba_dirs, roomba_confs, time = 0, ):
# 	    self.uav_loc = uav_loc
# 		self.uav_vel = uav_vel
# 		self.roomba_locs = roomba_locs
# 		self.roomba_dirs = roomba_dirs
# 		self.roomba_confs = roomba_confs
# 		self.time = time
		

class Roomba():
	'''
		:param loc is list [x,y], for continuous X,Y within [-10,10]
		:param vel is list [speed, direction] for direction is angle in radians
	'''
	
	def __init__(self, location, velocity):
		self.x, self.y = location
		self.speed, self.direction = velocity

	# setter functions
	def set_loc(self, new_location):
		self.x, self.y = new_location
    def set_vel(self, vel):
        self.speed, self.direction = vel
    
    # getter functions
    def get_loc(self):
        return [self.x, self.y]
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_vel(self):
        return [self.speed, self.direction]
        
    def roomba_step(self, delta_time):
        if self.speed == 0:
            #TODO
        else:
    		delta_x = delta_time * speed * math.cos(self.direction)
    		delta_y = delta_time * speed * math.sin(self.direction)
    		self.x += delta_x
    		self.y += delta_y
    		
class UAV():
	'''
		:param loc is list [x,y], for continuous X,Y within [-10,10]
		:param vel is list [speed, direction], for speed in [0,3] and direction in [0,2pi)
	'''
	def __init__(self, location, velocity):
		self.x, self.y = location
		self.speed, self.direction = velocity
		
	# set functions
	def set_vel(self, new_velocity):
		self.speed, self.direction = new_velocity
	def set_loc(self, new_location):
		self.x, self.y = new_location
		
	# get functions
	def get_vel(self):
	    return [self.speed, self.direction]
	def get_loc(self):
	    return [self.x, self.y]
	    
	def uav_step(self, delta_time):
		# updates location of the uav after one second
		delta_x = delta_time * speed * math.cos(self.direction)
		delta_y = delta_time * speed * math.sin(self.direction)
		self.x += delta_x
		self_y += delta_y

