import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from vector import Vector3D

q0 = 1.602E-19
m0 = 1.673E-27
v0x = 800
v0z = 200
B0 = 1.67E-5
Tmax = 0.015
dt = 0.00001


def calculation(q: float, m: float, v0x: float, v0z: float, B0: float, Tmax: float) -> tuple[list[float], list[float], list[float]]:
    xlist, ylist, zlist = [], [], []

    B = Vector3D(0, 0, B0)
    v = Vector3D(v0x, 0, v0z)
    R = Vector3D()
    t = 0

    A = (q / m) * (B * v)
    v += A * dt * 0.5

    while t <= Tmax:
        xlist.append(R.x)
        ylist.append(R.y)
        zlist.append(R.z)

        A = (q / m) * (B * v)
        v += A * dt
        R += v * dt
        t += dt
    return xlist, ylist, zlist


def draw(axXY, axXZ, axYZ, x: list, y: list, z: list):
    axXY.clear()
    axXY.set(title='',
           xlabel='X',
           ylabel='Y')
    axXY.grid()
    axXY.plot(x, y, color='black')

    axXZ.clear()
    axXZ.set(title='',
             xlabel='X',
             ylabel='Z')
    axXZ.grid()
    axXZ.plot(x, z, color='black')

    axYZ.clear()
    axYZ.set(title='',
             xlabel='Y',
             ylabel='Z')
    axYZ.grid()
    axYZ.plot(y, z, color='black')


def draw_3d(ax, x: list, y: list, z: list):
    ax.clear()
    ax.set(title='Движение заряженной частицы в магнитном поле',
           xlabel='X',
           ylabel='Y',
           zlabel='Z')
    # ax.scatter(0, 0, color='black')
    ax.plot3D(x, y, z, color='black')


def create_plot():
    fig = plt.figure(num=1, facecolor='gray')
    gs = fig.add_gridspec(1, 4)
    axXY = fig.add_subplot(gs[0, :2])
    axXZ = fig.add_subplot(gs[0, 2])
    axYZ = fig.add_subplot(gs[0, 3])
    return axXY, axXZ, axYZ


def create_plot_3d():
    fig = plt.figure(num=2, facecolor='gray')
    ax = plt.axes(projection='3d')
    return ax


def main():
    axXY, axXZ, axYZ = create_plot()
    ax = create_plot_3d()
    x, y, z = calculation(q0, m0, v0x, v0z, B0, Tmax)

    draw(axXY, axXZ, axYZ, x, y, z)
    draw_3d(ax, x, y, z)

    plt.show()


if __name__ == '__main__':
    main()
