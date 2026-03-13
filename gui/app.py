import tkinter as tk
from tkinter import ttk

from database.db import add

def run():
    root = tk.Tk()

    window =  ttk.Frame(root, padding=10)
    window.grid()

    ttk.Label(window, text="Instrument inventory").grid(column=0, row=0)
    root.geometry("800x600")

    name_label  = tk.StringVar()
    brand_label = tk.StringVar()
    category_label = tk.StringVar()
    condition_label = tk.StringVar()
    price_label = tk.StringVar()

    ttk.Label(window, text="Name").grid(column=0, row=1)
    ttk.Entry(window, textvariable=name_label).grid(column=1, row=1)

    ttk.Label(window, text="Brand").grid(column=0, row=2)
    ttk.Entry(window, textvariable=brand_label).grid(column=1, row=2)

    ttk.Label(window, text="Category").grid(column=0, row=3)
    ttk.Entry(window, textvariable=category_label).grid(column=1, row=3)

    ttk.Label(window, text="Condition").grid(column=0, row=4)
    ttk.Entry(window, textvariable=condition_label).grid(column=1, row=4)

    ttk.Label(window, text="Price").grid(column=0, row=5)
    ttk.Entry(window, textvariable=price_label).grid(column=1, row=5)

    def add_instrument():

        add(name_label.get(), brand_label.get(), category_label.get(), condition_label.get(), price_label.get())
        name_label.set("")
        brand_label.set("")
        category_label.set("")
        condition_label.set("")
        price_label.set("")

    ttk.Button(window, text="Add Instrument", command=add_instrument).grid(column=1, row=6)

    root.mainloop()
