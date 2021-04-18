import gibanje

def F1(x,v,t):
    F = 10
    return F

def F2(x,v,t):
    k = 50
    F = -k*x
    return F

p1 = gibanje.Particle(3,7,3,F1)
p1.move_particle(0.01,10)
p1.plot_all()
p2 = gibanje.Particle(4,10,15,F2)
p2.move_particle(0.01,10)
p2.plot_all()