from IARC_Domain import IARC_simulator
sim = IARC_simulator()

sim.s0()

s0 = sim.s0()
print s0[0]

i = 0
while i < 200:
    reward = sim.step()[0]
    print "Step "+i+" Reward: "+reward
    i += 1
