import numpy as np
from math import sqrt

G = 6.67408 * pow(10,-11)

class Particle:
    def __init__(self,m,r0,v0):
        self.m = m
        self.r0 = r0
        self.v0 = v0
        self.a0 = np.array([0,0,0])
        self.r = r0
        self.v = v0
        self.a = self.a0
        self.xlist = []
        self.ylist = []

    def reset(self):
        del self.m
        del self.r0
        del self.v0
        del self.r
        del self.v
        del self.a
        del self.xlist
        del self.ylist

    def return_to_start(self):
        m = self.m
        r0 = self.r0
        v0 = self.v0
        self.reset()
        self.m = m
        self.r0 = r0
        self.v0 = v0
        self.r = r0
        self.v = v0
        self.a = self.a0
        self.xlist = []
        self.ylist = []

    def __distance(self,other):
        x1 = self.r[0]
        x2 = other.r[0]
        y1 = self.r[1]
        y2 = other.r[1]
        z1 = self.r[2]
        z2 = other.r[2]
        x = x1 - x2
        y = y1 - y2
        z = z1 - z2
        vm = sqrt(pow(x,2) + pow(y,2) + pow(z,2))
        return vm
    
    def __gravitational_force_acc(self,other):
        distance = self.__distance(other)
        r12 = (self.r - other.r) * (1 / distance)
        r21 = (other.r - self.r) * (1 / distance)
        self.a = - ((G * other.m)/(pow(distance,2))) * r12
        other.a = - ((G * self.m)/(pow(distance,2))) * r21
    
    def __move(self,other,dt):
        self.__gravitational_force_acc(other)
        self.v = self.v + self.a * dt
        other.v = other.v + other.a * dt
        self.r = self.r + self.v * dt
        other.r = other.r + other.v * dt
        self.xlist.append(self.r[0])
        self.ylist.append(self.r[1])
        other.xlist.append(other.r[0])
        other.ylist.append(other.r[1])

    def run_event(self,other,T,dt):
        t = 0
        while t < T:
            self.__move(other, dt)
            t = t + dt
    
    def get_lists(self,other):
        return self.xlist, self.ylist, other.xlist, other.ylist