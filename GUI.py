from math import fabs
from tkinter import *

from matplotlib import pyplot as plt

from main import calculation, create_plot, draw

root = Tk()
root.title('Траектория движения тела')
root.geometry('490x300')
root.resizable(width=False, height=False)

frame = Frame(root, bg='white')
frame.place(relwidth=1, relheight=1)


def create_labels():
    """Надписи"""
    Label(frame, text='Введите данные', bg='white', font='Arial 14').pack()

    Label(frame, text='I, А - начальная сила тока', bg='white').place(x=270, y=50)
    Label(frame, text='q, Кл - начальный заряд конденсатора', bg='white').place(x=270, y=70)
    Label(frame, text='C, Ф - емкость конденсатора', bg='white').place(x=270, y=90)
    Label(frame, text='R, Ом - активное сопротивление', bg='white').place(x=270, y=110)
    Label(frame, text='L, Гн - индуктивность катушки', bg='white').place(x=270, y=130)
    Label(frame, text='t, с - время колебаний', bg='white').place(x=270, y=150)


def create_entries() -> tuple[Entry, Entry, Entry, Entry, Entry, Entry]:
    """Поля ввода"""
    entry_I0 = Entry(frame, bg="white", width=40)
    entry_q0 = Entry(frame, bg="white", width=40)
    entry_C = Entry(frame, bg="white", width=40)
    entry_R = Entry(frame, bg="white", width=40)
    entry_L = Entry(frame, bg="white", width=40)
    entry_t = Entry(frame, bg="white", width=40)

    entry_I0.place(x=5, y=50)
    entry_q0.place(x=5, y=70)
    entry_C.place(x=5, y=90)
    entry_R.place(x=5, y=110)
    entry_L.place(x=5, y=130)
    entry_t.place(x=5, y=150)

    entry_I0.insert(0, '0')
    entry_q0.insert(0, '4.0e-6')
    entry_C.insert(0, '1.0e-6')
    entry_R.insert(0, '1')
    entry_L.insert(0, '0.25')
    entry_t.insert(0, '1')

    entry_I0.bind('<Return>', run)
    entry_q0.bind('<Return>', run)
    entry_C.bind('<Return>', run)
    entry_R.bind('<Return>', run)
    entry_L.bind('<Return>', run)
    entry_t.bind('<Return>', run)

    return entry_I0, entry_q0, entry_C, entry_R, entry_L, entry_t


def create_buttons():
    """Кнопки"""
    btn_run = Button(frame, text='Построить', bg='white', command=run, width=16, height=2)
    btn_quit = Button(frame, text='Выход', bg='white', command=terminate, width=16, height=2)

    btn_run.place(x=480/2-57, y=200)
    btn_quit.place(x=480/2-57, y=250)


def terminate():
    root.destroy()
    plt.close()


def data_entry() -> tuple[float | int, float | int, float | int, float | int, float | int, float | int]:
    try:
        I0 = float(entry_I0.get())
        if I0 < 0:
            raise ValueError
    except ValueError:
        entry_I0.delete(0, END)
        entry_I0.insert(0, '0')
        I0 = 0
    try:
        q0 = float(entry_q0.get())
        if q0 < 0:
            raise ValueError
    except ValueError:
        entry_q0.delete(0, END)
        entry_q0.insert(0, '4.0e-6')
        q0 = 4.0e-6
    try:
        C = float(entry_C.get())
        if C < 0:
            raise ValueError
    except ValueError:
        entry_C.delete(0, END)
        entry_C.insert(0, '1.0e-6')
        C = 1.0e-6
    try:
        R = float(entry_R.get())
        if R < 0:
            raise ValueError
    except ValueError:
        entry_R.delete(0, END)
        entry_R.insert(0, '1')
        R = 1
    try:
        L = float(entry_L.get())
        if L < 0:
            raise ValueError
    except ValueError:
        entry_L.delete(0, END)
        entry_L.insert(0, '0.25')
        L = 0.25
    try:
        t = float(entry_t.get())
        if t < 0:
            raise ValueError
    except ValueError:
        entry_t.delete(0, END)
        entry_t.insert(0, '1')
        t = 1
    return I0, q0, C, R, L, t


def run(event=None):
    global ax
    if not plt.fignum_exists(1):
        ax = create_plot()

    I0, q0, C, R, L, t = data_entry()

    t, q = calculation(I0=I0, q0=q0, C=C, R=R, L=L, tmax=t)
    draw(ax, t, q)

    plt.show()


if __name__ == '__main__':
    create_labels()
    entry_I0, entry_q0, entry_C, entry_R, entry_L, entry_t = create_entries()
    create_buttons()
    root.mainloop()
