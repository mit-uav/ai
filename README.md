full_state = {
	
	'uav': UAVPrototype
	'roombas': [RoombaPrototype1, RoombaPrototype2, RoombaPrototype3...]
	'roomba_speed': 0.3
	'spikes': [SpikePrototype1, SpikePrototype2, SpikePrototype3...]
	'spike_speed': 0.3
}

UAVPrototype = class{
	
	def __init__(self, x, y, z):
		setPos(x,y,z)
		setVel(0,0,0)

	def setPos(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def setVel(self, x, y, z):
		self.xVel = 0
		self.yVel = 0
		self.zVel = 0
}

RoombaPrototype = class{
	
	def __init__(self, x, y, z, theta):
		setPos(x,y,z)
		self.angle = theta

	def setPos(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def setAngle(self, angle):
		self.angle = angle
}

SpikePrototype = class{
	
	def __init__(self, x, y, z, theta):
		setPos(x,y,z)
		self.angle = theta

	def setPos(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def setAngle(self, angle):
		self.angle = angle
}