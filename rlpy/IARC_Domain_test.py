from IARC_Domain import IARC_simulator
sim = IARC_simulator()

sim.s0()

s0 = sim.s0()
print s0[0]

i = 0
while i < 250:
    reward = sim.step(-1)[0]
    print "-----------------"
    print "Roomba xy:"
    print str(sim.roombas[0].x) + "," + str(sim.roombas[0].y)
    print "Roomba direciton:"
    print sim.roombas[0].get_vel()[1]
    print "Time:"+str(sim.time)
    print "Step "+ str(i) +" Reward: " + str(reward)
    i += 1
