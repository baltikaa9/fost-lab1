from math import cos, sin
from tkinter import *
from main import Movement, Angle, draw_plot, case_1, case_2

root = Tk()
root.title('Траектория движения тела')
root.geometry('350x350')
root.resizable(width=False, height=False)

frame = Frame(root, bg='white')
frame.place(relwidth=1, relheight=1)


def create_labels():
    """Надписи"""
    Label(frame, text='Введите данные', bg='white', font='Arial 14').pack()

    label_v0 = Label(frame, text='v0:', bg='white')
    label_alpha = Label(frame, text='α:', bg='white')
    label_m = Label(frame, text='m:', bg='white')
    label_k = Label(frame, text='k:', bg='white')

    label_v0.place(x=0, y=50)
    label_alpha.place(x=0, y=70)
    label_m.place(x=0, y=90)
    label_k.place(x=0, y=110)

    Label(frame, text='v0 - начальная скорость', bg='white').place(x=0, y=140)
    Label(frame, text='α - угол наклона', bg='white').place(x=0, y=160)
    Label(frame, text='m - масса', bg='white').place(x=0, y=180)
    Label(frame, text='k - коэффициент сопротивления воздуха', bg='white').place(x=0, y=200)


def create_entries() -> tuple[Entry, Entry, Entry, Entry]:
    """Поля ввода"""
    entry_v0 = Entry(frame, bg="white", width=50)
    entry_alpha = Entry(frame, bg="white", width=50)
    entry_m = Entry(frame, bg="white", width=50)
    entry_k = Entry(frame, bg="white", width=50)

    entry_v0.place(x=30, y=50)
    entry_alpha.place(x=30, y=70)
    entry_m.place(x=30, y=90)
    entry_k.place(x=30, y=110)

    entry_v0.insert(0, '10')
    entry_alpha.insert(0, '45')
    entry_m.insert(0, '1')
    entry_k.insert(0, '1')

    entry_v0.bind('<Return>', run)
    entry_alpha.bind('<Return>', run)
    entry_m.bind('<Return>', run)
    entry_k.bind('<Return>', run)

    return entry_v0, entry_alpha, entry_m, entry_k


def create_buttons():
    """Кнопки"""
    btn_run = Button(frame, text='Построить', bg='white', command=run, width=16, height=2)
    btn_quit = Button(frame, text='Выход', bg='white', command=root.destroy, width=16, height=2)

    btn_run.place(x=115, y=240)
    btn_quit.place(x=115, y=290)


def get_data() -> Movement:
    try:
        v0 = float(entry_v0.get())
        if v0 < 0:
            raise ValueError
    except ValueError:
        entry_v0.delete(0, END)
        entry_v0.insert(0, '10')
        v0 = 10
    try:
        alpha = Angle(deg=float(entry_alpha.get()))
    except ValueError:
        entry_alpha.delete(0, END)
        entry_alpha.insert(0, '45')
        alpha = Angle(deg=45)
    try:
        m = float(entry_m.get())
        if m <= 0:
            raise ValueError
    except ValueError:
        entry_m.delete(0, END)
        entry_m.insert(0, '1')
        m = 1
    try:
        k = float(entry_k.get())
        if k < 0:
            raise ValueError
    except ValueError:
        entry_k.delete(0, END)
        entry_k.insert(0, '0')
        k = 0
    return Movement(v0, alpha, m, k)


def run(event=None):
    obj = get_data()
    x1, y1 = case_1(obj.v0x, obj.v0y)
    x2, y2 = case_2(obj.v0x, obj.v0y, obj.m, obj.k)
    if x1 or y1 or x2 or y2 is not None:
        draw_plot(x1, y1, x2, y2, obj.k)


if __name__ == '__main__':
    create_labels()
    entry_v0, entry_alpha, entry_m, entry_k = create_entries()
    create_buttons()
    root.mainloop()
