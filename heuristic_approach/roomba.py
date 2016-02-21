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
        
    def step(self, board_time):
        if 
        
    def tapped(self):
        pass
    
    def could_die_in_next(self, delta_t):
        # uses direction of roomba and speed and returns 
        # wether the roomba could leave the board in delta_t miliseconds
        # *** Uses just a straight line approximation of where the roomba is moving
        travel_radius = self.speed*(1000/delta_t)
        outVec = Vector(travel_radius*math.cos(self.angle), travel_radius*math.sin(self.angle)
        if outVec.x + self.pos.x > 10 or outVec.x + self.pos.x < -10 or outVec.y + self.pos.y > 10 or outVec.y + self.pos.y < -10:
            # The roomba could go out of bounds
            return True