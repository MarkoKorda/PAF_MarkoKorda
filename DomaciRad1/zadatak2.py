import particle as prt
import matplotlib.pyplot as plt
from math import pi

p = prt.Particle(50,0,30,70)
xlist = []
ylist1 = []
ylist2 = []

for angle in range(-90,90,1):
    xlist.append(angle)
    angle = (angle/180)*pi
    p.theta = angle
    p.return_to_start()
    range_ = p.range_(0.01)
    time = p.total_time(0.01)
    ylist1.append(range_)
    ylist2.append(time)

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(xlist, ylist1)
ax1.set(xlabel='angle [°]', ylabel='range [m]')
ax2.plot(xlist, ylist2)
ax2.set(xlabel='angle [°]', ylabel='total time [s]')
plt.show()
