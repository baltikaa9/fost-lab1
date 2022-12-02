from math import fabs
from tkinter import *

from matplotlib import pyplot as plt

from main import calculation, create_plot, draw, create_plot_3d, draw_3d

root = Tk()
root.title('Движение заряженной частицы в магнитном поле')
root.geometry('490x300')
root.resizable(width=False, height=False)

frame = Frame(root, bg='white')
frame.place(relwidth=1, relheight=1)


def create_labels():
    """Надписи"""
    Label(frame, text='Введите данные', bg='white', font='Arial 14').pack()

    Label(frame, text='q, Кл - заряд частицы', bg='white').place(x=270, y=50)
    Label(frame, text='m, кг - масса частицы', bg='white').place(x=270, y=70)
    Label(frame, text='v0x, м/с - скорость по x', bg='white').place(x=270, y=90)
    Label(frame, text='v0z, м/с - скорость по z', bg='white').place(x=270, y=110)
    Label(frame, text='B, Тл - индукция магнитного поля', bg='white').place(x=270, y=130)
    Label(frame, text='t, с - время движения частицы', bg='white').place(x=270, y=150)


def create_entries() -> tuple[Entry, Entry, Entry, Entry, Entry, Entry]:
    """Поля ввода"""
    entry_q = Entry(frame, bg="white", width=40)
    entry_m = Entry(frame, bg="white", width=40)
    entry_v0x = Entry(frame, bg="white", width=40)
    entry_v0z = Entry(frame, bg="white", width=40)
    entry_B = Entry(frame, bg="white", width=40)
    entry_t = Entry(frame, bg="white", width=40)

    entry_q.place(x=5, y=50)
    entry_m.place(x=5, y=70)
    entry_v0x.place(x=5, y=90)
    entry_v0z.place(x=5, y=110)
    entry_B.place(x=5, y=130)
    entry_t.place(x=5, y=150)

    entry_q.insert(0, '1.602E-19')
    entry_m.insert(0, '1.673E-27')
    entry_v0x.insert(0, '800')
    entry_v0z.insert(0, '200')
    entry_B.insert(0, '1.67E-5')
    entry_t.insert(0, '0.1')

    entry_q.bind('<Return>', run3d)
    entry_m.bind('<Return>', run3d)
    entry_v0x.bind('<Return>', run3d)
    entry_v0z.bind('<Return>', run3d)
    entry_B.bind('<Return>', run3d)
    entry_t.bind('<Return>', run3d)

    return entry_q, entry_m, entry_v0x, entry_v0z, entry_B, entry_t


def create_buttons():
    """Кнопки"""
    btn_run_2d = Button(frame, text='Построить 2D', bg='white', command=run2d, width=16, height=2)
    btn_run_3d = Button(frame, text='Построить 3D', bg='white', command=run3d, width=16, height=2)
    btn_quit = Button(frame, text='Выход', bg='white', command=terminate, width=16, height=2)

    btn_run_2d.place(x=480 / 2 - 123, y=200)
    btn_run_3d.place(x=480 / 2 + 7, y=200)
    btn_quit.place(x=480 / 2 - 57, y=250)


def data_entry() -> tuple[float | int, float | int, float | int, float | int, float | int, float | int]:
    try:
        q = float(entry_q.get())
        if fabs(q) > 1.0E-15:
            raise ValueError
    except ValueError:
        entry_q.delete(0, END)
        entry_q.insert(0, '1.602E-19')
        q = 1.602E-19
    try:
        m = float(entry_m.get())
        if m < 0:
            raise ValueError
    except ValueError:
        entry_m.delete(0, END)
        entry_m.insert(0, '1.673E-27')
        m = 1.673E-27
    try:
        v0x = float(entry_v0x.get())
        if v0x < 0:
            raise ValueError
    except ValueError:
        entry_v0x.delete(0, END)
        entry_v0x.insert(0, '800')
        v0x = 800
    try:
        v0z = float(entry_v0z.get())
        if v0z < 0:
            raise ValueError
    except ValueError:
        entry_v0z.delete(0, END)
        entry_v0z.insert(0, '200')
        v0z = 200
    try:
        B = float(entry_B.get())
        if B > 1.67E-4:
            raise ValueError
    except ValueError:
        entry_B.delete(0, END)
        entry_B.insert(0, '1.67E-5')
        B = 1.67E-5
    try:
        t = float(entry_t.get())
        if t < 0:
            raise ValueError
    except ValueError:
        entry_t.delete(0, END)
        entry_t.insert(0, '0.1')
        t = 0.1
    return q, m, v0x, v0z, B, t


def run2d(event=None):
    global axXY, axXZ, axYZ
    if not plt.fignum_exists(1):
        axXY, axXZ, axYZ = create_plot()

    q, m, v0x, v0z, B, t = data_entry()

    x, y, z = calculation(q, m, v0x, v0z, B, t)
    draw(axXY, axXZ, axYZ, x, y, z)

    plt.show()


def run3d(event=None):
    global ax
    if not plt.fignum_exists(2):
        ax = create_plot_3d()

    q, m, v0x, v0z, B, t = data_entry()

    x, y, z = calculation(q, m, v0x, v0z, B, t)
    draw_3d(ax, x, y, z)

    plt.show()


def terminate():
    root.destroy()
    plt.close('all')


if __name__ == '__main__':
    create_labels()
    entry_q, entry_m, entry_v0x, entry_v0z, entry_B, entry_t = create_entries()
    create_buttons()
    root.mainloop()
