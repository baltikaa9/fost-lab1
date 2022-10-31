from tkinter import *

from matplotlib import pyplot as plt

from main import Const, DimPar, draw_v, draw_h, calculation, create_plot

root = Tk()
root.title('Траектория движения тела')
root.geometry('350x350')
root.resizable(width=False, height=False)

frame = Frame(root, bg='white')
frame.place(relwidth=1, relheight=1)


def create_labels():
    """Надписи"""
    Label(frame, text='Введите данные', bg='white', font='Arial 14').pack()

    label_m0 = Label(frame, text='m0:', bg='white')
    label_mend = Label(frame, text='m end:', bg='white')
    label_s = Label(frame, text='S:', bg='white')

    label_m0.place(x=0, y=50)
    label_mend.place(x=0, y=70)
    label_s.place(x=0, y=90)
    Label(frame, text='m0 - начальная масса (в кг)', bg='white').place(x=0, y=140)
    Label(frame, text='m end - конечная масса (в кг)', bg='white').place(x=0, y=160)
    Label(frame, text='S - площадь поверхности', bg='white').place(x=0, y=180)


def create_entries() -> tuple[Entry, Entry, Entry]:
    """Поля ввода"""
    entry_m0 = Entry(frame, bg="white", width=40)
    entry_mend = Entry(frame, bg="white", width=40)
    entry_S = Entry(frame, bg="white", width=40)

    entry_m0.place(x=45, y=50)
    entry_mend.place(x=45, y=70)
    entry_S.place(x=45, y=90)

    entry_m0.insert(0, '300000')
    entry_mend.insert(0, '20000')
    entry_S.insert(0, '1917')

    entry_m0.bind('<Return>', run)
    entry_mend.bind('<Return>', run)
    entry_S.bind('<Return>', run)

    return entry_m0, entry_mend, entry_S


def create_buttons():
    """Кнопки"""
    btn_run = Button(frame, text='Построить', bg='white', command=run, width=16, height=2)
    btn_quit = Button(frame, text='Выход', bg='white', command=root.destroy, width=16, height=2)

    btn_run.place(x=115, y=240)
    btn_quit.place(x=115, y=290)


def data_entry() -> DimPar:
    try:
        m0 = float(entry_m0.get())
        if m0 < 0:
            raise ValueError
    except ValueError:
        entry_m0.delete(0, END)
        entry_m0.insert(0, '300000')
        m0 = 300000
    try:
        mend = float(entry_mend.get())
        if mend < 0:
            raise ValueError
    except ValueError:
        entry_mend.delete(0, END)
        entry_mend.insert(0, '20000')
        mend = 20000
    try:
        S = float(entry_S.get())
        if S <= 0:
            raise ValueError
    except ValueError:
        entry_S.delete(0, END)
        entry_S.insert(0, '1917')
        S = 1917
    return DimPar(m0, mend, S)


def run(event=None):
    # if axV is None:
    #     axV, axH = create_plot()
    print(fig)
    axV.clear()
    axH.clear()

    axV.grid()
    axH.grid()

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
    axV, axH, fig = create_plot()
    create_labels()
    entry_m0, entry_mend, entry_S = create_entries()
    create_buttons()
    root.mainloop()
