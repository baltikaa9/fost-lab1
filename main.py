from dataclasses import dataclass
from math import sin, cos, exp, pi
from tkinter import messagebox
from typing import Tuple, List, Any

import matplotlib.pyplot as plt
import numpy as np

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


@dataclass
class Movement:
    v0: float = 20
    alpha: Angle = Angle(deg=45)
    m: float = 0
    k: float = 0

    def __str__(self):
        return f'{self.v0=}, {self.alpha=}, {self.m}, {self.k}'


def data_entry() -> Movement:
    try:
        v0 = float(input('v0='))
    except ValueError:
        v0 = 20
    try:
        alpha = Angle(deg=float(input('α=')))
    except ValueError:
        alpha = Angle(deg=45)
    try:
        m = float(input('m='))
    except ValueError:
        m = 0
    try:
        k = float(input('k='))
    except ValueError:
        k = 0

    return Movement(v0, alpha, m, k)


def calc_coord(v0: float, alpha: float, m: float, k: float) -> tuple[None, None] | tuple[
    list[float | Any], list[float | Any]]:
    t, xlist, ylist = 0, [], []
    while True:
        if k == 0:
            x = v0 * cos(alpha) * t
            y = v0 * sin(alpha) * t - g * t * t / 2
        else:
            try:
                x = v0 * cos(alpha) * m / k * (1 - exp(-(k / m) * t))
                # x = v0 * cos(alpha) * m / k * (1 - np.exp(-(k / m) * t, dtype=np.longfloat))
                y = m * ((v0 * sin(alpha) + m * g / k) * (1 - exp(-k * t / m)) - g * t) / k
                # y = m * ((v0 * sin(alpha) + m * g / k) * (1 - np.exp(-(k / m) * t, dtype=np.longfloat)) - g * t) / k
            except ZeroDivisionError:
                messagebox.showinfo("Что-то пошло не так", 'Укажите массу')
                return None, None

        xlist.append(x)
        ylist.append(y)

        if y <= 0 and t > 0:
            break
        t += 0.001
    return xlist, ylist


def draw_plot(x: list, y: list):
    fig = plt.figure(facecolor='gray')
    ax = fig.add_subplot(111)
    ax.set(title='Траектория движения тела',
           xlabel='X',
           ylabel='Y')

    ax.plot(x, y, color='black')
    plt.show()


def main():
    obj = data_entry()
    x, y = calc_coord(obj.v0, obj.alpha.rad, obj.m, obj.k)
    draw_plot(x, y)


if __name__ == '__main__':
    main()
