from math import pi

import matplotlib.pyplot as plt


def fall_air(m, height=None, chest_circumference=None, R=None, ro=1.29, c=None, g=9.8):
    """Парашютист"""
    t, v0, h0 = 0, 0, 0
    tlist, vlist, hlist = [], [], []
    if R is None:
        S = height * chest_circumference
        tau = 0.2
    else:
        S = pi * R * R
        tau = 0.2
    k = 0.5 * c * S * ro

    while t <= 60:
        v = v0 + tau / 2 * ((m * g - k * v0 * v0) / m + (m * g - k * (v0 + tau * (m * g - k * v0 * v0) / m) ** 2) / m)
        h = h0 + v*tau

        vlist.append(v0)
        tlist.append(t)
        hlist.append(h0)

        v0 = v
        h0 = h
        t += tau

    return tlist, vlist, hlist


def fall_viscous_med(r, ro_solid, ro_liquid, viscosity, g=9.8):
    """Шар в глицерине"""
    t, v0, h0 = 0, 0, 0
    tlist, vlist, hlist = [], [], []

    tau = 0.02
    m1 = 4/3 * pi * r**3 * (ro_solid - ro_liquid)
    m = 4/3 * pi * r**3 * ro_solid
    k = 6 * pi * viscosity * r

    while t <= 1:
        v = v0 + tau/2 * ((m1*g - k*v0)/m + (m1*g - k * (v0 + tau * (m1*g - k*v0)/m))/m)
        h = h0 + v * tau

        vlist.append(v0)
        tlist.append(t)
        hlist.append(h0)

        v0 = v
        h0 = h
        t += tau

    return tlist, vlist, hlist


def draw_v(t1: list, v1: list, t2: list = None, v2: list = None):
    fig = plt.figure(facecolor='gray')
    ax = fig.add_subplot(111)
    ax.set(title='График зависимости v от t',
           xlabel='время t, (с)',
           ylabel='скорость v, (м/с)')

    if t2 is not None:
        ax.plot(t1, v1, color='black', label='Без парашюта')
        ax.plot(t2, v2, color='red', label='С парашютом')

        ax.legend()
    else:
        ax.plot(t1, v1, color='black')

    ax.grid()
    plt.show()


def draw_h(t1: list, h1: list, t2: list = None, h2: list = None):
    fig = plt.figure(facecolor='gray')
    ax = fig.add_subplot(111)
    ax.set(title='График зависимости h от t',
           xlabel='время t, (с)',
           ylabel='высота h, (м)')

    if t2 is not None:
        ax.plot(t1, h1, color='black', label='Без парашюта')
        ax.plot(t2, h2, color='red', label='С парашютом')

        ax.legend()
    else:
        ax.plot(t1, h1, color='black')

    ax.grid()
    plt.show()


def main():
    t1, v1, h1 = fall_air(80, 1.65, 0.33, c=1.22)
    t2, v2, h2 = fall_air(80, R=2.7, c=1.33)
    draw_v(t1, v1, t2, v2)
    draw_h(t1, h1, t2, h2)

    t, v, h = fall_viscous_med(0.1, 7800, 1260, 1480)
    draw_v(t, v)
    draw_h(t, h)


if __name__ == '__main__':
    main()
