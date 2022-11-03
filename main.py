from math import sqrt

import matplotlib.pyplot as plt

dt = 0.01


def V(v: float, coord1: float, coord2: float):
    a = -coord1 / sqrt((coord1 ** 2 + coord2 ** 2) ** 3)
    return v + a * dt


def calculation(x0: float, v0: float, t: float) -> tuple[list[float], list[float]]:
    x, y, vx, vy = x0, 0, 0, v0
    xlist, ylist = [], []
    t0 = 0

    while t0 < t:
        xlist.append(x)
        ylist.append(y)

        vx = V(vx, x, y)
        vy = V(vy, y, x)

        x += vx * dt
        y += vy * dt

        t0 += dt

    return xlist, ylist


def draw(ax, x: list, y: list):
    ax.clear()
    ax.set(title='Траектория движения спутника',
           xlabel='x',
           ylabel='y')
    ax.grid()
    ax.plot(x, y, color='black')
    ax.scatter(0, 0, color='dodgerblue', label='Земля')
    ax.legend()


def create_plot():
    fig = plt.figure(num=1, facecolor='gray')
    ax = fig.add_subplot(111)

    return ax


def main():
    ax = create_plot()

    x0 = 1
    v0 = 1
    t = 100

    x, y = calculation(x0, v0, t)

    draw(ax, x, y)

    plt.show()


if __name__ == '__main__':
    main()
