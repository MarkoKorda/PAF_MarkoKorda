import Projectile as prt
import matplotlib.pyplot as plt

p1 = prt.Projectile(50,0,0,0,0.1,1.22,0.1,0.01,True)
p1.angle_to_hit_target_ar(150,0.01,200,50)

p2 = prt.Projectile(50,0,0,0,0.1,1.22,0.1,0.01,False)
p2.angle_to_hit_target_ar(150,0.01,200,50)

plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.show()