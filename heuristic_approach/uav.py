class UAV(object):
    """
    init_pos: initial position Vector Object
    init_vel: initial velocity Vector Object
    uav_cfg: UAV config (dictionary)
    """
     def __init__(self, init_pos, init_ang, uav_cfg):
        self.pos = init_pos
        self.angle = init_ang
        self.radius = uav_cfg['rad']
        self.speed = uav_cfg['speed']
