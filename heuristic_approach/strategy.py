class Strategy(object):
    
    def __init__(self):
        pass
    
    def act(self, state):
        pass
    
    def flip_roomba(self, state):
        if state['time']%(20*1000) < 10*1000:
            # In first 10 seconds of the 20 second roomba interval
            for roomba in state['roombas']:
                if distance_between(roomba, state['uav']) <= 0:
                    roomba.tapped()
                    #break
        else:
            # In second 10 seconds of the 20 second roomba interval
            # If the roomba will die by the next 180 turn, it is flipped
            for roomba in state['roombas']:
                if distance_between(roomba, state['uav']) <= 0:
                    if roomba.could_die_in_next(20*1000 - state['time']%20*1000):
                        roomba.tapped()
                
    def distance_between(obj1, obj2):
        hpt = Math.hypot(obj1.pos.x-obj2.pos.x, obj1.pos.y-obj2.pos.y)
        return hpt - obj1.rad - obj2.rad