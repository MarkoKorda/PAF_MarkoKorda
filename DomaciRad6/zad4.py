import Pendulum as pnd
import math
import matplotlib.pyplot as plt

p1 = pnd.Pendulum(math.pi/20, 1, 0.1, 0.05)
p2 = pnd.Pendulum(math.pi/20, 1, 0.1, 0.05)

p1.oscillate(5)
p2.oscillate_ar(5, 0.1)

plt.plot(p1.t_list, p1.theta_list)
plt.plot(p2.t_list, p2.theta_list)
plt.show()