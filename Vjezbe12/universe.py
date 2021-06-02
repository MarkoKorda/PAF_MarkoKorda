import numpy as np
from math import sqrt 

G = 6.67408 * pow(10,-11)

class Universe:
    def __init__(self):
        self.list_of_objects = []

    def add_object(self,obj):
        self.list_of_objects.append(obj)

    def __move(self,dt):
        n = len(self.list_of_objects)
        for i in range(n):
            a = np.array([0,0])
            for j in range(n):
                if i != j:
                    a = a + self.list_of_objects[i].gravitational_force_acc(self.list_of_objects[j])
            self.list_of_objects[i].a = a
        for planet in self.list_of_objects:
            planet.v = planet.v + planet.a * dt
            planet.r = planet.r + planet.v * dt
            planet.xlist.append(planet.r[0])
            planet.ylist.append(planet.r[1])

    def evolve(self,T,dt):
        t = 0
        while t < T:
            self.__move(dt)
            t = t + dt

class Planet:
    def __init__(self,m,r0,v0):
        self.m = m
        self.r0 = r0
        self.v0 = v0
        self.a0 = np.array([0,0])
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
        x = x1 - x2
        y = y1 - y2
        d = sqrt(pow(x,2) + pow(y,2))
        return d

    def gravitational_force_acc(self,other):
        distance = self.__distance(other)
        r12 = (self.r - other.r) * (1 / distance)
        a = - ((G * other.m)/(pow(distance,2))) * r12
        return a
