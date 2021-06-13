import universe
import numpy as np
import matplotlib.pyplot as plt 

au = 1.486e11
minute = 60
hour = 60 * minute
day = 24 * hour
year = 365.242 * day

sun = universe.Planet("Sun","yellow",1.989e30, np.array([0,0]), np.array([0,0]))
mercury = universe.Planet("Mercury","orange",3.3e24, np.array([0,0.466*au]), np.array([-47362,0]))
venus = universe.Planet("Venus","red",4.8685e24, np.array([0.723*au,0]), np.array([0,35020]))
earth = universe.Planet("Earth","green",5.9742e24, np.array([-au,0]), np.array([0,-29783]))
mars = universe.Planet("Mars","brown",6.417e23, np.array([0,-1.666*au]), np.array([24007,0]))

solar_system = universe.Universe()
solar_system.add_object(sun)
solar_system.add_object(mercury)
solar_system.add_object(venus)
solar_system.add_object(earth)
solar_system.add_object(mars)

solar_system.evolve(5 * year, hour)

fig = plt.figure(figsize = (8,8))

plt.plot(sun.xlist, sun.ylist, label = sun.name, color = sun.color, linewidth = 5)

plt.plot(mercury.xlist, mercury.ylist, label = mercury.name, color = mercury.color)
plt.plot(mercury.xlist[-1], mercury.ylist[-1], "o", color = mercury.color)

plt.plot(venus.xlist, venus.ylist, label = venus.name, color = venus.color)
plt.plot(venus.xlist[-1], venus.ylist[-1], "o", color = venus.color)

plt.plot(earth.xlist, earth.ylist, label = earth.name, color = earth.color)
plt.plot(earth.xlist[-1], earth.ylist[-1], "o", color = earth.color)

plt.plot(mars.xlist, mars.ylist, label = mars.name, color = mars.color)
plt.plot(mars.xlist[-1], mars.ylist[-1], "o", color = mars.color)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Solar System")
plt.legend(loc="upper right")
plt.show()