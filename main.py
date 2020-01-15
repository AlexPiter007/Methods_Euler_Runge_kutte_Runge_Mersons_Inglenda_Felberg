from tkinter import *
from math import fabs
r = Tk()
r.geometry('1300x700')
r.title("Methods")
r.state("zoomed")
##################################### Methods ############################################

def f(x, y):
    return x + y


def euler(a, b, h, y0):
    n = ((b - a) / h) + 1
    x = [a]
    y = [y0]
    for i in range(int(n)):
        x.append(x[i] + h)
        y.append(y[i] + h * f(x[i], y[i]))
    for i in range(int(n)):
        lbox.insert(END, " x = " + str(round(x[i], 2)) + "     y = " + str(y[i]))


def runge_kutte(a, b, h, y0):
    n = ((b - a) / h) + 1
    x = [a]
    y = [y0]
    for i in range(int(n)):
        x.append(x[i] + h)
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h / 2.0, y[i] + k1 / 2.0)
        k3 = h * f(x[i] + h / 2.0, y[i] + k2 / 2.0)
        k4 = h * f(x[i] + h, y[i] + k3)
        y.append(y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6)

    for i in range(int(n)):
        lbox1.insert(END, " x = " + str(round(x[i], 2)) + "     y = " + str(y[i]))


def rkutm(a, b, h, y0, e):
    n = 100000
    x = [a]
    y = [y0]
    for k in range(n):
        x.append(x[k] + h)
        k1 = f(x[k], y[k])
        k2 = f(x[k] + h / 3.0, y[k] + k1 * h / 3.0)
        k3 = f(x[k] + h / 3, y[k] + (k1 * h / 6) + (k2 * h / 3))
        k4 = f(x[k] + h / 2, y[k] + (k1 * h / 3) + (k3 * (3 * h) / 8))
        k5 = f(x[k] + h / 3, y[k] + (k1 * h / 2) - (k3 * (3 * h) / 2) + 2 * k3 * h)
        y.append(y[k] + (h * (k1 + 4 * k4 + k5)) / 6)
        r = (-2 * k1 + 9 * k3 - 8 * k4 + k1) / 32
        if (fabs(r) <= e) & (fabs(r) >= (e / 32)):
            h = h
        if fabs(r) > e:
            print("\tR = " + str(fabs(r)) + " > " + str(e))
            h = h / 2
            k = 0
        if fabs(r) < (e / 32):
            print("\tR = " + str(fabs(r)) + " < " + str(e / 32))
            h = h * 2
            k = 0
        if x[k] > b:
            break

    k = 0
    index = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    while True:
        for i in index:
            if i == round(x[k], 3):
                lbox2.insert(END, " x = " + str(round(x[k], 3)) + "     y = " + str(y[k]))
        if x[k] > b:
            break
        k += 1


def inglenda(a, b, h, y0):
    n = ((b - a) / h) + 1
    x = [a]
    y = [y0]
    for i in range(int(n)):
        x.append(x[i] + h)
        k1 = f(x[0], y[0])
        k2 = f(x[i] + h / 2, y[i] + k1 * (h / 2))
        k3 = f(x[i] + h / 2, y[i] + (h / 4) * (k1 + k2))
        k4 = f(x[i] + h, y[i] + h * (2 * k3 - k2))
        k5 = f(x[i] + (2 * h) / 3, y[i] + (h / 27) * (7 * k1 + 10 * k2 + k4))
        k6 = f(x[i] + h / 5, y[i] + (h / 625) * (28 * k1 - 125 * k2 + 546 * k3 + k4 * k4 - 378 * k5))
        y.append(y[i] + (1.0 / 336.0) * h * (14 * k1 + 35 * k4 + 162 * k5 + 125 * k6))
    for i in range(int(n)):
        lbox3.insert(END, " x = " + str(round(x[i], 2)) + "     y = " + str(y[i]))


