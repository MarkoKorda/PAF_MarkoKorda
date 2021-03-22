import particle as prt
import matplotlib.pyplot as plt

def log_scale_ne():
    dtlist = []
    dtmax = 1
    dtlist.append(dtmax)
    n = 100

    for i in range(n):
        dt_ = dtlist[i]/1.1
        dtlist.append(dt_)

    re_list = []

    p = prt.Particle(10,60,40,30)

    for i in range(n+1):
        p.reset()
        p = prt.Particle(10,60,40,30)
        dt = dtlist[i]
        re = (abs((p.range(dt)-p.range_analitic())/p.range_analitic()))*100
        re_list.append(re)

    plt.xlabel("dt [s]")
    plt.ylabel("relative error [%]")
    plt.xscale("log")
    plt.plot(dtlist,re_list)
    plt.show()
    p.reset()

def lin_scale_ne():
    dtlist = []
    dtmin = 0.01
    dtlist.append(dtmin)
    n = 100

    for i in range(n):
        dt_ = dtlist[i] + 0.01
        dtlist.append(dt_)

    re_list = []

    p = prt.Particle(10,60,40,30)

    for i in range(n+1):
        p.reset()
        p = prt.Particle(10,60,40,30)
        dt = dtlist[i]
        re = (abs((p.range(dt)-p.range_analitic())/p.range_analitic()))*100
        re_list.append(re)

    plt.xlabel("dt [s]")
    plt.ylabel("relative error [%]")
    plt.plot(dtlist,re_list)
    plt.show()
    p.reset()

log_scale_ne()
lin_scale_ne()