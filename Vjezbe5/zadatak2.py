import harmonic_oscillator as ho
import matplotlib.pyplot as plt

ho1 = ho.HarmonicOscillator(18,8,3,7)
ho1_period = ho1.period_num(0.001)
print("Period je {} sekundi".format(ho1_period))
ho2 = ho.HarmonicOscillator(7,11,5,-4)

xlist = []
ylist = []
dt = 0.2
k = 1.1
n = 60

for i in range(n):
    num = ho2.period_num(dt)
    analitic = ho2.period_analitic()
    rel_error = (abs(num - analitic)/analitic)*100
    xlist.append(dt)
    ylist.append(rel_error)
    dt = dt/k

plt.plot(xlist,ylist)
plt.xlabel("dt [s]")
plt.ylabel("error [%]")
plt.xscale("log")
plt.show()