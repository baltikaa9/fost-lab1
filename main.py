import matplotlib.pyplot as plt

dt = 0.00001
C = 1.0e-6
R = 1
L = 0.25
q0 = 4.0e-6
I0 = 1
tmax = 1


def calculation(I0: float, q0: float, C: float, R: float, L: float, tmax: float) -> tuple[list[float], list[float]]:
    tlist, qlist = [], []
    t = 0

    B = R / (2 * L)
    w02 = 1 / (L * C)
    I = I0 - (2 * B * I0 + w02 * q0) * dt * 0.5
    q = q0

    while t <= tmax:
        tlist.append(t)
        qlist.append(q)

        I = I - (2 * B * I + w02 * q) * dt
        q += I * dt
        t += dt
    return tlist, qlist


def draw(ax, x: list, y: list):
    ax.clear()
    ax.set(title='',
           xlabel='t',
           ylabel='q')
    ax.grid()
    ax.plot(x, y, color='black')


def create_plot():
    fig = plt.figure(num=1, facecolor='gray')
    ax = fig.add_subplot(111)
    return ax


def main():
    ax = create_plot()

    t, q = calculation(I0, q0, C, R, L, tmax)

    draw(ax, t, q)

    plt.show()


if __name__ == '__main__':
    main()
