import kosi_hitac as kh

v0 = 50
theta = 45
y0 = 60
xm = 280
ym = 30
rm = 5

kh.crtanje_putanje(v0,theta,y0)
print("Projektil je dosegao visinu od {} m".format(kh.maksimalna_visina(v0,theta,y0)))
print("Domet projektila je {} m".format(kh.domet(v0,theta,y0)))
print("Projektil je dosegao maksimalnu brzinu od {} ms^-1".format(kh.maksimalna_brzina(v0,theta,y0)))
kh.gadanje_mete(v0,theta,y0,xm,ym,rm)