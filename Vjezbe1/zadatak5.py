import matplotlib.pyplot as plt

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def jednadzba_pravca(x1,y1,x2,y2):
    k = (y2 - y1)/(x2 - x1)
    l = y1 - k*x1

    if k == int(k):
        k = int(k)

    if l == int(l):
        l = int(l)

    if l >= 0:
        print("Jednadzba pravca je y = {}x + {}".format(k,l))
    else:
        print("Jednadzba pravca je y = {}x {}".format(k,l))

    dx = x2-x1
    dy = y2-y1

    plt.plot([x1-2*dx,x2+2*dx], [y1-2*dy,y2+2*dy])
    plt.plot([x1,x2], [y1,y2],'ro')
    plt.axis([x1-3*dx,x2+3*dx,y1-3*dy,y2+3*dy])
    
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


while True:
    unos = input("Unesi x:")
    if is_number(unos):
        x1 = float(unos)
        break
    else:
        print("Pogresan unos!")
while True:
    unos = input("Unesi y:")
    if is_number(unos):
        y1 = float(unos)
        break
    else:
        print("Pogresan unos!")
while True:
    unos = input("Unesi x:")
    if is_number(unos):
        x2 = float(unos)
        break
    else:
        print("Pogresan unos!")
while True:
    unos = input("Unesi y:")
    if is_number(unos):
        y2 = float(unos)
        break
    else:
        print("Pogresan unos!")

jednadzba_pravca(x1,y1,x2,y2)