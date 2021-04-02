import particle as prt 

p1 = prt.Particle(50,45,30,40)
p2 = prt.Particle(60,30,50,70)
print("Ukupno vrijeme je: {} s".format(p1.total_time(0.01)))
print("Maksimalna brzina je: {} ms^-1".format(p1.max_speed(0.01)))
p1.velocity_to_hit_target(55,0.01,160,170)
p2.angle_to_hit_target(50,0.01,100,90)