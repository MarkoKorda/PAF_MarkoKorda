import Particle as prt
import matplotlib.pyplot as plt
import numpy as np

au = 1.486 * pow(10,11)
vzx = 29783
ms = 1.989 * pow(10,30)
mz = 5.9742 * pow(10,24)

rs = np.array([0,0,0])
rz = np.array([0, - au,0])
vs = np.array([0,0,0])
vz = np.array([vzx,0,0])

sunce = prt.Particle(ms,rs,vs)
zemlja = prt.Particle(mz,rz,vz)

T = 3 * 365 * 24 * 60 * 60
dt = 3600

sunce.run_event(zemlja, T, dt)

xlist1, ylist1, xlist2, ylist2 = sunce.get_lists(zemlja)

fig = plt.figure()
ax = plt.axes()
ax.plot(xlist1, ylist1, c="orange", label="Sun", linewidth=3)
ax.plot(xlist2, ylist2, c="green", label="Earth")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_aspect('equal')
plt.legend()
plt.show()