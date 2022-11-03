from math import pow, fabs
import json

import matplotlib.pyplot as plt

dt = 0.01
m = 6.645E-27  # масса альфа-частицы
k = 8.98E9  # коэф. пропорциональности в законе Кулона
e = 1.602E-19  # заряд электрона


def v(v: float, coord1: float, coord2: float, dt: float, z: int):
    return v + (2 * k * z * e * e / m) * (coord1 / pow(coord1 ** 2 + coord2 ** 2, 1.5)) * dt


def calculation(x0: float = -1, y0: float = 1, vx0: float = 1, vy0: float = -0.5, xmax: float = 5, ymax: float = 5, z: int = 88) -> tuple[list[float], list[float]]:
    xlist, ylist = [], []
    x, y, vx, vy = x0, y0, v(vx0, x0, y0, dt*0.5, z), v(vy0, y0, x0, dt*0.5, z)

    while fabs(x) <= xmax and fabs(y) <= ymax:
        xlist.append(x)
        ylist.append(y)

        x += vx * dt
        y += vy * dt

        vx = v(vx, x, y, dt, z)
        vy = v(vy, y, x, dt, z)

    return xlist, ylist


def element_name():
    elements = {}
    with open('periodic_table.json', encoding='UTF-8') as file:
        elements = json.load(file)
    return elements


def draw(ax, x: list, y: list, z: int):
    ax.clear()
    ax.set(title='Траектория движения спутника',
           xlabel='x',
           ylabel='y')
    ax.grid()
    ax.plot(x, y, color='black', label=r'$\alpha$-частица')
    elements = element_name()
    ax.scatter(0, 0, color='navy', label=f'Ядро ({elements[str(z)]})')
    ax.legend()


def create_plot():
    fig = plt.figure(num=1, facecolor='gray')
    ax = fig.add_subplot(111)

    return ax


def main():
    ax = create_plot()

    x, y = calculation()

    draw(ax, x, y, z=88)

    plt.show()


if __name__ == '__main__':
    main()
