class Roomba(object):
    """
    init_pos: initial position Vector Object
    init_vel: initial velocity Vector Object
    roomba_cfg: roomba config (dictionary)
    """
    def __init__(self, init_pos, init_ang, roomba_cfg):
        self.pos = init_pos
        self.angle = init_ang
        self.radius = roomba_cfg['rad']
        self.speed = roomba_cfg['speed']
        
    # INPUT: time - time since game started in miliseconds
    #        time_step - the amount of time between this and next time steps
    # OUTPUT: an action {null, angular movement, or displacement} the roomba wants to take
    def act(self, time, time_step):
        # Every 20 seconds turn 180 degrees

        # Every 5 seconds (except the 180 turns) noise +/- 20 degrees

        # Else move straight at velocity m/s

        
    def tapped(self):
        
    
    