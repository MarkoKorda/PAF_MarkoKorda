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