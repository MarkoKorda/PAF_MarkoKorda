import VertikalniHitac as vert 

dt1 = 0.01
dt2 = 0.05

vh1 = vert.VertikalniHitac(10,10)
maxy = vh1.max_height(dt1)
vh1.return_to_start()
t = vh1.duration(dt2)
print("Max visina je: {} m \nVrijeme trajanja je: {} s".format(maxy,t))