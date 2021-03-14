import matplotlib.pyplot as plt
import math

def crtanje_putanje(v0,theta,y0):
    theta = (theta/360)*2*math.pi
    vx0 = v0 * math.cos(theta)
    vy0 = v0 * math.sin(theta)
    vy = vy0
    x_list = []
    y_list = []
    dt = 0.01
    x = 0
    y = y0
    a = 9.81
    t_ = 0
    x_list.append(x)
    y_list.append(y)
    while True:
        t_ = t_ + dt
        x = x + vx0*dt
        vy = vy - a*dt
        y = y + vy*dt
        if y <= 0:
            break
        x_list.append(x)
        y_list.append(y)
    plt.plot(x_list,y_list)
    plt.show()

def maksimalna_visina(v0,theta,y0):
    theta = (theta/360)*2*math.pi
    vy0 = v0 * math.sin(theta)
    vy = vy0
    dt = 0.01
    y = y0
    a = 9.81
    while True:
        vy = vy - a*dt
        if vy < 0:
            break
        y = y + vy*dt
    return y

def domet(v0,theta,y0):
    theta = (theta/360)*2*math.pi
    vx0 = v0 * math.cos(theta)
    vy0 = v0 * math.sin(theta)
    vy = vy0
    dt = 0.01
    x = 0
    y = y0
    a = 9.81
    while True:
        x = x + vx0*dt
        vy = vy - a*dt
        y = y + vy*dt
        if y <= 0:
            break
    return x

def maksimalna_brzina(v0,theta,y0):
    theta = (theta/360)*2*math.pi
    vx0 = v0 * math.cos(theta)
    vy0 = v0 * math.sin(theta)
    vy = vy0
    dt = 0.01
    x = 0
    y = y0
    a = 9.81
    while True:
        x = x + vx0*dt
        vy = vy - a*dt
        y = y + vy*dt
        if y <= 0:
            break
    vmax = math.sqrt(vx0**2 + vy**2)
    return vmax

def gadanje_mete(v0,theta,y0,xm,ym,rm):
    theta = (theta/360)*2*math.pi
    vx0 = v0 * math.cos(theta)
    vy0 = v0 * math.sin(theta)
    vy = vy0
    x_list = []
    y_list = []
    dmin = math.sqrt(xm**2 + (ym-y0)**2)
    dt = 0.01
    x = 0
    y = y0
    a = 9.81
    x_list.append(x)
    y_list.append(y)
    i = False
    while True:
        x = x + vx0*dt
        vy = vy - a*dt
        y = y + vy*dt
        if y <= 0:
            break
        x_list.append(x)
        y_list.append(y)
        d = math.sqrt((xm-x)**2+(ym-y)**2)
        if d <= rm:
            i = True
            break
        else:
            if d - rm < dmin:
                dmin = d - rm
    if i:
        print("Meta je pogodena!")
    else:
        print("Meta nije pogodena!")
        print("Najmanja udaljenost od mete je: {} m".format(dmin))
    
    xaxis = []
    yaxis = []

    for phi in range (1,3600):
        X = xm + rm*math.cos(phi/10)
        Y = ym + rm*math.sin(phi/10)
        xaxis.append(X)
        yaxis.append(Y)

    plt.plot(xaxis,yaxis)
    plt.plot(x_list,y_list)
    plt.show()

