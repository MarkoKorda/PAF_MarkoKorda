import Particle as prt
import matplotlib.pyplot as plt
import numpy as np

E1 = np.array([0,0,0])
B1 = np.array([0,0,1])
v01 = np.array([0.1,0.1,0.1])
q1 = 1
m1 = 1

E2 = np.array([0,0,0])
B2 = np.array([0,0,1])
v02 = np.array([0.1,0.1,0.1])
q2 = -1
m2 = 1

p1 = prt.Particle(E1,B1,v01,q1,m1)
p1.run_event(0.01,20)
xlist1, ylist1, zlist1 = p1.get_lists()
p1.return_to_start()

p2 = prt.Particle(E2,B2,v02,q2,m2)
p2.run_event(0.01,20)
xlist2, ylist2, zlist2 = p2.get_lists()
p2.return_to_start()

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(xlist1, ylist1, zlist1, c="orange", label="positron")
ax.plot3D(xlist2, ylist2, zlist2, c="blue", label="electron")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.view_init(30,30)
plt.legend()
plt.show()