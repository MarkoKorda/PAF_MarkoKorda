from math import pi,sin,cos
import matplotlib.pyplot as plt

class Particle:
    def __init__(self,v0,theta,x0,y0):
        self.v0 = v0
        theta = (theta/180)*pi
        self.theta = theta
        self.x = x0
        self.y = y0
        self.xlist = []
        self.xlist.append(x0)
        self.ylist = []
        self.ylist.append(y0)
        self.vx = v0*cos(self.theta)
        self.vy = v0*sin(self.theta)

    def reset(self):
        del self.v0
        del self.theta
        del self.x
        del self.y
        del self.xlist
        del self.ylist
        del self.vx
        del self.vy

    def __move(self,dt):
        self.vy = self.vy - 9.81*dt
        self.x = self.x + self.vx * dt
        self.xlist.append(self.x)
        self.y = self.y + self.vy * dt
        self.ylist.append(self.y)

    def range(self):
        x0 = self.x
        dt = 0.01
        while True:
            self.__move(dt)
            if self.y <= 0:
                break
        d = abs(self.x - x0)
        return d

    def plot_trajectory(self):
        plt.plot(self.xlist,self.ylist)
        plt.show()

    




