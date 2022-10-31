from tkinter import *

from matplotlib import pyplot as plt

from main import calculation, create_plot, draw

root = Tk()
root.title('Траектория движения тела')
root.geometry('350x350')
root.resizable(width=False, height=False)

frame = Frame(root, bg='white')
frame.place(relwidth=1, relheight=1)


def create_labels():
    """Надписи"""
    Label(frame, text='Введите данные', bg='white', font='Arial 14').pack()

    label_x0 = Label(frame, text='x0:', bg='white')
    label_v0 = Label(frame, text='v0:', bg='white')
    label_t = Label(frame, text='t:', bg='white')

    label_x0.place(x=0, y=50)
    label_v0.place(x=0, y=70)
    label_t.place(x=0, y=90)
    Label(frame, text='x0 - начальное положение', bg='white').place(x=0, y=140)
    Label(frame, text='v0 - начальная скорость', bg='white').place(x=0, y=160)
    Label(frame, text='t - время полета', bg='white').place(x=0, y=180)


def create_entries() -> tuple[Entry, Entry, Entry]:
    """Поля ввода"""
    entry_x0 = Entry(frame, bg="white", width=40)
    entry_v0 = Entry(frame, bg="white", width=40)
    entry_t = Entry(frame, bg="white", width=40)

    entry_x0.place(x=45, y=50)
    entry_v0.place(x=45, y=70)
    entry_t.place(x=45, y=90)

    entry_x0.insert(0, '1')
    entry_v0.insert(0, '1')
    entry_t.insert(0, '100')

    entry_x0.bind('<Return>', run)
    entry_v0.bind('<Return>', run)
    entry_t.bind('<Return>', run)

    return entry_x0, entry_v0, entry_t


def create_buttons():
    """Кнопки"""
    btn_run = Button(frame, text='Построить', bg='white', command=run, width=16, height=2)
    btn_quit = Button(frame, text='Выход', bg='white', command=terminate, width=16, height=2)

    btn_run.place(x=115, y=240)
    btn_quit.place(x=115, y=290)


def terminate():
    root.destroy()
    plt.close()


def data_entry() -> tuple[float | int, float | int, float | int]:
    try:
        x0 = float(entry_x0.get())
        if x0 < 0:
            raise ValueError
    except ValueError:
        entry_x0.delete(0, END)
        entry_x0.insert(0, '1')
        x0 = 1
    try:
        v0 = float(entry_v0.get())
        if v0 < 0:
            raise ValueError
    except ValueError:
        entry_v0.delete(0, END)
        entry_v0.insert(0, '1')
        v0 = 1
    try:
        t = float(entry_t.get())
        if t <= 0:
            raise ValueError
    except ValueError:
        entry_t.delete(0, END)
        entry_t.insert(0, '100')
        t = 100
    return x0, v0, t


def run(event=None):
    global ax
    if not plt.fignum_exists(1):
        ax = create_plot()

    ax.clear()
    ax.grid()

    x0, v0, t = data_entry()

    x, y = calculation(x0, v0, t)
    draw(ax, x, y)

    plt.show()


if __name__ == '__main__':
    create_labels()
    entry_x0, entry_v0, entry_t = create_entries()
    create_buttons()
    root.mainloop()
