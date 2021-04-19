import VertikalniHitac as vert 

vh1 = vert.VertikalniHitac(5,10)
vh2 = vert.VertikalniHitac(7,8)

vh1.change_y0(11)
vh2.change_v0(4)

print("Pocetna visina prvog objekta je sada: {} m \nPocetna brzina drugog objekta je sada: {} ms^-1".format(vh1.y,vh2.v))