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

    def step(self):
        # TODO