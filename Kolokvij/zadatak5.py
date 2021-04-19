import VertikalniHitac as vert
import matplotlib.pyplot as plt

dt  = 0.01
k = 1.5
vh1 = vert.VertikalniHitac(10,10)

maxy = vh1.max_height(dt)
vh1.return_to_start()
maxyar = vh1.max_height_with_ar(dt,k)
vh1.return_to_start()

t = vh1.duration(dt)
vh1.return_to_start()
tar = vh1.duration_with_ar(dt,k)
vh1.return_to_start()

ylist1, vlist1, tlist1 = vh1.run_event(dt)
vh1.return_to_start()

ylist2, vlist2, tlist2 = vh1.run_event_with_ar(dt,k)
vh1.return_to_start()

print("Max visina bez otpora zraka je: {} m \nMax visina sa otporom zraka je: {} m".format(maxy,maxyar))
print("Vrijeme trajanja hitca bez otpora zraka je: {} s\nVrijeme trajanja hitca sa otporom zraka je: {} s".format(t,tar))

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(tlist1, ylist1)
ax1.set(xlabel='t [s]', ylabel='y [m]')
ax2.plot(tlist1, vlist1)
ax2.set(xlabel='t [s]', ylabel='v [ms^-1]')
plt.title("Bez otpora zraka")
plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(tlist2, ylist2)
ax1.set(xlabel='t [s]', ylabel='y [m]')
ax2.plot(tlist2, vlist2)
ax2.set(xlabel='t [s]', ylabel='v [ms^-1]')
plt.title("Sa otporom zraka")
plt.show()