from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import glob
import os

path = os.getcwd()
files = glob.glob(f'{path}/*.txt')

window = Tk()
window.title("App")

frame = Frame(window)
frame.grid(column=0, row=1)

heading = Label(window, text="Type data to find: ")
heading.grid(column=0, row=0)

type_data = Entry(window, width=20)
type_data.grid(column=1, row=0)

labels = []


def create_label(text, row):
    label = Label(frame, text=text)
    label.grid(column=0, row=row)
    labels.append(label)


def remove_labels():
    for i in labels:
        i.destroy()


def find_data_button():
    remove_labels()
    ask = type_data.get()
    if ask != "":
        result = []
        for file in files:
            with open(file, 'r+') as f:
                line_number = 0
                for line in f:
                    line_number += 1
                    if ask in line:
                        index = line.find(ask)
                        result.append(f"File name: '{file}', Line number: {line_number}, Index: {index}")
                        number_of_row = 1
                        for data in result:
                            create_label(data, number_of_row)
                            number_of_row += 1


button = Button(window, text="Find", command=find_data_button())
button.grid(column=3, row=0)
button.config(command=find_data_button)

window.mainloop()
