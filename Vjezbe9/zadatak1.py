import BungeeJumper as Bg
import matplotlib.pyplot as plt

p1 = Bg.BungeeJumper(100,50,500,50)
p1.run_event(50,0.001)
p2 = Bg.BungeeJumper(100,50,500,50,1.22,2,0.1,True)
p2.run_event(50,0.001)

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(p1.tlist, p1.ylist)
axs[0, 1].plot(p1.tlist, p1.Ep_list)
axs[0, 1].plot(p1.tlist, p1.Ek_list)
axs[0, 1].plot(p1.tlist, p1.Ee_list)
axs[0, 1].plot(p1.tlist, p1.E_list)
axs[1, 0].plot(p2.tlist, p2.ylist)
axs[1, 1].plot(p2.tlist, p2.Ep_list)
axs[1, 1].plot(p2.tlist, p2.Ek_list)
axs[1, 1].plot(p2.tlist, p2.Ee_list)
axs[1, 1].plot(p2.tlist, p2.E_list)
plt.show()