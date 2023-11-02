# NiceRice
# git push origin master
import numpy as np
from tkinter import *
#

#
# source https://www.lakeshore.com/docs/default-source/product-downloads/ethernet-firmware-updates/curve_dt670.zip?sfvrsn=bd514207_4

def C_100_500(Z):
    ZL = 0.070000
    ZU = 0.99799
    T = 0
    constants = (
    306.592351, -205.393808, -4.695680, -2.031603, -0.071792, -0.437682, 0.176352, -0.182516, 0.064687, -0.027019,
    0.010019)
    normalized_var = ((Z - ZL) - (ZU - Z)) / (ZU - ZL)

    for index in range(len(constants)):
        T = T + constants[index] * np.cos(index * np.arccos(normalized_var))
    return T


def C_24_100(Z):
    ZL = 0.909416
    ZU = 1.122751
    T = 0
    constants = (
    82.017868, -59.064244, -1.356615, 1.055396, 0.837341, 0.431875, 0.440840, -0.061588, 0.209414, -0.120882, 0.055734,
    -0.035974)
    normalized_var = ((Z - ZL) - (ZU - Z)) / (ZU - ZL)

    for index in range(len(constants)):
        T = T + constants[index] * np.cos(index * np.arccos(normalized_var))
    return T


def C_12_24(Z):
    ZL = 1.11230
    ZU = 1.38373
    T = 0
    constants = (
    17.244846, -7.964373, 0.625343, -0.105068, 0.292196, -0.344492, 0.271670, -0.151722, 0.121320, -0.035566, 0.045966)
    normalized_var = ((Z - ZL) - (ZU - Z)) / (ZU - ZL)

    for index in range(len(constants)):
        T = T + constants[index] * np.cos(index * np.arccos(normalized_var))
    return T


def C_2_12(Z):
    ZL = 1.294390
    ZU = 1.680000
    T = 0
    constants = (
    6.429274, -7.514262, -0.725882, -1.117846, -0.562041, -0.360239, -0.229751, -0.135713, -0.068203, -0.029755)
    normalized_var = ((Z - ZL) - (ZU - Z)) / (ZU - ZL)

    for index in range(len(constants)):
        T = T + constants[index] * np.cos(index * np.arccos(normalized_var))
    return T


# source: https://python-course.eu/tkinter_entry_widgets.php
# globally declare the expression variable
expression = ""


# Function to update expression
# in the text entry box
def press(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    expression.set(expression)


import tkinter as tk
#from math import *


def evaluate(event):
    # res.configure(text = "Result: " + str(C_2_12(float(entry.get()))) + " K")

    user_input = float(str(entry.get().replace(",", ".")))  # replace comma to dot
#
    if 0.090681 <= user_input < 1:
        kelvin = str(round(C_100_500(user_input), 2))
    elif 1 <= user_input < 1.125923:
        kelvin = str(round(C_24_100(user_input), 2))
    elif 1.125923 <= user_input <= 1.334990:
        kelvin = str(round(C_12_24(user_input), 2))
    elif 1.334990 <= user_input <= 1.634720:
        kelvin = str(round(C_2_12(user_input), 2))
    else:
        res.configure(text="out of range")
    degree = str(round((float(kelvin) - 273.15), 2))
    res.configure(text=str(user_input) + "V \u2248 " + kelvin + " K or " + degree + " °C")


w = tk.Tk()
w.title("LakeShore Cryotronics DT-670 Series")
w.geometry("360x60")
tk.Label(w, text="(2K) 1.634720V \u2264 range \u2264 0.090681V (500K)").pack()
entry = tk.Entry(w)
entry.bind("<Return>", evaluate)
entry.pack()
res = tk.Label(w)
res.pack()
w.mainloop()
