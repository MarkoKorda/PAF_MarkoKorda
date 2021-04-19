class VertikalniHitac:
    def __init__(self,y0,v0):
        self.y = y0
        self.v = v0
        self.t = 0
        self.ylist = []
        self.vlist = []
        self.tlist = []
        self.ylist.append(self.y)
        self.vlist.append(self.v)
        self.tlist.append(self.t)
        print("Objekt je uspjesno stvoren!")
        print("Pocetna visina je: {} m\nPocetna brzina je: {} ms^-1".format(self.y,self.v))

    def change_y0(self,y0):
        self.y = y0

    def change_v0(self,v0):
        self.v = v0

    def return_to_start(self):
        self.y = self.ylist[0]
        self.v = self.vlist[0]
        self.t = 0
        self.ylist = []
        self.vlist = []
        self.tlist = []
        self.ylist.append(self.y)
        self.vlist.append(self.v)
        self.tlist.append(self.t)

    def __move(self,dt):
        self.v = self.v - 9.81 * dt
        self.y = self.y + self.v * dt
        self.t = self.t + dt
        self.ylist.append(self.y)
        self.vlist.append(self.v)
        self.tlist.append(self.t)

    def run_event(self,dt):
        while self.y > 0:
            self.__move(dt)
        return self.ylist, self.vlist, self.tlist

    def max_height(self,dt):
        while True:
            y_ = self.y
            self.__move(dt)
            if self.y < y_:
                break
        return y_

    def duration(self,dt):
        while self.y > 0:
            self.__move(dt)
        return self.t

    def __move_with_ar(self,dt,k):
        a = -9.81 - k * self.v
        self.v = self.v + a * dt
        self.y = self.y + self.v * dt
        self.t = self.t + dt
        self.ylist.append(self.y)
        self.vlist.append(self.v)
        self.tlist.append(self.t)

    def run_event_with_ar(self,dt,k):
        while self.y > 0:
            self.__move_with_ar(dt,k)
        return self.ylist, self.vlist, self.tlist
        
    def max_height_with_ar(self,dt,k):
        while True:
            y_ = self.y
            self.__move_with_ar(dt,k)
            if self.y < y_:
                break
        return y_

    def duration_with_ar(self,dt,k):
        while self.y > 0:
            self.__move_with_ar(dt,k)
        return self.t