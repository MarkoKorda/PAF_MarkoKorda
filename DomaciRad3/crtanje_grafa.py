import matplotlib.pyplot as plt

f1 = open("x.txt", "r")
xstring = f1.read()
f1.close()

f2 = open("v.txt", "r")
vstring = f2.read()
f2.close()

f3 = open("a.txt", "r")
astring = f3.read()
f3.close()

f4 = open("t.txt", "r")
tstring = f4.read()
f4.close()

xlist_ = xstring.split(",")
vlist_ = vstring.split(",")
alist_ = astring.split(",")
tlist_ = tstring.split(",")

xlist = []
vlist = []
alist = []
tlist = []

for element in xlist_:
    xlist.append(float(element))

for element in vlist_:
    vlist.append(float(element))

for element in alist_:
    alist.append(float(element))

for element in tlist_:
    tlist.append(float(element))

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.plot(tlist, xlist)
ax1.set(xlabel='t [s]', ylabel='x [m]')
ax2.plot(tlist, vlist)
ax2.set(xlabel='t [s]', ylabel='v [ms^-1]')
ax3.plot(tlist, alist)
ax3.set(xlabel='t [s]', ylabel='a [ms^-2]')
plt.show()