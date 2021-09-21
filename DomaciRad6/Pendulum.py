import math

class Pendulum:
    def __init__(self,theta0,l,m,dt):
        self.theta = theta0
        self.omega = 0
        self.alpha = 0
        self.t = 0
        self.dt = dt
        self.l = l
        self.m = m
        self.theta_list = []
        self.t_list = []
        self.theta_list.append(self.theta)
        self.t_list.append(self.t)
        self.__is_small_angle()

    def __is_small_angle(self):
        if self.theta * (180 / math.pi) < 10:
            print("Kut otklona je mal!")
        else:
            print("Kut otklona nije mal!")

    def change_angle(self,deg_or_rad,theta):
        if deg_or_rad == "deg":
            self.theta += theta * (math.pi/180)
        elif deg_or_rad == "rad":
            self.theta += theta
        else:
            print("Krivi unos!")
    
    def __move(self):
        self.alpha = - (9.81 * math.sin(self.theta))/self.l
        self.omega = self.omega + self.alpha * self.dt
        self.theta = self.theta + self.omega * self.dt
        self.t = self.t + self.dt
        self.theta_list.append(self.theta)
        self.t_list.append(self.t)

    def oscillate(self,t):
        while self.t < t:
            self.__move()

    def __move_ar(self,k):
        self.alpha = - ((self.omega * abs(self.omega) * self.l * self.l)*(k/self.m) + 9.81 * math.sin(self.theta))/self.l
        self.omega = self.omega + self.alpha * self.dt
        self.theta = self.theta + self.omega * self.dt
        self.t = self.t + self.dt
        self.theta_list.append(self.theta)
        self.t_list.append(self.t)

    def oscillate_ar(self,t,k):
        while self.t < t:
            self.__move_ar(k)

    def calculate_period(self):
        i = 0
        while i < 1:
            old_omega = self.omega
            self.__move()
            if (self.omega == 0) or (old_omega * self.omega < 0):
                i += 1
        return self.t