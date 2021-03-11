import matplotlib.pyplot as plt
import math

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

while True:
    unos = input("Unesi iznos brzine u ms^-1:")
    if is_number(unos) and float(unos) > 0:
        v0 = float(unos)
        break
    else:
        print("Pogresan unos!")

while True:
    unos = input("Unesi kut u stupnjevima:")
    if is_number(unos) and 0 <= float(unos) <= 90:
        theta = float(unos)
        break
    else:
        print("Pogresan unos!")

theta = (theta/360)*2*math.pi
vx0 = v0 * math.cos(theta)
vy0 = v0 * math.sin(theta)
vy = vy0
x_list = []
y_list = []
t_list = []
t = 10
n = 100
dt = t/n
x = 0
y = 0
a = 9.81
t_ = 0
x_list.append(x)
y_list.append(y)
t_list.append(t_)

for i in range(n):
    t_ = t_ + dt
    x = x + vx0*dt
    vy = vy - a*dt
    y = y + vy*dt
    x_list.append(x)
    y_list.append(y)
    t_list.append(t_)

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x_list, y_list)
axs[0, 0].set_title("x-y graf")
axs[0, 1].plot(t_list, x_list)
axs[0, 1].set_title('x-t graf')
axs[1, 0].plot(t_list, y_list,)
axs[1, 0].set_title('y-t graf')
plt.show()
