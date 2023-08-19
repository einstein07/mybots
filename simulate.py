import pybullet as p
import time

physicsClient = p.connect(p.GUI)
for n in range (1001):
	time.sleep( 1/60 )
	p.stepSimulation()
	print(n)

p.disconnect()
