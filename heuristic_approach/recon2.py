import math
import random
import os
import time
import subprocess
import rospy
from threading import Thread
from rosgraph_msgs.msg import Clock

from gazebo_msgs.msg import ModelState
from gazebo_msgs.msg import ModelStates

from geometry_msgs.msg import Pose
from geometry_msgs.msg import Twist

from nav_msgs.msg import Odometry

# add this line to ~/.bashrc to help with importing the needed messages
# export PYTHONPATH="${PYTHONPATH}:/opt/ros/indigo/lib/python2.7/dist-packages"
pathToComm = os.path.dirname(os.path.abspath(__file__))#"/home/sam/Desktop/pixhawk/src/"

class FollowController:
	sec = 0
	roombaUpdateTime = 0
	closestRoomba = None

	def __init__(self):
		rospy.init_node('followController')
		self.uav = UAV_Simple()
		self.time_subscriber = rospy.Subscriber('/clock', Clock, self.getTime)		
		# replace this line with land mode at 0 speed
		self.setDesiredStatePub = rospy.Publisher('/uav/destination', Pose, queue_size = 0)
		self.getCurrentStateSub = rospy.Subscriber('/ground_truth/state', Odometry, self.setTrueState)
		self.getRoombaSub = rospy.Subscriber('/gazebo/model_states', ModelStates, self.roombaStates)
		print "Iniitializing UAV follow controller"
	
	def setTrueState(self, modelState):
		self.uav.setState(modelState.pose.pose, self.secondsPassed())

	def getTime(self, timeMessage):
		self.sec = rospy.get_time()
		#self.sec = timeMessage.secs
		#self.nsec = timeMessage.nsecs
		if (self.simulationActive):
			self.update()

	def update(self):
		# TODO check if we should stop moving.
		goTo = self.act()
		if (goTo is not False):
			# Hover over closest Roomba at 3m
			goTo.position.z = 3
			self.setDesiredStatePub.publish(goTo)

	def act(self):
		# look at roombas and find the closest one
		# return a position in the form of Pose, or false
		if not self.closestRoomba is None:
			return self.closestRoomba
		return False

	def secondsPassed(self):
		return self.sec + self.nsec*10**-9 - self.zeroTime

	def roombaStates(self, states):
		# first check if at least 1 second has passed since last check
		if (self.roombaUpdateTime + 1 > self.secondsPassed()):
			return

		closestDist = 20*(2**(0.5)) # max field distance
		closest = -1
		for i in range(len(states.name)):
			name = states.name[i]
			pose = states.pose[i]
			if not name.startswith('create'):
				continue
			dist = self.getDistance(pose)
			if (dist < closestDist):
				closestDist = dist
				closest = i

		self.roombaUpdateTime = self.secondsPassed()
		if (closest > -1):
			print "closestRoomba index: "+ str(closest)
			self.closestRoomba = states.pose[closest]
		else:
			print "Unable to find the closest roomba"
			self.closestRoomba = None

	def getDistance(self, you):
		me = self.uav.getState()
		sqdist = (me.position.x - you.position.x)**2 + (me.position.y - you.position.y)**2
		return sqdist**(0.5)

	def start(self):		
		# subscribe to simulator time
		self.zeroTime = self.secondsPassed()
		self.simulationActive = True
		# update each roomba
		# while (not rospy.is_shutdown() and self.simulationActive):
		# 	now = rospy.get_rostime()

class UAV_Simple:
	def __init__(self):
		self.current = None

	def setState(self, position, secondsPassed):
		self.current = position
		return False

	def getState(self):
		return self.current

if __name__ == "__main__":
	fc = FollowController()
	fc.start()
