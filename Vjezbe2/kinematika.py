import matplotlib.pyplot as plt
import math

def jednoliko_gibanje(F,m,t):
    x_list = []
    v_list = []
    a_list = []
    t_list = []

    x = 0
    v = 0
    a = F/m
    t0 = 0
    t_ = t0

    x_list.append(x)
    v_list.append(v)
    a_list.append(a)
    t_list.append(t_)

    n = 100
    dt = t/n

    for i in range(n):
        t_ = t_ + dt
        v = v + a*dt
        x = x + v*dt
        x_list.append(x)
        v_list.append(v)
        a_list.append(a)
        t_list.append(t_)

    fig, axs = plt.subplots(2, 2)
    axs[0, 0].plot(t_list, x_list)
    axs[0, 0].set_title("x-t graf")
    axs[0, 1].plot(t_list, v_list)
    axs[0, 1].set_title('v-t graf')
    axs[1, 0].plot(t_list, a_list,)
    axs[1, 0].set_title('a-t graf')
    plt.show()

def kosi_hitac(v0,theta,t):
    theta = (theta/360)*2*math.pi
    vx0 = v0 * math.cos(theta)
    vy0 = v0 * math.sin(theta)
    vy = vy0
    x_list = []
    y_list = []
    t_list = []
    n = 100
    dt = t/n
    x = 0
    y = 0
    a = 9.81
    t_ = 0
    x_list.append(x)
    y_list.append(y)
    t_list.append(t_)

    for i in range(n):
        t_ = t_ + dt
        x = x + vx0*dt
        vy = vy - a*dt
        y = y + vy*dt
        x_list.append(x)
        y_list.append(y)
        t_list.append(t_)

    fig, axs = plt.subplots(2, 2)
    axs[0, 0].plot(x_list, y_list)
    axs[0, 0].set_title("x-y graf")
    axs[0, 1].plot(t_list, x_list)
    axs[0, 1].set_title('x-t graf')
    axs[1, 0].plot(t_list, y_list,)
    axs[1, 0].set_title('y-t graf')
    plt.show()
