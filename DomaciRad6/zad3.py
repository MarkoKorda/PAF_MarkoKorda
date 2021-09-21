import Pendulum as pnd
import math
import matplotlib.pyplot as plt

p1 = pnd.Pendulum(math.pi/20, 1, 0.1, 0.01)

p1.oscillate(5)

plt.plot(p1.t_list, p1.theta_list)
plt.show()