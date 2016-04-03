from __future__ import division
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

class UAVControl:

	def __init__(self,sweetSpots):
		rospy.init_node('reconController')
		self.setDesiredStatePub = rospy.Publisher('/uav/destination', Pose)
		self.getCurrentStateSub = rospy.Subscriber('/ground_truth/state', Odometry, self.doRecon)
		self.sweetSpots  = sweetSpots
		self.targetIndex = 0
		print "Iniitializing Recon controller"
		#os.system("rosservice call /ardrone/togglecam") #camera is default front
		#os.system("rostopic pub -1 /ardrone/takeoff std_msgs/Empty")

	def doRecon(self, msg):
		pose = msg.pose.pose.position
		x=pose.x 
		y=pose.y #check if at recon point
		z=pose.z
		if abs(x-self.sweetSpots[self.targetIndex][0])<.3 and abs(y-self.sweetSpots[self.targetIndex][1])<.3 and abs(z-self.sweetSpots[self.targetIndex][2])<.2:
			self.targetIndex=(1+self.targetIndex)%len(self.sweetSpots)
			
		x,y,z=self.sweetSpots[self.targetIndex]
		position=Pose()
		position.position.x=x 
		position.position.y=y 
		position.position.z=z
		self.setDesiredStatePub.publish(position) #go to recon point

	
if __name__ == "__main__":
	try:
		# Go in square
		# uav = UAVControl([(5,5),(5,-5),(-5,-5),(-5,5)])

		# Go in circle oscillating height
		ss = []
		rad = 5
		numPoints = 40
		for i in range(numPoints):
			ss.append((rad*math.sin(2*math.pi*(i/numPoints)),rad*math.cos(2*math.pi*(i/40)),2+math.sin(i*math.pi/8)))
		uav = UAVControl(ss)
		rospy.spin()
	except rospy.ROSInterruptException:
		pass
