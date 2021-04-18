import matplotlib.pyplot as plt
from math import sin,cos,sqrt,pi

class HarmonicOscillator:
    def __init__(self,k,m,x0,v0):
        self.k = k
        self.m = m
        self.x = x0
        self.v = v0
        self.a = -(k/m)*x0

    def __move(self,dt):
        self.a = -(self.k/self.m)*self.x
        self.v = self.v + self.a*dt
        self.x = self.x + self.v*dt

    def show_graphs(self,T,dt):
        t = 0
        xlist = []
        vlist = []
        alist = []
        tlist = []
        while t < T:
            xlist.append(self.x)
            vlist.append(self.v)
            alist.append(self.a)
            tlist.append(t)
            self.__move(dt)
            t += dt
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
        ax1.plot(tlist, xlist)
        ax1.set(xlabel='t [s]', ylabel='x [m]')
        ax2.plot(tlist, vlist)
        ax2.set(xlabel='t [s]', ylabel='v [ms^-1]')
        ax3.plot(tlist, alist)
        ax3.set(xlabel='t [s]', ylabel='a [ms^-2]')
        plt.show()

    def num_error(self,T,dt):
        self.v = 0
        A = self.x
        t = 0
        xlist1 = []
        vlist1 = []
        alist1 = []
        tlist1 = []
        xlist2 = []
        vlist2 = []
        alist2 = []
        tlist2 = []
        omega = sqrt(self.k/self.m)
        while t < T:
            x = A*cos(omega*t)
            xlist2.append(x)
            v = - A*omega*sin(omega*t)
            vlist2.append(v)
            a = - A*(omega**2)*cos(omega*t)
            alist2.append(a)
            tlist2.append(t)
            xlist1.append(self.x)
            vlist1.append(self.v)
            alist1.append(self.a)
            tlist1.append(t)
            self.__move(dt)
            t += dt
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
        ax1.plot(tlist1, xlist1, ".")
        ax1.plot(tlist2,xlist2)
        ax1.set(xlabel='t [s]', ylabel='x [m]')
        ax2.plot(tlist1, vlist1, ".")
        ax2.plot(tlist2,vlist2)
        ax2.set(xlabel='t [s]', ylabel='v [ms^-1]')
        ax3.plot(tlist1, alist1, ".")
        ax3.plot(tlist2, alist2)
        ax3.set(xlabel='t [s]', ylabel='a [ms^-2]')
        plt.show()

    def period_num(self,dt):
        x0 = self.x
        self.__move(dt)
        T = dt
        if self.x > x0:
            j = 1
        else:
            j = 2
        while True:
            x1 = self.x
            self.__move(dt)
            T += dt
            x2 = self.x
            if j == 1:
                if (x2 > x0) and (x1 < x0):
                    break
            else:
                if (x2 < x0) and (x1 > x0):
                    break
        return T

    def period_analitic(self):
        T = 2*pi*sqrt(self.m/self.k)
        return T
