import matplotlib.pyplot as plt
from math import sqrt, sin, cos, pi

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

while True:
    unos = input("Unesi x:")
    if is_number(unos):
        x = float(unos)
        break
    else:
        print("Pogresan unos!")
while True:
    unos = input("Unesi y:")
    if is_number(unos):
        y = float(unos)
        break
    else:
        print("Pogresan unos!")
while True:
    unos = input("Unesi xr:")
    if is_number(unos):
        xr = float(unos)
        break
    else:
        print("Pogresan unos!")
while True:
    unos = input("Unesi yr:")
    if is_number(unos):
        yr = float(unos)
        break
    else:
        print("Pogresan unos!")
while True:
    unos = input("Unesi r:")
    if is_number(unos):
        r = float(unos)
        break
    else:
        print("Pogresan unos!")

def funkcija(x,y,xr,yr,r):
    d = sqrt((x-xr)**2+(y-yr)**2)

    if d > r:
        print("Tocka je izvan kruznice.")
        print("Udaljena je {} od kruznice.".format(d-r))
    elif d == r:
        print("Tocka je na kruznici.")
    else: 
        print("Tocka je unutar kruznice.")

    xaxis = []
    yaxis = []

    for phi in range (1,3600):
        X = xr + r*cos(phi/10)
        Y = yr + r*sin(phi/10)
        xaxis.append(X)
        yaxis.append(Y)

    plt.plot(xaxis,yaxis)
    plt.plot([x],[y],'ro')

    while True:
            izbor = int(input("Unesi 1 za spremanje, a 2 za crtanje:"))
            if izbor == 1:
                ime = input("Ime grafa:")
                plt.savefig(f"{ime}.pdf")
                break
            elif izbor == 2:
                plt.show()
                break
            else:
                print("Pogresan unos!")

funkcija(x,y,xr,yr,r)