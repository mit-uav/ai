import random
import copy
import numpy
import math

DIMX = 7
DIMY = 7

External_State_Structure = []
# Parse grid file
f = open("grid.txt",'r')
i = 0
for line in f:
	i+=1
	l = line.split()
	DIMX = len(l)
	External_State_Structure.append(l)
DIMY = i

def reward(state):
	reward = 0

	spot = External_State_Structure[state[1]][state[0]]
	if spot == '2':
		reward = -100
	elif spot == '1':
		reward = 0
	else:
		reward = -1
	return reward

def isTerminal(state, time):
	r = state[1]
	c = state[0]

	spot = External_State_Structure[state[1]][state[0]]
	if spot == '2' or spot == '1':
		return True

	if time > 100:
		return True

class Agent:


	def __init__(self, learnMeth = "SARSA"):
		# Misc
		self.weights = [random.random() for i in range(4)]
		self.features = [0 for i in range(4)]
		# features = [X-coord, Y-coord, Dist_to_target]
		self.time = 0
		self.W = 0
		self.L = 0
		self.epsilon = .3
		self.alpha = 0.05
		self.gamma = 0.9
		self.learnMethod = learnMeth

		# Initialize Q Values to 0
# 		self.qValues = []
# 		for i in range(DIMY):
# 			q = []
# 			for j in range(DIMX):
# 				q.append([0,0,0,0])
# 			self.qValues.append(q)

		# Go to starting state
		self.state = []
		self.prevState = None
		self.nextAction = None
		self.prevQ = 0
		self.s0()

	def s0(self):
		self.state = [0,0]
		self.time = 0
		self.nextAction = self.chooseAction()
		self.features[0] = self.state[0]
		self.features[1] = self.state[1]
		self.features [2] = self.distToTarget(self.state[0], self.state[1])
		self.features[3] = self.nextAction

	def step(self):
		self.time += 1
		self.prevState = copy.copy(self.state)
		action = copy.copy(self.nextAction)
		self.prevQ = self.getQ(self.prevState, action)
		

		# Update Domain and Agent State
		if action == 1: #UP
			self.state[1] = self.prevState[1] - 1
		elif action == 2: #DOWN
			self.state[1] = self.prevState[1] + 1
		elif action == 3: #LEFT
			self.state[0] = self.prevState[0] - 1
		elif action == 4: #RIGHT
			self.state[0] = self.prevState[0] + 1

		r = reward(self.state)
		self.nextAction = self.chooseAction()

		# Update the features vector:
		self.features[0] = self.state[0]
		self.features[1] = self.state[1]
		self.features [2] = self.distToTarget(self.state[0], self.state[1])
		self.features[3] = self.nextAction 
		# Learning Methods
		if self.learnMethod == "SARSA":
			# SARSA
			self.learnSARSA(self.prevQ, r, self.state, self.nextAction)

		elif self.learnMethod == "Q":
			quit()
			# Q-Learning
			# Tabular method:
# 			maxQ = self.maxQ(self.state)
# 			self.learnQ(self.prevState, action, r, maxQ)

		# Check if the state is terminal
		if isTerminal(self.state, self.time):
			spot = External_State_Structure[self.state[1]][self.state[0]]
			if spot == '1':
				self.W += 1
			else:
				self.L += 1
			self.s0()

	def learnSARSA(self, prevQ, reward, state, nextAction):
		# self.qValues[prevState[1]][prevState[0]][prevAction-1] += self.alpha*(reward+self.gamma*self.getQ(state,nextAction)-self.getQ(prevState,prevAction))
		delta = reward + self.gamma*(self.getQ(state, nextAction)) - prevQ
		for i in range(len(self.weights)):
			self.weights[i] += self.alpha*delta*self.features[i]

# 	def learnQ(self, prevState, prevAction, reward, maxQ):
# 		self.qValues[prevState[1]][prevState[0]][prevAction-1] += self.alpha*(reward+self.gamma*maxQ-self.getQ(prevState,prevAction))

	def getQ(self, state, action):
