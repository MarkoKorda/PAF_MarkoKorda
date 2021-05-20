import matplotlib.pyplot as plt

class BungeeJumper:
    def __init__(self,y0,l0,k,m,rho = 1,Cd = 1,A = 1,AirResistance = False):
        self.y0 = y0
        self.l0 = l0
        self.k = k
        self.m = m
        self.rho = rho
        self.Cd = Cd
        self.A = A
        self.AirResistance = AirResistance
        self.y = y0
        self.v = 0
        self.t = 0
        self.ylist = []
        self.tlist = []
        self.ylist.append(self.y)
        self.tlist.append(self.t)
        self.Ep = m * 9.81 * self.y
        self.Ek = 0
        self.Ee = 0
        self.E = self.Ep + self.Ek + self.Ee
        self.Ep_list = []
        self.Ek_list = []
        self.Ee_list = []
        self.E_list = []
        self.Ep_list.append(self.Ep)
        self.Ek_list.append(self.Ek)
        self.Ee_list.append(self.Ee)
        self.E_list.append(self.E)

    def reset(self):
        del self.y0
        del self.l0
        del self.k
        del self.m
        del self.rho
        del self.Cd
        del self.A
        del self.AirResistance
        del self.y
        del self.v
        del self.t
        del self.ylist
        del self.tlist
        del self.Ep
        del self.Ek
        del self.Ee
        del self.E
        del self.Ep_list
        del self.Ek_list
        del self.Ee_list
        del self.E_list

    def return_to_start(self):
        y0 = self.y0
        l0 = self.l0
        k = self.k
        m = self.m
        rho = self.rho
        Cd = self.Cd
        A = self.A
        AirResistance = self.AirResistance
        self.reset()
        self.y0 = y0
        self.l0 = l0
        self.k = k
        self.m = m
        self.rho = rho
        self.Cd = Cd
        self.A = A
        self.AirResistance = AirResistance
        self.y = y0
        self.v = 0
        self.t = 0
        self.ylist = []
        self.tlist = []
        self.ylist.append(self.y)
        self.tlist.append(self.t)
        self.Ep = m * 9.81 * self.y
        self.Ek = 0
        self.Ee = 0
        self.E = self.Ep + self.Ek + self.Ee
        self.Ep_list = []
        self.Ek_list = []
        self.Ee_list = []
        self.E_list = []
        self.Ep_list.append(self.Ep)
        self.Ek_list.append(self.Ek)
        self.Ee_list.append(self.Ee)
        self.E_list.append(self.E)

    def elastic_force(self):
        d = self.y0 - self.y - self.l0
        if d > 0:
            F = self.k * d
        else:
            F = 0
        return F

    def air_resistance(self):
        F = - abs(self.v) * self.v * self.rho * self.Cd * self.A * 0.5
        return F

    def elastic_energy(self):
        d = self.y0 - self.y - self.l0
        if d > 0:
            E = 0.5 * self.k * d * d
        else:
            E = 0
        return E

    def __move(self,dt):
        a = -9.81 + self.elastic_force()/self.m
        self.v = self.v + a * dt
        self.y = self.y + self.v * dt
        self.t = self.t + dt
        self.Ep = self.m * 9.81 * self.y
        self.Ek = 0.5 * self.m * self.v * self.v
        self.Ee = self.elastic_energy()
        self.E = self.Ep + self.Ek + self.Ee
        self.ylist.append(self.y)
        self.tlist.append(self.t)
        self.Ep_list.append(self.Ep)
        self.Ek_list.append(self.Ek)
        self.Ee_list.append(self.Ee)
        self.E_list.append(self.E)

    def __move_with_ar(self,dt):
        a = -9.81 + (self.elastic_force() + self.air_resistance())/self.m
        self.v = self.v + a * dt
        self.y = self.y + self.v * dt
        self.t = self.t + dt
        self.Ep = self.m * 9.81 * self.y
        self.Ek = 0.5 * self.m * self.v * self.v
        self.Ee = self.elastic_energy()
        self.E = self.Ep + self.Ek + self.Ee
        self.ylist.append(self.y)
        self.tlist.append(self.t)
        self.Ep_list.append(self.Ep)
        self.Ek_list.append(self.Ek)
        self.Ee_list.append(self.Ee)
        self.E_list.append(self.E)

    def run_event(self,T,dt):
        if self.AirResistance:
            while self.t < T:
                self.__move_with_ar(dt)
        else:
            while self.t < T:
                self.__move(dt)


