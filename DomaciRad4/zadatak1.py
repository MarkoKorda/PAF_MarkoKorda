import Projectile
import matplotlib.pyplot as plt

p1 = Projectile.Projectile(50,45,0,0,0.1,1.22,0.1,0.1,False)

p1.run_event_with_ar(0.01)
xlist1 = p1.xlist
ylist1 = p1.ylist

p1.return_to_start()
p1.isCube = True

p1.run_event_with_ar(0.01)
xlist2 = p1.xlist
ylist2 = p1.ylist

fig, axs = plt.subplots(1, 2)
axs[0].plot(xlist1, ylist1)
axs[1].plot(xlist2, ylist2)
axs[0].title.set_text("sphere")
axs[1].title.set_text("cube")
plt.show()