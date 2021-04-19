import VertikalniHitac as vert
import matplotlib.pyplot as plt 

vh1 = vert.VertikalniHitac(10,10)
dt = 0.01

ylist, vlist, tlist = vh1.run_event(dt)

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(tlist, ylist)
ax1.set(xlabel='t [s]', ylabel='y [m]')
ax2.plot(tlist, vlist)
ax2.set(xlabel='t [s]', ylabel='v [ms^-1]')
plt.show()