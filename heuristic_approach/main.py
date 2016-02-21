# config; assumes a 20 by 20 grid from -10 to 10
MAIN_CONFIG = {
    "sim_res": 30, # steps per second, simulation resolution
    "render_every": 1 # how often to render the world
}
WORLD_CONFIG = {
    "time_step": 1*(1000./MAIN_CONFIG["sim_res"]), # ms (world time) per step
    "max_time": 10*1000 # length of a game in ms
}
UAV_CONFIG = {
    "rad": 0.25, # arbitrary size of the uav in meters
    "speed": 0.15 # arbitrary speed of the uav in m/s
}
ROOMBA_CONFIG = {
    "n": 10, # number of roombas
    "rad": 0.2, # radius of the Roombas
    "speed": 0.05, # speed in m/s
    "init_dist": 5, # how far the roombas are initially
    "ang_speed": 1.38, # angular speed in radians per second
    "flip_freq": 20*1000, # rotates 180 degrees every this many ms
    "rand_rot_freq": 5*1000, # rotates randomly every this many ms
    "act_angle": 45*math.pi/180, # how much it rotates upon activation
    "rand_ang_mag": 40*math.pi/180 # how much it wiggles via random rotations
}
SPIKE_CONFIG = {
    "n": 4, # number of spikes
    "rad": 1.5*ROOMBA_SPEC.rad, # radius of the spikes
    "speed": ROOMBA_SPEC.speed, # speed of the spikes
    "init_dist": 8, # how for the spikes are initially
    "ang_speed": 1.38 # angular speed in radians per second
}

# Main interfaces the visualization with the world 
class Main(object):
    def __init__(self, main_cfg):
        self.sim_res = main_cfg["sim_res"]
        self.render_every = main_cfg["render_every"]
        
        self.vis = Visualizer()
        self.world = World(WORLD_CONFIG, UAV_CONFIG, ROOMBA_CONFIG, SPIKE_CONFIG)
        
        self.steps = 0
        
    def step_once(self):
        # call this self.sim_res times per second
        keep_going = self.world.step()
        
        # call this every self.render_every many steps
        if self.steps % self.render_every == 0:
            self.vis.render(
                self.world.getState()
            )
        self.steps++
        
        # bubble up the stop condition
        return keep_going
    
    def run(self):
        # call endlessly at a delay
        keep_going = self.step_once()
        while keep_going:
            time.sleep(1000./self.sim_res)
            keep_going = self.step_once()