# 		return self.qValues[state[1]][state[0]][action-1]
		return numpy.dot(self.weights, [state[0],state[1],self.distToTarget(state[0],state[1]),action])
		
# 	def maxQ(self, state):
# 		return max([self.getQ(state, a) for a in self.possibleActions()])

	def possibleActions(self):
		# 1 == UP
		# 2 == DOWN
		# 3 == LEFT
		# 4 == RIGHT

		actions = []
		if not(self.state[1] == 0):
			actions.append(1) # UP
		if not(self.state[1] == DIMY-1):
			actions.append(2) # DOWN
		if not(self.state[0] == 0):
			actions.append(3) # LEFT
		if not(self.state[0] == DIMX-1):
			actions.append(4) # RIGHT
		return actions

	def chooseAction(self):
		action = 0 
		pa = self.possibleActions()
		if random.random() < self.epsilon:
			a = random.choice(pa)
		else:
			q = [self.getQ(self.state, a) for a in pa]
			maxQ = max(q)
			count = q.count(maxQ)
			if count > 1:
				best = [i for i in range(len(pa)) if q[i] == maxQ]
				i = random.choice(best)
			else:
				i = q.index(maxQ)
			a = pa[i]
		return a

	def distToTarget(self , ax, ay):
		target = [0,0]
		for y in range(DIMY):
			for x in range(DIMX):
				if External_State_Structure[y][x] == "1":
					target = [x,y]
		return math.hypot(ax-x, ay-y)

	def printqValues(self):
		for row in range(len(self.qValues)):
			print self.qValues[row]
		
	def printWeightValues(self):
		for i in range(len(self.weights)):
			print "W" + str(i) + ":  " + str(self.weights[i])

	def clearWins(self):
		self.W = 0
		self.L = 0

	def setEpison(self, ep):
		self.epsilon = ep



MAX_STEPS = 10000
DISP_STEPS = MAX_STEPS/10
# a = Agent("Q")
# Epsilon = 0.3
# print "Q-Learning:"
# for timestep in range(MAX_STEPS):
# 	a.step()
# 	if timestep%DISP_STEPS == 0:
# 		Epsilon = Epsilon/2
# 		a.setEpison(Epsilon)
# 		print "Timestep: " + str(timestep)
# 		print "W: " + str(a.W) + "    L: " + str(a.L)
# 		a.clearWins()

# print "Timestep: " + str(timestep)
# print "W: " + str(a.W) + "    L: " + str(a.L)
# print a.printqValues()
# print "\n"

a = Agent("SARSA")
Epsilon = 0.3
print "SARSA:"
for timestep in range(MAX_STEPS):
	a.step()
	if timestep%DISP_STEPS == 0:
		Epsilon = Epsilon/2
		a.setEpison(Epsilon)
		print "Timestep: " + str(timestep)
		print "W: " + str(a.W) + "    L: " + str(a.L)
		a.clearWins()

print "Timestep: " + str(timestep)
print "W: " + str(a.W) + "    L: " + str(a.L)
print a.printWeightValues()



# MAX_STEPS = 10
# a = Agent()

# def getAction(action):
# 	if action == 1:
# 		return "UP"
# 	if action == 2:
# 		return "DOWN"
# 	if action == 3:
# 		return "LEFT"
# 	if action == 4:
# 		return "RIGHT"
# 	if action == None:
# 		return "NONE"

# print "Position: " + str(a.state)
# print "Next Action: " + getAction(a.nextAction)
# print "Q Values: "
# print a.printqValues()
# print ""

# for timestep in range(MAX_STEPS):
# 	a.step()
# 	print "Position: " + str(a.state)
# 	print "Next Action: " + getAction(a.nextAction)
# 	print "Q Values: "
# 	print a.printqValues()
# 	print ""