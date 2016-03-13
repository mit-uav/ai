full_state = {
	
	'uav': UAVPrototype
	'roombas': [RoombaPrototype1, RoombaPrototype2, RoombaPrototype3...]
	'spikes': [SpikePrototype1, SpikePrototype2, SpikePrototype3...]
}

UAVPrototype = class{
	
	def __init__(self, x, y, z):
		self.position = Vector(x,y,z)
		self.velocity = Vector(0,0,0)

	def set_position(self, x, y, z):
		self.pos.x = x
		self.pos.y = y
		self.pos.z = z


	def set_velocity(self, x, y, z):
		self.velocity.x = x
		self.velocity.y = y
		self.velocity.z = z
}

RoombaPrototype = class{
	
	def __init__(self, x, y, z, theta):
		self.position = Vector(x,y,z)
		self.angle = theta
		self.is_moving = false
		self.confidence = 1

	def set_position(self, x, y, z):
		self.position.x = x
		self.position.y = y
		self.position.z = z

	def set_angle(self, angle):
		self.angle = angle

	def set_moving(self, moving):
		self.is_moving = moving

	def set_confidence(self, c):
		self.confidence = c
}

SpikePrototype = class{
	
	def __init__(self, x, y, z, theta):
		setPos(x,y,z)
		self.angle = theta
		self.is_moving = false
		self.confidence = 1

	def set_position(self, x, y, z):
		self.position.x = x
		self.position.y = y
		self.position.z = z

	def set_angle(self, angle):
		self.angle = angle

	def set_moving(self, moving):
		self.is_moving = moving

	def set_confidence(self, c):
		self.confidence = c
}
}