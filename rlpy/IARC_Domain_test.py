from IARC_Domain import IARC_simulator
sim = IARC_simulator()

sim.s0()

s0 = sim.s0()
print s0[0]

i = 0
while i < 400:
    reward = sim.step(-1)[0]
    print "Step "+ str(i) +" Reward: " + str(reward)
    i += 1
