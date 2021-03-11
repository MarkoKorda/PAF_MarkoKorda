import matplotlib.pyplot as plt

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

while True:
    unos = input("Unesi silu u N:")
    if is_number(unos):
        F = float(unos)
        break
    else:
        print("Pogresan unos!")

while True:
    unos = input("Unesi masu u kg:")
    if is_number(unos) and float(unos) > 0:
        m = float(unos)
        break
    else:
        print("Pogresan unos!")

t = 10

x_list = []
v_list = []
a_list = []
t_list = []

x = 0
v = 0
a = F/m
t0 = 0
t_ = t0

x_list.append(x)
v_list.append(v)
a_list.append(a)
t_list.append(t_)

n = 100
dt = t/n

for i in range(n):
    t_ = t_ + dt
    v = v + a*dt
    x = x + v*dt
    x_list.append(x)
    v_list.append(v)
    a_list.append(a)
    t_list.append(t_)

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(t_list, x_list)
axs[0, 0].set_title("x-t graf")
axs[0, 1].plot(t_list, v_list)
axs[0, 1].set_title('v-t graf')
axs[1, 0].plot(t_list, a_list,)
axs[1, 0].set_title('a-t graf')
plt.show()
