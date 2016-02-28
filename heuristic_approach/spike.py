class Spike(object):
    """
    init_pos: initial position Vector Object
    init_vel: initial velocity Vector Object
    spike_cfg: spike config (dictionary)
    """
    def __init__(self, init_pos, init_ang, spike_cfg):
        self.pos = init_pos
        self.angle = init_ang
        self.radius = spike_cfg['rad']
        self.speed = spike_cfg['speed']

    # INPUT: time_steps - the amount of time between this and next time steps
    # OUTPUT: action {null or displacement}
    def step(self, time_step):
        # Move in a circle clockwise direction
        # Approximate as a very high polygon shape with time_steps guiding the displacement vector

        # Stop when in a collision with roomba

        # Else move