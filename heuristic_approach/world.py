# World manages the UAVs and Roombas
class World(object):
    def __init__(self, world_cfg, uav_cfg, roomba_cfg, spike_cfg):
        # set up world state
        self.t = 0 # global time
        self.time_step = world_cfg["time_step"]
        self.max_time = world_cfg["max_time"]
        
        # make the uav
        self.uav = UAV(uav_cfg)
        
        # make n roombas in a circle
        self.roombas = []
        for i in range(roomba_cfg.n):
            theta = i * (2*math.pi / roomba_cfg.n);
            x = roomba_cfg.init_dist * math.cos(theta);
            y = roomba_cfg.init_dist * math.sin(theta);
            self.roombas.append(
                Roomba(Vector(x, y), theta, roomba_cfg)
            )
        
        # make m spikes also in a circle
        self.spikes = []
        for i in range(spike_cfg.n):
            theta = i * (2*math.pi / spike_cfg.n);
            x = spike_cfg.init_dist * math.cos(theta);
            y = roomba_cfg.init_dist * math.sin(theta);
            self.spikes.append(
                Spike(Vector(x, y), spike_cfg)
            )
    
    def step(self):
        # handle collisions by checking for them and updating velocities
        # TODO
        
        # move the roombas and spikes
        for roomba in self.roombas:
            roomba.act(self.time_step)
        for spike in self.spikes:
            spike.act(self.time_step)
            
        # get the uav to act
        curr_state = self.getState()
        action = uav.act(self.time_step, curr_state)
        if action == 'tap':
            # tap at the uav's current position
            # TODO
        
        # keep track of time
        self.t += self.time_step
        
        return True # True if the simulation is not over
    