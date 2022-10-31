from dataclasses import dataclass
from math import exp, pi

import matplotlib.pyplot as plt


@dataclass(frozen=True)
class Const:
    p0: float = 1.27
    beta: float = 2.3026
    g: float = 9.8
    t_: int = 150
    v_: int = 7800
    h_: int = 17000
    dt: float = 0.001


class DimPar:
    def __init__(self, m0, m_end, S, c=0.4):
        # self.a = (Ft * Const.t_) / (m0 * Const.v_)
        self.b = (Const.t_ * Const.g) / Const.v_
        self.e = (Const.v_ * Const.t_) / Const.h_
        self.p = 0.5 * c * Const.p0 * S * Const.v_ * Const.t_ / m0 # /10
        self.k = m_end / m0


def f(tau, k):
    return (1 - (1 - k) * tau) if tau <= 1 else k


def dVdTau(tau: float, a: float, b: float, p: float, H: float, V: float, k: float):
    return (a - b * f(tau, k) - p * exp(-Const.beta * H) * V * V) / f(tau, k)


def calculation(a: float, b: float, e: float, p: float, k: float, const: Const):
    taulist, Vlist, Hlist = [], [], []
    tau, V, H = 0, 0, 0
    while tau <= 1:
        nextV = V + const.dt * 0.5 * abs(
            dVdTau(tau, a, b, p, H, V, k) + dVdTau(tau, a, b, p, H, V + const.dt * dVdTau(tau, a, b, p, H, V, k), k))
        nextH = H + e * V * const.dt

        taulist.append(tau)
        Vlist.append(V)
        Hlist.append(H)

        V = nextV
        H = nextH
        tau += const.dt
    return taulist, Vlist, Hlist


def draw_v(ax, t: list, v: list, a: float):
    match a:
        case 0.2:
            ax.plot(t, v, color='black', label=f'a = {a}')
        case 0.3:
            ax.plot(t, v, color='red', label=f'a = {a}')
        case 0.4:
            ax.plot(t, v, color='blue', label=f'a = {a}')
        case 0.5:
            ax.plot(t, v, color='purple', label=f'a = {a}')

    ax.legend()


def draw_h(ax, t: list, h: list, a: float):
    match a:
        case 0.2:
            ax.plot(t, h, color='black', label=f'a = {a}')
        case 0.3:
            ax.plot(t, h, color='red', label=f'a = {a}')
        case 0.4:
            ax.plot(t, h, color='blue', label=f'a = {a}')
        case 0.5:
            ax.plot(t, h, color='purple', label=f'a = {a}')

    ax.legend()


def data_entry() -> DimPar:
    try:
        m0 = float(input('m0='))
    except ValueError:
        m0 = 300000
    try:
        mend = float(input('m_end='))
    except ValueError:
        mend = 20000
    try:
        S = float(input('S='))
    except ValueError:
        S = 2 * pi * 5.5 * 50 + pi * 5.5 ** 2

    return DimPar(m0, mend, S)


def create_plot():
    fig = plt.figure(facecolor='gray')
    axV = fig.add_subplot(121)
    axH = fig.add_subplot(122)

    axV.grid()
    axH.grid()

    return axV, axH, fig


def main():
    axV, axH, fig = create_plot()

    rocket = data_entry()
    const = Const()

    tau, V, H = calculation(a := 0.2, rocket.b, rocket.e, rocket.p, rocket.k, const)
    # print(V)
    draw_v(axV, tau, V, a)
    draw_h(axH, tau, H, a)

    tau, V, H = calculation(a := 0.3, rocket.b, rocket.e, rocket.p, rocket.k, const)
    draw_v(axV, tau, V, a)
    draw_h(axH, tau, H, a)

    tau, V, H = calculation(a := 0.4, rocket.b, rocket.e, rocket.p, rocket.k, const)
    draw_v(axV, tau, V, a)
    draw_h(axH, tau, H, a)

    tau, V, H = calculation(a := 0.5, rocket.b, rocket.e, rocket.p, rocket.k, const)
    draw_v(axV, tau, V, a)
    draw_h(axH, tau, H, a)

    plt.show()


if __name__ == '__main__':
    main()
