import math

def derivate_3_step(func,x,h):
    derivate = (func(x+h)-func(x-h))/(2*h)
    return derivate

def derivate_2_step(func,x,h):
    derivate = (func(x+h)-func(x))/h
    return derivate

def derivate(func,a,b,h,m = 3):
    listx = []
    listy = []
    i = a
    while i <= b:
        listx.append(i)
        i += h
    if m == 2:
        for element in listx:
            derivate = derivate_2_step(func,element,h)
            listy.append(derivate)
    elif m == 3:
        for element in listx:
            derivate = derivate_3_step(func,element,h)
            listy.append(derivate)
    return listx,listy
    
def integrate_rect(func,a,b,n):
    h = (b-a)/n
    upper = 0
    lower = 0
    i = a
    j = a + h
    for k in range(n):
        if abs(func(i)) >= abs(func(j)):
            upper += func(i)*h
            lower += func(j)*h
        else:
            upper += func(j)*h
            lower += func(i)*h
        i += h
        j += h
    return lower,upper

def integrate_trap(func,a,b,n):
    h = (b-a)/n
    integral = 0
    i = a
    j = a + h
    for k in range(n):
        integral += ((func(i) + func(j))/2)*h
        i += h
        j += h
    return integral

def f1(x):
    return x*x

def f2(x):
    return 6*x**3 - 2*x**2 + 4*x - 7

def f3(x):
    return 4*math.sin(x) + 3*math.cos(2*x)

def der_f1(x):
    return 2*x

def der_f2(x):
    return 18*x**2 - 4*x + 4

def der_f3(x):
    return 4*math.cos(x) - 6*math.sin(2*x)




