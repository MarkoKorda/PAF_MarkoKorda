import matplotlib.pyplot as plt 

class Particle:
    def __init__(self,m,x0,v0,func):
        self.F = func
        self.m = m
        self.x = x0
        self.v = v0
        self.t = 0
        self.a = self.F(self.x,self.v,self.t)/self.m
        self.xlist = []
        self.vlist = []
        self.alist = []
        self.tlist = []
        self.xlist.append(self.x)
        self.vlist.append(self.v)
        self.alist.append(self.a)
        self.tlist.append(self.t)

    def __move(self,dt):
        self.a = self.F(self.x,self.v,self.t)/self.m
        self.v = self.v + self.a*dt
        self.x = self.x + self.v*dt
        self.t = self.t + dt
        self.xlist.append(self.x)
        self.vlist.append(self.v)
        self.alist.append(self.a)
        self.tlist.append(self.t)
        
    def reset(self):
        del self.F
        del self.m
        del self.x
        del self.v
        del self.t
        del self.a
        del self.xlist
        del self.vlist
        del self.alist
        del self.tlist

    def return_to_start(self):
        self.x = self.xlist[0]
        self.v = self.vlist[0]
        self.t = 0
        self.a = self.F(self.x,self.v,self.t)/self.m
        self.xlist = []
        self.vlist = []
        self.alist = []
        self.tlist = []
        self.xlist.append(self.x)
        self.vlist.append(self.v)
        self.alist.append(self.a)
        self.tlist.append(self.t)
        
    def move_particle(self,dt,T):
        while self.t < T:
            self.__move(dt)

    def plot_all(self):
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
        ax1.plot(self.tlist, self.xlist)
        ax1.set(xlabel='t [s]', ylabel='x [m]')
        ax2.plot(self.tlist, self.vlist)
        ax2.set(xlabel='t [s]', ylabel='v [ms^-1]')
        ax3.plot(self.tlist, self.alist)
        ax3.set(xlabel='t [s]', ylabel='a [ms^-2]')
        plt.show()