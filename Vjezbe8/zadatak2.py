import Projectile as pct
import matplotlib.pyplot as plt

pct1 = pct.Projectile(10,45,0,0,0.1,1.22,0.1,0.05)

pct1.run_event_with_ar(0.01)

xlist1 = pct1.xlist
ylist1 = pct1.ylist

pct1.return_to_start()

pct1.run_event_with_ar_RK(0.01)

xlist2 = pct1.xlist
ylist2 = pct1.ylist

plt.plot(xlist1,ylist1,label = "Eulerova metoda")
plt.plot(xlist2,ylist2,label = "RK metoda")
plt.legend()
plt.show()