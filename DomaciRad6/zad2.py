import Pendulum as pnd
import math

p1 = pnd.Pendulum(math.pi/20, 0.3, 0.01, 0.01)
p2 = pnd.Pendulum(math.pi/20, 0.3, 0.01, 0.01)

print(p1.theta)
p1.change_angle("deg", 1)
print(p1.theta)

print(p2.theta)
p2.change_angle("rad", math.pi/40)
print(p2.theta)