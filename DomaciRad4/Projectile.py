from math import pi,sin,cos,sqrt,atan
import matplotlib.pyplot as plt
from random import uniform

class Projectile:
    def __init__(self,v0,theta,x0,y0,m = 1,rho = 1,Cd = 1,A = 1,isCube = False):
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
        self.m = m
        self.rho = rho
        self.Cd = Cd
        self.A = A
        self.vtheta = theta
        self.isCube = isCube

    def reset(self):
        del self.v0
        del self.theta
        del self.x
        del self.y
        del self.xlist
        del self.ylist
        del self.vx
        del self.vy
        del self.m
        del self.rho
        del self.Cd
        del self.A
        del self.vtheta
        del self.isCube

    def return_to_start(self):
        v0 = self.v0
        theta = self.theta
        x0 = self.xlist[0]
        y0 = self.ylist[0]
        m = self.m
        rho = self.rho
        Cd = self.Cd
        A = self.A
        isCube = self.isCube
        self.reset()
        self.v0 = v0
        self.theta = theta
        self.x = x0
        self.y = y0
        self.xlist = []
        self.xlist.append(x0)
        self.ylist = []
        self.ylist.append(y0)
        self.vx = v0*cos(self.theta)
        self.vy = v0*sin(self.theta)
        self.m = m
        self.rho = rho
        self.Cd = Cd
        self.A = A
        self.vtheta = theta
        self.isCube = isCube

    def __move(self,dt):
        self.vy = self.vy - 9.81*dt
        self.x = self.x + self.vx * dt
        self.xlist.append(self.x)
        self.y = self.y + self.vy * dt
        self.ylist.append(self.y)

    def __move_with_ar(self,dt):
        ax = - (abs(self.vx) * self.vx * self.rho * self.Cd * self.A)/(2*self.m)
        self.vx = self.vx + ax * dt
        self.x = self.x + self.vx * dt
        self.xlist.append(self.x)
        ay = - 9.81 - (abs(self.vy) * self.vy * self.rho * self.Cd * self.A)/(2*self.m)
        self.vy = self.vy + ay * dt
        self.y = self.y + self.vy * dt
        self.ylist.append(self.y)

    def __move_with_ar_RK(self,dt):
        ax = - (abs(self.vx) * self.vx * self.rho * self.Cd * self.A)/(2*self.m)
        k1vx = ax * dt
        k1x = self.vx * dt
        ax = - (abs(self.vx + 0.5 * k1vx) * (self.vx + 0.5 * k1vx) * self.rho * self.Cd * self.A)/(2*self.m)
        k2vx = ax * dt
        k2x = (self.vx + 0.5 * k1vx) * dt
        ax = - (abs(self.vx + 0.5 * k2vx) * (self.vx + 0.5 * k2vx) * self.rho * self.Cd * self.A)/(2*self.m)
        k3vx = ax * dt
        k3x = (self.vx + 0.5 * k2vx) * dt
        ax = - (abs(self.vx + k3vx) * (self.vx + k3vx) * self.rho * self.Cd * self.A)/(2*self.m)
        k4vx = ax * dt
        k4x = (self.vx + k3vx) * dt
        self.vx = self.vx + (1/6)*(k1vx + 2 * k2vx + 2 * k3vx + k4vx)
        self.x = self.x + (1/6)*(k1x + 2 * k2x + 2 * k3x + k4x)
        self.xlist.append(self.x)

        ay = - 9.81 - (abs(self.vy) * self.vy * self.rho * self.Cd * self.A)/(2*self.m)
        k1vy = ay * dt
        k1y = self.vy * dt
        ay = - 9.81 - (abs(self.vy + 0.5 * k1vy) * (self.vy + 0.5 * k1vy) * self.rho * self.Cd * self.A)/(2*self.m)
        k2vy = ay * dt
        k2y = (self.vy + 0.5 * k1vy) * dt
        ay = - 9.81 - (abs(self.vy + 0.5 * k2vy) * (self.vy + 0.5 * k2vy) * self.rho * self.Cd * self.A)/(2*self.m)
        k3vy = ay * dt
        k3y = (self.vy + 0.5 * k2vy) * dt
        ay = - 9.81 - (abs(self.vy + k3vy) * (self.vy + k3vy) * self.rho * self.Cd * self.A)/(2*self.m)
        k4vy = ay * dt
        k4y = (self.vy + k3vy) * dt
        self.vy = self.vy + (1/6)*(k1vy + 2 * k2vy + 2 * k3vy + k4vy)
        self.y = self.y + (1/6)*(k1y + 2 * k2y + 2 * k3y + k4y)
        self.ylist.append(self.y)

    def __move_with_ar_cube(self,dt):
        self.vtheta = abs(atan(self.vy / self.vx))
        if atan(self.vy / self.vx) >= 0:
            i = 1
        else:
            i = -1
        A = self.A * (abs(sin(self.vtheta)) + abs(cos(self.vtheta)))
        v = sqrt(self.vx * self.vx + self.vy * self.vy)
        a = (v * v * self.rho * self.Cd * A)/(2*self.m)
        ax = - a * cos(self.vtheta)
        self.vx = self.vx + ax * dt
        self.x = self.x + self.vx * dt
        self.xlist.append(self.x)
        ay = - 9.81 - a * sin(self.vtheta) * i
        self.vy = self.vy + ay * dt
        self.y = self.y + self.vy * dt
        self.ylist.append(self.y)
    
    def run_event(self,dt):
        while True:
            self.__move(dt)
            if self.y <= 0:
                break

    def run_event_with_ar(self,dt):
        if self.isCube:
            while True:
                self.__move_with_ar_cube(dt)
                if self.y <= 0:
                    break
        else:
            while True:
                self.__move_with_ar(dt)
                if self.y <= 0:
                    break

    def run_event_with_ar_RK(self,dt):
        while True:
            self.__move_with_ar_RK(dt)
            if self.y <= 0:
                break
    
    def range_(self,dt):
        x0 = self.x
        while True:
            self.__move(dt)
            if self.y <= 0:
                break
        d = abs(self.x - x0)
        self.return_to_start()
        return d

    def range_with_ar(self,dt):
        x0 = self.x
        while True:
            self.__move_with_ar(dt)
            if self.y <= 0:
                break
        d = abs(self.x - x0)
        self.return_to_start()
        return d

    def range_with_ar_RK(self,dt):
        x0 = self.x
        while True:
            self.__move_with_ar_RK(dt)
            if self.y <= 0:
                break
        d = abs(self.x - x0)
        self.return_to_start()
        return d

    def plot_trajectory(self):
        plt.plot(self.xlist,self.ylist)
        plt.show()

    def range_analitic(self):
        vy0 = self.v0*sin(self.theta)
        y0 = self.ylist[0]
        t1 = (vy0 + sqrt(vy0**2 + 2*9.81*y0))/9.81
        t2 = (vy0 - sqrt(vy0**2 + 2*9.81*y0))/9.81
        if t2 > t1:
            t = t2
        else:
            t = t1
        d = self.v0*cos(self.theta)*t
        return d

    def total_time(self,dt):
        tt = 0
        while True:
            self.__move(dt)
            tt = tt + dt
            if self.y <= 0:
                break
        self.return_to_start()
        return tt

    def max_speed(self,dt):
        vmax = self.v0
        while True:
            self.__move(dt)
            v = sqrt(self.vx**2 + self.vy**2)
            if v > vmax:
                vmax = v
            if self.y <= 0:
                break
        self.return_to_start()
        return vmax

    def velocity_to_hit_target(self,theta,dt,xt,yt):
        rt = 2
        theta = (theta/180)*pi
        self.theta = theta
        is_hit = False
        vmin = 0
        vmax = 300
        while True:
            v = uniform(vmin,vmax)
            self.v0 = v
            self.return_to_start()
            is_overhit = False
            while True:
                self.__move(dt)
                d = sqrt((xt-self.x)**2+(yt-self.y)**2)
                if xt - rt < self.x < xt + rt:
                    if self.y > yt:
                        is_overhit = True
                if d <= rt:
                    is_hit = True
                    break
                elif self.y <= 0:
                    break
            if is_hit:
                break
            elif is_overhit:
                vmax = v
            else:
                vmin = v
        print("Potrebna brzina je {} ms^-1".format(v))
        
        plt.plot(self.xlist,self.ylist)
        
        xaxis = []
        yaxis = []

        for phi in range (1,3600):
            X = xt + rt*cos(phi/10)
            Y = yt + rt*sin(phi/10)
            xaxis.append(X)
            yaxis.append(Y)

        plt.plot(xaxis,yaxis)
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.show()
        self.return_to_start()

    def angle_to_hit_target(self,v0,dt,xt,yt):
        j = 1
        rt = 1
        self.v0 = v0
        theta1 = 0
        theta2 = 0
        thetamin1 = -90
        thetamax1 = 90
        thetamin2 = -90
        thetamax2 = 90
        xlist1 = []
        ylist1 = []
        xlist2 = []
        ylist2 = []
        is_hit1 = False
        is_hit2 = False
        for i in range(-90,91,1):
            theta = (i/180)*pi
            self.theta = theta
            self.return_to_start()
            is_hit = False
            is_overhit = False
            while True:
                self.__move(dt)
                d = sqrt((xt-self.x)**2+(yt-self.y)**2)
                if xt - rt < self.x < xt + rt:
                    if self.y > yt:
                        is_overhit = True
                if d <= rt:
                    is_hit = True
                    break
                elif self.y <= 0:
                    break
            if is_hit:
                theta1 = i
                xlist1 = self.xlist.copy()
                ylist1 = self.ylist.copy()
                is_hit1 = True
                break
            elif is_overhit:
                thetamax1 = i
                thetamin1 = i - 1
                break
            elif i == 90:
                j = 0
                break
        if j:
            for i in range(90,-91,-1):
                theta = (i/180)*pi
                self.theta = theta
                self.return_to_start()
                is_hit = False
                is_overhit = False
                while True:
                    self.__move(dt)
                    d = sqrt((xt-self.x)**2+(yt-self.y)**2)
                    if xt - rt < self.x < xt + rt:
                        if self.y > yt:
                            is_overhit = True
                    if d <= rt:
                        is_hit = True
                        break
                    elif self.y <= 0:
                        break
                if is_hit:
                    theta2 = i
                    xlist2 = self.xlist.copy()
                    ylist2 = self.ylist.copy()
                    is_hit2 = True
                    break
                elif is_overhit:
                    thetamax2 = i + 1
                    thetamin2 = i 
                    break
            if not is_hit1:
                while True:
                    theta = uniform(thetamin1,thetamax1)
                    thetarad = (theta/180)*pi
                    self.theta = thetarad
                    self.return_to_start()
                    is_overhit = False
                    while True:
                        self.__move(dt)
                        d = sqrt((xt-self.x)**2+(yt-self.y)**2)
                        if xt - rt < self.x < xt + rt:
                            if self.y > yt:
                                is_overhit = True
                        if d <= rt:
                            is_hit1 = True
                            break
                        elif self.y <= 0:
                            break
                    if is_hit1:
                        theta1 = theta
                        xlist1 = self.xlist.copy()
                        ylist1 = self.ylist.copy()
                        break
                    elif is_overhit:
                        thetamax1 = theta
                    else:
                        thetamin1 = theta
            if not is_hit2:
                while True:
                    theta = uniform(thetamin2,thetamax2)
                    thetarad = (theta/180)*pi
                    self.theta = thetarad
                    self.return_to_start()
                    is_overhit = False
                    while True:
                        self.__move(dt)
                        d = sqrt((xt-self.x)**2+(yt-self.y)**2)
                        if xt - rt < self.x < xt + rt:
                            if self.y > yt:
                                is_overhit = True
                        if d <= rt:
                            is_hit2 = True
                            break
                        elif self.y <= 0:
                            break
                    if is_hit2:
                        theta2 = theta
                        xlist2 = self.xlist.copy()
                        ylist2 = self.ylist.copy()
                        break
                    elif is_overhit:
                        thetamin2 = theta
                    else:
                        thetamax2 = theta
            print("Potreban kut iznosi {} ili {} stupnjeva".format(theta1,theta2))
            plt.plot(xlist1,ylist1)
            plt.plot(xlist2,ylist2)
            xaxis = []
            yaxis = []

            for phi in range (1,3600):
                X = xt + rt*cos(phi/10)
                Y = yt + rt*sin(phi/10)
                xaxis.append(X)
                yaxis.append(Y)

            plt.plot(xaxis,yaxis)
            plt.xlabel("x [m]")
            plt.ylabel("y [m]")
            plt.show()
            self.return_to_start()
        else:
            print("Brzina je premala za pogodak!")

    def angle_to_hit_target_ar(self,v0,dt,xt,yt):
        j = 1
        rt = 1
        self.v0 = v0
        theta1 = 0
        theta2 = 0
        thetamin1 = -90
        thetamax1 = 90
        thetamin2 = -90
        thetamax2 = 90
        xlist1 = []
        ylist1 = []
        xlist2 = []
        ylist2 = []
        is_hit1 = False
        is_hit2 = False
        for i in range(-90,91,1):
            theta = (i/180)*pi
            self.theta = theta
            self.return_to_start()
            is_hit = False
            is_overhit = False
            while True:
                if self.isCube:
                    self.__move_with_ar_cube(dt)
                else:
                    self.__move_with_ar(dt)
                d = sqrt((xt-self.x)**2+(yt-self.y)**2)
                if xt - rt < self.x < xt + rt:
                    if self.y > yt:
                        is_overhit = True
                if d <= rt:
                    is_hit = True
                    break
                elif self.y <= 0:
                    break
            if is_hit:
                theta1 = i
                xlist1 = self.xlist.copy()
                ylist1 = self.ylist.copy()
                is_hit1 = True
                break
            elif is_overhit:
                thetamax1 = i
                thetamin1 = i - 1
                break
            elif i == 90:
                j = 0
                break
        if j:
            for i in range(90,-91,-1):
                theta = (i/180)*pi
                self.theta = theta
                self.return_to_start()
                is_hit = False
                is_overhit = False
                while True:
                    if self.isCube:
                        self.__move_with_ar_cube(dt)
                    else:
                        self.__move_with_ar(dt)
                    d = sqrt((xt-self.x)**2+(yt-self.y)**2)
                    if xt - rt < self.x < xt + rt:
                        if self.y > yt:
                            is_overhit = True
                    if d <= rt:
                        is_hit = True
                        break
                    elif self.y <= 0:
                        break
                if is_hit:
                    theta2 = i
                    xlist2 = self.xlist.copy()
                    ylist2 = self.ylist.copy()
                    is_hit2 = True
                    break
                elif is_overhit:
                    thetamax2 = i + 1
                    thetamin2 = i 
                    break
            if not is_hit1:
                while True:
                    theta = uniform(thetamin1,thetamax1)
                    thetarad = (theta/180)*pi
                    self.theta = thetarad
                    self.return_to_start()
                    is_overhit = False
                    while True:
                        if self.isCube:
                            self.__move_with_ar_cube(dt)
                        else:
                            self.__move_with_ar(dt)
                        d = sqrt((xt-self.x)**2+(yt-self.y)**2)
                        if xt - rt < self.x < xt + rt:
                            if self.y > yt:
                                is_overhit = True
                        if d <= rt:
                            is_hit1 = True
                            break
                        elif self.y <= 0:
                            break
                    if is_hit1:
                        theta1 = theta
                        xlist1 = self.xlist.copy()
                        ylist1 = self.ylist.copy()
                        break
                    elif is_overhit:
                        thetamax1 = theta
                    else:
                        thetamin1 = theta
            if not is_hit2:
                while True:
                    theta = uniform(thetamin2,thetamax2)
                    thetarad = (theta/180)*pi
                    self.theta = thetarad
                    self.return_to_start()
                    is_overhit = False
                    while True:
                        if self.isCube:
                            self.__move_with_ar_cube(dt)
                        else:
                            self.__move_with_ar(dt)
                        d = sqrt((xt-self.x)**2+(yt-self.y)**2)
                        if xt - rt < self.x < xt + rt:
                            if self.y > yt:
                                is_overhit = True
                        if d <= rt:
                            is_hit2 = True
                            break
                        elif self.y <= 0:
                            break
                    if is_hit2:
                        theta2 = theta
                        xlist2 = self.xlist.copy()
                        ylist2 = self.ylist.copy()
                        break
                    elif is_overhit:
                        thetamin2 = theta
                    else:
                        thetamax2 = theta
            print("Potreban kut iznosi {} ili {} stupnjeva".format(theta1,theta2))
            plt.plot(xlist1,ylist1)
            plt.plot(xlist2,ylist2)
            xaxis = []
            yaxis = []

            for phi in range (1,3600):
                X = xt + rt*cos(phi/10)
                Y = yt + rt*sin(phi/10)
                xaxis.append(X)
                yaxis.append(Y)

            plt.plot(xaxis,yaxis)
            self.return_to_start()
        else:
            print("Brzina je premala za pogodak!")