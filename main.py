from math import sin, cos, exp, pi

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
            self.rad = self.deg * pi / 180

    def deg_to_rad(self) -> None:
        self.rad = self.deg * pi / 180

    def rad_to_deg(self) -> None:
        self.deg = self.rad * 180 / pi

    def __str__(self):
        return f'∠α = {self.deg}°, {self.rad} rads'


def data_entry():
    v0 = float(input('v0='))
    alpha = Angle(deg=float(input('α=')))
    m = float(input('m='))
    k = float(input('k='))

    return v0, alpha, m, k


def calc_coord(v0: float, alpha: float, m: float, k: float) -> tuple[list[float], list[float]]:
    t, xlist, ylist = 0, [], []
    while True:
        if k == 0:
            x = v0 * cos(alpha) * t
            y = v0 * sin(alpha) * t - g * t * t / 2
        else:
            x = v0 * cos(alpha) * m / k * (1 - exp(-k * t / m))
            y = m * ((v0 * sin(alpha) + m * g / k) * (1 - exp(-k * t / m)) - g * t) / k

        xlist.append(x)
        ylist.append(y)

        if y <= 0 and t > 0:
            break
        t += 0.001
    return xlist, ylist


def draw_plot(x: list, y: list):
    plt.plot(x, y)
    plt.show()


def main():
    v0, alpha, m, k = data_entry()
    x, y = calc_coord(v0, alpha.rad, m, k)
    draw_plot(x, y)


if __name__ == '__main__':
    main()
