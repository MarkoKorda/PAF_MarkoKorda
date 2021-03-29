import calculus
import matplotlib.pyplot as plt

listx1,listy1 = calculus.derivate(calculus.f3,-5,5,0.1,2)
listy2 = []
for element in listx1:
    y2 = calculus.der_f3(element)
    listy2.append(y2)
plt.plot(listx1,listy1,".")
plt.plot(listx1,listy2)
plt.show()