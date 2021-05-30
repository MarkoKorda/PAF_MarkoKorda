import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self,E,B,v0,q,m):
        self.E = E
        self.B = B
        self.v0 = v0
        self.q = q
        self.m = m
        self.a = np.array([0,0,0])
        self.v = v0
        self.x = np.array([0,0,0])
        self.xlist = [0]
        self.ylist = [0]
        self.zlist = [0]
    
    def reset(self):
        del self.E
        del self.B
        del self.v0
        del self.q
        del self.m
        del self.a
        del self.v
        del self.x
        del self.xlist
        del self.ylist
        del self.zlist

    def return_to_start(self):
        E = self.E
        B = self.B
        v0 = self.v0
        q = self.q
        m = self.m
        xlist = self.xlist
        self.reset()
        self.E = E
        self.B = B
        self.v0 = v0
        self.q = q
        self.m = m
        self.a = np.array([0,0,0])
        self.v = v0
        self.x = np.array([0,0,0])
        self.xlist = [0]
        self.ylist = [0]
        self.zlist = [0]

    def __electric_force(self):
        Fe = self.q * self.E
        return Fe

    def __magnetic_force(self):
        Fm = self.q * (np.cross(self.v,self.B))
        return Fm

    def __move(self,dt):
        F = self.__electric_force() + self.__magnetic_force()
        self.a = F / self.m
        self.v = self.v + self.a * dt
        self.x = self.x + self.v * dt
        self.xlist.append(self.x[0])
        self.ylist.append(self.x[1])
        self.zlist.append(self.x[2])

    def __move_RK(self,dt):
        v0 = self.v
        x0 = self.x

        F = self.__electric_force() + self.__magnetic_force()
        self.a = F / self.m
        k1v = self.a * dt
        k1x = v0 * dt
        
        self.v = v0 + 0.5 * k1v
        self.x = x0 + 0.5 * k1x
        F = self.__electric_force() + self.__magnetic_force()
        self.a = F / self.m
        k2v = self.a * dt
        k2x = (v0 + 0.5 * k1v) * dt

        self.v = v0 + 0.5 * k2v
        self.x = x0 + 0.5 * k2x
        F = self.__electric_force() + self.__magnetic_force()
        self.a = F / self.m
        k3v = self.a * dt
        k3x = (v0 + 0.5 * k2v) * dt

        self.v = v0 + k3v
        self.x = x0 + k3x
        F = self.__electric_force() + self.__magnetic_force()
        self.a = F / self.m
        k4v = self.a * dt
        k4x = (v0 + k3v) * dt

        self.v = v0 + (1/6)*(k1v + 2 * k2v + 2 * k3v + k4v)
        self.x = x0 + (1/6)*(k1x + 2 * k2x + 2 * k3x + k4x)
        
        self.xlist.append(self.x[0])
        self.ylist.append(self.x[1])
        self.zlist.append(self.x[2])

    def run_event(self,dt,T):
        t = 0
        while t < T:
            self.__move(dt)
            t = t + dt

    def run_event_RK(self,dt,T):
        t = 0
        while t < T:
            self.__move_RK(dt)
            t = t + dt

    def get_lists(self):
        return self.xlist, self.ylist, self.zlist

    