import calculus
import matplotlib.pyplot as pyplot

lower,upper = calculus.integrate_rect(calculus.f2,3,7,100)
integral = calculus.integrate_trap(calculus.f2,3,7,100)
print("Donja i gornja meda su: {} i {}".format(lower,upper))
print("Rezultat integrala je: {}".format(integral))