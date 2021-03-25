import matplotlib.pyplot as plt
import numpy as np


class Kordynaty:
    def __init__(self, x1, y1, px1, py1, px2, py2, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.px1 = px1
        self.py1 = py1
        self.px2 = px2
        self.py2 = py2
        self.x2 = x2
        self.y2 = y2


def krzywa_beziera(p):
    warx = []
    wary = []
    for i in range(0, 201, 1):
        t = i / 200

        x = (p.x1 * (1 - t) ** 3 + p.px1 * 3 * t * (1 - t) ** 2 + p.px2 * 3 * t ** 2 * (1 - t) + p.x2 * t ** 3)
        y = (p.y1 * (1 - t) ** 3 + p.py1 * 3 * t * (1 - t) ** 2 + p.py2 * 3 * t ** 2 * (1 - t) + p.y2 * t ** 3)
        warx.append(x)
        wary.append(y)
    plt.plot(warx, wary, "black")


def wczytai():
    kord = []
    f = open("Dane.txt", "r")
    tekst = f.read()
    f.read()
    v = tekst.splitlines()
    for i in v:
        x = (i.split(","))
        y = np.asarray(x, dtype=np.float64, order='C')
        kord.append(Kordynaty(y[0], y[1], y[2], y[3], y[4], y[5], y[6], y[7]))
    for p in kord:
        krzywa_beziera(p)


if __name__ == '__main__':
    wczytai()
    plt.axis("off")
    plt.gca().invert_yaxis()
    plt.show()
