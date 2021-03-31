import calculus
import matplotlib.pyplot as plt
import math

def funkcija1(x):
    return (math.e**x)*math.sin(x)

def int_funkcija1(x):
    return ((math.e**x)/2)*(math.sin(x)-math.cos(x))

def funkcija2(x):
    return 2*x**2 + 10

def int_funkcija2(x):
    return (2/3)*x**3 + 10*x

lower1,upper1 = calculus.integrate_rect(calculus.f2,3,7,100)
integral1 = calculus.integrate_trap(calculus.f2,3,7,100)
print("Donja i gornja meda su: {} i {}".format(lower1,upper1))
print("Rezultat integrala je: {}".format(integral1))

a = 0
b = 5
xlist = []
ylist1 = []
ylist2 = []
ylist3 = []
ylist4 = []
dn = 50
for i in range(1,20,1):
    xlist.append(dn*i)

for x in xlist:
    lower,upper = calculus.integrate_rect(funkcija1,a,b,x)
    integral_trap = calculus.integrate_trap(funkcija1,a,b,x)
    integral = int_funkcija1(b) - int_funkcija1(a)
    ylist1.append(lower)
    ylist2.append(upper)
    ylist3.append(integral_trap)
    ylist4.append(integral)

plt.plot(xlist,ylist1,".")
plt.plot(xlist,ylist2,".")
plt.plot(xlist,ylist3,".")
plt.plot(xlist,ylist4)
plt.xlabel("N steps")
plt.ylabel("integral")
plt.show()