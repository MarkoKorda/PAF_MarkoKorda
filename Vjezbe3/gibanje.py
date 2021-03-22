import particle as prt

p1 = prt.Particle(50,60,70,120)
print(p1.range(0.01))
p1.plot_trajectory()
p1.reset()