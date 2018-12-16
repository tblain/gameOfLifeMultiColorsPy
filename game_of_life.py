from tkinter import *
import numpy as np
import time

master = Tk()

def display(a):
    rows = a.shape[0]
    cols = a.shape[1]

    for x in range(0, rows):
        for y in range(0, cols):
            if a[x, y] == 1:
                w.create_rectangle(x*10, y*10, (x+1)*10, (y+1)*10, fill="blue")
            elif a[x, y] == -1:
                w.create_rectangle(x*10, y*10, (x+1)*10, (y+1)*10, fill="red")
                # print(a[x, y])
                # print(str(x*10) + " " + str((x+1)*10) + " " + str(y*10) + " " + str((y+1)*10))


def nbNeighOn(a, x, y, c):
    nb = 0
    rows = a.shape[0]
    cols = a.shape[1]

    if x > 0:
        if a[x-1, y] == c :
            nb+=1

        if y > 0:
            if a[x-1, y-1] == c:
                nb+=1

        if y < cols-1:
            if a[x-1, y+1] == c:
                nb+=1


    if x < rows-1:
        if a[x+1, y] == c:
            nb+=1

        if y > 0:
            if a[x+1, y-1] == c:
                nb+=1

        if y < cols-1:
            if a[x+1, y+1] == c:
                nb+=1

    if y > 0:
        if a[x, y-1] == c:
            nb+=1

    if y < cols-1:
        if a[x, y+1] == c:
            nb+=1

    return nb

def gol(a):
    rows = a.shape[0]
    cols = a.shape[1]

    b = np.empty([rows, cols])

    for x in range(0, rows):
        for y in range(0, cols):

            if a[x, y] == 0:
                nb1 = nbNeighOn(a, x, y, 1)
                nb2 = nbNeighOn(a, x, y, -1)
                nb = nb1 + nb2

                if nb == 3:
                    if nb1 > nb2:
                        b[x, y] = 1
                    else:
                        b[x, y] = -1
                else:
                    b[x, y] = 0

            else:
                c = a[x, y]
                nba = nbNeighOn(a, x, y, c)
                nbe = nbNeighOn(a, x, y, -c)
                nb = nbe + nba

                if nb > 5 or nb < 3:
                        b[x, y] = 0
                else:
                    diff = nba - nbe

                    if -1 <= diff <= 1:
                        b[x, y] = 0
                    elif diff < -3:
                        b[x, y] = -c
                    else: b[x, y] = c

    return b



w = Canvas(master, width=1500, height=900)
w.pack()

choices = np.array([0, 1, -1])

a = np.random.randint(-1, 2, size=(100,100))

while True:
    a = gol(a)
    w.delete(ALL)
    display(a)
    time.sleep(0.01)
    master.update_idletasks()
    master.update()
