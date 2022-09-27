from dataclasses import dataclass
from math import sin, cos, exp, pi
from tkinter import messagebox
from typing import Tuple, List, Any
from math import sqrt

import matplotlib.pyplot as plt

g = 9.8


class Angle:
    def __init__(self, deg: float = None, rad: float = None):
        self.deg = deg
        self.rad = rad

        if self.rad is None:
            self.rad = self.deg / 180 * pi
        elif self.deg is None:
            self.deg = self.rad * 180 / pi
        else:
            self.rad = self.deg / 180 * pi

    def __str__(self):
        return f'∠α = {self.deg}°, {self.rad} rads'


# @dataclass
# class Movement:
#     v0: float = 10
#     alpha: Angle = Angle(deg=45)
#     # v0x = _v0 * cos(alpha.rad)
#     # v0y = _v0 * sin(alpha.rad)
#     m: float = 1
#     k: float = 0
#
#     def __str__(self):
#         return f'{self.v0=}, {self.alpha=}, {self.m=}, {self.k=}'


class Movement:
    def __init__(self, v0: float = 10, alpha: Angle = Angle(deg=45), m: float = 1, k: float = 0):
        self._v0 = v0
        self.alpha = alpha
        self.m = m
        self.k = k

        if self.k == int(self.k):
            self.k = int(self.k)

        self.v0x = self._v0 * cos(self.alpha.rad)
        self.v0y = self._v0 * sin(self.alpha.rad)


def data_entry() -> Movement:
    try:
        v0 = float(input('v0='))
    except ValueError:
        v0 = 10
    try:
        alpha = Angle(deg=float(input('α=')))
    except ValueError:
        alpha = Angle(deg=45)
    try:
        m = float(input('m='))
    except ValueError:
        m = 1
    try:
        k = float(input('k='))
    except ValueError:
        k = 0

    return Movement(v0, alpha, m, k)


# def calc_coord(v0: float, alpha: float, m: float, k: float) -> tuple[None, None] | tuple[
#     list[float | Any], list[float | Any]]:
#     t, xlist, ylist = 0, [], []
#     while True:
#         if k == 0:
#             x = v0 * cos(alpha) * t
#             y = v0 * sin(alpha) * t - g * t * t / 2
#         else:
#             try:
#                 x = v0 * cos(alpha) * m / k * (1 - exp(-(k / m) * t))
#                 # x = v0 * cos(alpha) * m / k * (1 - np.exp(-(k / m) * t, dtype=np.longfloat))
#                 y = m * ((v0 * sin(alpha) + m * g / k) * (1 - exp(-k * t / m)) - g * t) / k
#                 # y = m * ((v0 * sin(alpha) + m * g / k) * (1 - np.exp(-(k / m) * t, dtype=np.longfloat)) - g * t) / k
#             except ZeroDivisionError:
#                 messagebox.showinfo("Что-то пошло не так", 'Укажите массу')
#                 return None, None
#
#         xlist.append(x)
#         ylist.append(y)
#
#         if y <= 0 and t > 0:
#             break
#         t += 0.001
#     return xlist, ylist

dt = 0.001


def xt(x, v0x):
    return x + v0x * dt


def yt(y, v0y):
    return y + v0y * dt


def vx_next(vx, vy, m, k):
    return vx - k / m * sqrt(vx * vx + vy * vy) * vx * dt


def vy_next(vx, vy, m, k):
    return vy - (g + k / m * sqrt(vx * vx + vy * vy) * vy) * dt


def case_1(vx, vy):
    t, xlist, ylist = 0, [], []
    while True:
        x = vx * t
        y = vy * t - g * t * t / 2

        xlist.append(x)
        ylist.append(y)
        # print(y)

        if y <= 0 and t > 0:
            break
        t += dt

    return xlist, ylist


def case_2(vx, vy, m, k):
    t, xlist, ylist = 0, [], []
    x, y = 0, 0
    while True:
        x = xt(x, vx)
        y = yt(y, vy)

        vx = vx_next(vx, vy, m, k)
        vy = vy_next(vx, vy, m, k)

        xlist.append(x)
        ylist.append(y)

        if y <= 0 and t > 0:
            break
        t += dt

    return xlist, ylist


def draw_plot(x1: list, y1: list, x2: list, y2: list, k):
    fig = plt.figure(facecolor='gray')
    ax = fig.add_subplot(111)
    ax.set(title='Траектория движения тела',
           xlabel='X',
           ylabel='Y')

    ax.plot(x1, y1, color='black', label='k = 0')
    ax.plot(x2, y2, color='red', label=f'k = {k}')
    ax.grid()
    ax.legend()

    plt.show()


def main():
    obj = data_entry()
    x1, y1 = case_1(obj.v0x, obj.v0y)
    x2, y2 = case_2(obj.v0x, obj.v0y, obj.m, obj.k)
    draw_plot(x1, y1, x2, y2, obj.k)


if __name__ == '__main__':
    main()