def felberg(a, b, h, y0):
    n = ((b - a) / h) + 1
    x = [a]
    y = [y0]
    for i in range(int(n)):
        x.append(x[i] + h)
        k1 = f(x[0], y[0])
        k2 = f(x[i] + (h / 4), y[i] + k1 * (h / 4))
        k3 = f(x[i] + ((3 * h) / 8), y[i] + k1 * ((3 * h) / 32) + k2 * ((9 * h) / 32))
        k4 = f(x[i] + ((12 * h) / 13),
               y[i] + k1 * ((1932 * h) / 2197) - k2 * ((7200 * h) / 2197) + k3 * ((7296 * h) / 2197))
        k5 = f(x[i] + h,
               y[i] + k1 * ((439 * h) / 2162) - 8 * h * k2 + k3 * ((3680 * h) / 513) - k4 * ((845 * h) / 4104))
        k6 = f(x[i] + h / 2,
               y[i] + k1 * ((8 * h) / 27) + 2 * h * k2 - k3 * ((3544 * h) / 2565) + k4 * ((1859 * h) / 4104) - k5 * (
                       (11 * h) / 40))
        y.append(y[i] + h * ((16.0 / 135) * k1 + (6665.0 / 12825) * k3 + (28561.0 / 56430) * k4 + (9.0 / 50) * k5 + (
                2.0 / 55) * k6))
    for i in range(int(n)):
        lbox4.insert(END, " x = " + str(round(x[i], 2)) + "     y = " + str(y[i]))



###########################################################################################
def btnClik():
    a = float(a_str.get())
    b = float(b_str.get())
    h = float(h_str.get())
    y = float(y0_str.get())
    e = 0.001
    euler(a, b, h, y)
    runge_kutte(a, b, h, y)
    rkutm(a, b, h, y, e)
    inglenda(a, b, h, y)
    felberg(a, b, h, y)

def design():
    frame0 = Frame(r)
    frame = Frame(r)
    frame1 = Frame(r)
    frame2 = Frame(r)
    frame3 = Frame(r)
    frame4 = Frame(r)
    frame0.pack()
    frame.pack(side="left", padx=10)
    frame1.pack(side="left", padx=10)
    frame2.pack(side="left", padx=10)
    frame3.pack(side="left", padx=10)
    frame4.pack(side="left", padx=10)
    global a_str, b_str, h_str, y0_str
    a_str = StringVar()
    b_str = StringVar()
    h_str = StringVar()
    y0_str = StringVar()
    Label(frame0, text="Y=x+y", font=("Helvetica", 15)).pack(pady=10)
    # Etries
    Label(frame0, text="a = ").pack(side="left", pady=5)
    Entry(frame0, width=10, font=("Helvetica", 15), textvariable=a_str).pack(side="left", padx=10, pady=5)

    Label(frame0, text="b = ").pack(side="left", pady=5)
    Entry(frame0, width=10, font=("Helvetica", 15), textvariable=b_str).pack(side="left", padx=10, pady=5)

    Label(frame0, text="h = ").pack(side="left", pady=5)
    Entry(frame0, width=10, font=("Helvetica", 15), textvariable=h_str).pack(side="left", padx=10, pady=5)

    Label(frame0, text="y(0) = ").pack(side="left", pady=5)
    Entry(frame0, width=10, font=("Helvetica", 15), textvariable=y0_str).pack(side="left", padx=10, pady=5)

    # Buttons
    Button(frame0, text="Ok", command=btnClik, width=20, height=3).pack(side="left")

    global lbox, lbox1, lbox2, lbox3, lbox4
    # Labels
    Label(frame, text="Euler Methods").pack()
    Label(frame1, text="Runge Kutta Methods").pack()
    Label(frame2, text="Runnge Kutta Merson Methods").pack()
    Label(frame3, text="Inglenda Methods").pack()
    Label(frame4, text="Felberg Methods").pack()

    # Listboxs
    lbox = Listbox(frame, width=40, height=30)
    lbox1 = Listbox(frame1, width=40, height=30)
    lbox2 = Listbox(frame2, width=40, height=30)
    lbox3 = Listbox(frame3, width=40, height=30)
    lbox4 = Listbox(frame4, width=40, height=30)
    lbox.pack(side="left", fill="y")
    lbox1.pack(side="left", fill="y")
    lbox2.pack(side="left", fill="y")
    lbox3.pack(side="left", fill="y")
    lbox4.pack(side="left", fill="y")
    #


def main():
    design()
    r.mainloop()
if __name__ == '__main__':
    main()




