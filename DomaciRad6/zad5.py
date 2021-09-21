import Pendulum as pnd
import math

p1 = pnd.Pendulum(math.pi/20, 0.5, 0.01, 0.001)

T = p1.calculate_period()
print(T)