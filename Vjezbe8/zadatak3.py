import Projectile as prt
import matplotlib.pyplot as plt

Cd_list = []

for i in range(1000):
    Cd = i * 0.001
    Cd_list.append(Cd)

m_list = []

for i in range(1000):
    m = 0.005 * (i+1)
    m_list.append(m)

range_list1 = []
range_list2 = []

p1 = prt.Projectile(50,45,0,0,0.1,1.22,0.1,0.01)

for element in Cd_list:
    p1.Cd = element
    r = p1.range_with_ar(0.01)
    range_list1.append(r)
    p1.return_to_start()

plt.plot(Cd_list,range_list1)
plt.xlabel("Cd")
plt.ylabel("range [m]")
plt.show()

p1.Cd = 0.1

for element in m_list:
    p1.m = element
    r = p1.range_with_ar(0.01)
    range_list2.append(r)
    p1.return_to_start()

plt.plot(m_list,range_list2)
plt.xlabel("m [kg]")
plt.ylabel("range [m]")
plt.show()