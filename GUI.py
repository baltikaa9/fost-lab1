from tkinter import *
from main import fall_air, fall_viscous_med, draw_v, draw_h

root = Tk()
root.title('Лаба 3')
root.geometry('350x200')
root.resizable(width=False, height=False)

frame = Frame(root, bg='white')
frame.place(relwidth=1, relheight=1)


def create_buttons():
    """Кнопки"""
    btn_1 = Button(frame, text='Парашютист', bg='white', command=fall_1, width=16, height=2)
    btn_2 = Button(frame, text='Шар в вязкой среде', bg='white', command=fall_2, width=16, height=2)
    btn_quit = Button(frame, text='Выход', bg='white', command=root.destroy, width=16, height=2)

    btn_1.place(x=25, y=70)
    btn_2.place(x=200, y=70)
    btn_quit.place(x=115, y=140)


def fall_1():
    t1, v1, h1 = fall_air(80, 1.65, 0.33, c=1.22)
    t2, v2, h2 = fall_air(80, R=2.7, c=1.33)
    draw_v(t1, v1, t2, v2)
    draw_h(t1, h1, t2, h2)


def fall_2():
    t, v, h = fall_viscous_med(0.1, 7800, 1260, 1480)
    draw_v(t, v)
    draw_h(t, h)


if __name__ == '__main__':
    Label(frame, text='Выберите график', bg='white', font='Arial 14').pack()
    create_buttons()
    root.mainloop()
