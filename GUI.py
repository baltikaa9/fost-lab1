from math import fabs
from tkinter import *

from matplotlib import pyplot as plt

from main import calculation, create_plot, draw

root = Tk()
root.title('Траектория движения тела')
root.geometry('480x300')
root.resizable(width=False, height=False)

frame = Frame(root, bg='white')
frame.place(relwidth=1, relheight=1)


def create_labels():
    """Надписи"""
    Label(frame, text='Введите данные', bg='white', font='Arial 14').pack()

    label_x0 = Label(frame, text='x0:', bg='white')
    label_y0 = Label(frame, text='y0:', bg='white')
    label_xmax = Label(frame, text='xmax:', bg='white')
    label_ymax = Label(frame, text='ymax:', bg='white')
    label_vx0 = Label(frame, text='vx0:', bg='white')
    label_vy0 = Label(frame, text='vy0:', bg='white')
    label_Z = Label(frame, text='Z:', bg='white')

    label_x0.place(x=0, y=50)
    label_y0.place(x=0, y=70)
    label_xmax.place(x=0, y=90)
    label_ymax.place(x=0, y=110)
    label_vx0.place(x=0, y=130)
    label_vy0.place(x=0, y=150)
    label_Z.place(x=0, y=170)
    Label(frame, text='x0 - начальное x', bg='white').place(x=300, y=50)
    Label(frame, text='y0 - начальное y', bg='white').place(x=300, y=70)
    Label(frame, text='xmax - максимальное x', bg='white').place(x=300, y=90)
    Label(frame, text='ymax - максимальное y', bg='white').place(x=300, y=110)
    Label(frame, text='vx - начальная скорость по x', bg='white').place(x=300, y=130)
    Label(frame, text='vy - начальная скорость по y', bg='white').place(x=300, y=150)
    Label(frame, text='Z  - заряд ядра', bg='white').place(x=300, y=170)


def create_entries() -> tuple[Entry, Entry, Entry, Entry, Entry, Entry, Entry]:
    """Поля ввода"""
    entry_x0 = Entry(frame, bg="white", width=40)
    entry_y0 = Entry(frame, bg="white", width=40)
    entry_xmax = Entry(frame, bg="white", width=40)
    entry_ymax = Entry(frame, bg="white", width=40)
    entry_vx0 = Entry(frame, bg="white", width=40)
    entry_vy0 = Entry(frame, bg="white", width=40)
    entry_Z = Entry(frame, bg="white", width=40)

    entry_x0.place(x=37, y=50)
    entry_y0.place(x=37, y=70)
    entry_xmax.place(x=37, y=90)
    entry_ymax.place(x=37, y=110)
    entry_vx0.place(x=37, y=130)
    entry_vy0.place(x=37, y=150)
    entry_Z.place(x=37, y=170)

    entry_x0.insert(0, '-1')
    entry_y0.insert(0, '1')
    entry_xmax.insert(0, '3')
    entry_ymax.insert(0, '3')
    entry_vx0.insert(0, '1')
    entry_vy0.insert(0, '-0.5')
    entry_Z.insert(0, '88')

    entry_x0.bind('<Return>', run)
    entry_y0.bind('<Return>', run)
    entry_xmax.bind('<Return>', run)
    entry_ymax.bind('<Return>', run)
    entry_vx0.bind('<Return>', run)
    entry_vy0.bind('<Return>', run)
    entry_Z.bind('<Return>', run)

    return entry_x0, entry_y0, entry_xmax, entry_ymax, entry_vx0, entry_vy0, entry_Z


def create_buttons():
    """Кнопки"""
    btn_run = Button(frame, text='Построить', bg='white', command=run, width=16, height=2)
    btn_quit = Button(frame, text='Выход', bg='white', command=terminate, width=16, height=2)

    btn_run.place(x=480/2-57, y=200)
    btn_quit.place(x=480/2-57, y=250)


def terminate():
    root.destroy()
    plt.close()


def data_entry() -> tuple[float | int, float | int, float | int, float | int, float | int, float | int, int]:
    x0 = float(entry_x0.get())
    y0 = float(entry_y0.get())
    try:
        xmax = float(entry_xmax.get())
        if xmax <= fabs(x0) or xmax <= 0:
            raise ValueError
    except ValueError:
        entry_xmax.delete(0, END)
        entry_xmax.insert(0, f'{int(fabs(x0)+2)}')
        xmax = fabs(x0)+2
    try:
        ymax = float(entry_ymax.get())
        if ymax <= fabs(y0) or ymax <= 0:
            raise ValueError
    except ValueError:
        entry_ymax.delete(0, END)
        entry_ymax.insert(0, f'{int(fabs(y0)+2)}')
        ymax = fabs(y0)+2
    vx0 = float(entry_vx0.get())
    vy0 = float(entry_vy0.get())
    try:
        Z = int(entry_Z.get())
        if Z <= 0 or Z > 118:
            raise ValueError
    except ValueError:
        entry_Z.delete(0, END)
        entry_Z.insert(0, '88')
        Z = 88
    return x0, y0, xmax, ymax, vx0, vy0, Z


def run(event=None):
    global ax
    if not plt.fignum_exists(1):
        ax = create_plot()

    x0, y0, xmax, ymax, vx0, vy0, Z = data_entry()

    x, y = calculation(x0=x0, y0=y0, xmax=xmax, ymax=ymax, vx0=vx0, vy0=vy0, z=Z)
    draw(ax, x, y, Z)

    plt.show()


if __name__ == '__main__':
    create_labels()
    entry_x0, entry_y0, entry_xmax, entry_ymax, entry_vx0, entry_vy0, entry_Z = create_entries()
    create_buttons()
    root.mainloop()
