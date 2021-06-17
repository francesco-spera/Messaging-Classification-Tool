import sys
import main_training as m
import MC_training_support
import random as rd
from datetime import datetime
from tkinter import filedialog
from tkinter import *

import time

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


def vp_start_gui():
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    MC_training_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    training_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

def open_csv():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select a csv file", filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
    lab.delete(0, END)
    lab.insert(0, root.filename)


class Toplevel1:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x600+505+183")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("MC Tool Training")
        top.iconbitmap('molecularstructure_87618.ico')
        top.configure(background="#e3e3e1")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.047, rely=0.05, height=34, width=137)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(borderwidth="4")
        self.Button1.configure(command=open_csv)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Century Gothic} -size 11")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Open csv file''')

        self.TEntry1 = Entry(top)
        self.TEntry1.place(relx=0.308, rely=0.05, relheight=0.052
                , relwidth=0.443)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")
        global lab
        lab = self.TEntry1

        self.nn_set_label = tk.LabelFrame(top)
        self.nn_set_label.place(relx=0.032, rely=0.2, relheight=0.275
                , relwidth=0.892)
        self.nn_set_label.configure(relief='groove')
        self.nn_set_label.configure(font="-family {Century Gothic} -size 14")
        self.nn_set_label.configure(foreground="black")
        self.nn_set_label.configure(text='''Neural network settings''')
        self.nn_set_label.configure(background="#e3e3e1")

        self.hidd_lay_label = tk.Label(self.nn_set_label)
        self.hidd_lay_label.place(relx=0.034, rely=0.242, height=21, width=152
                , bordermode='ignore')
        self.hidd_lay_label.configure(background="#e3e3e1")
        self.hidd_lay_label.configure(disabledforeground="#a3a3a3")
        self.hidd_lay_label.configure(font="-family {Century Gothic} -size 10")
        self.hidd_lay_label.configure(foreground="#000000")
        self.hidd_lay_label.configure(text='''number of hidden layers''')

        self.hidd_nod_label = tk.Label(self.nn_set_label)
        self.hidd_nod_label.place(relx=0.034, rely=0.485, height=21, width=152
                , bordermode='ignore')
        self.hidd_nod_label.configure(activebackground="#f9f9f9")
        self.hidd_nod_label.configure(activeforeground="black")
        self.hidd_nod_label.configure(background="#e3e3e1")
        self.hidd_nod_label.configure(disabledforeground="#a3a3a3")
        self.hidd_nod_label.configure(font="-family {Century Gothic} -size 10")
        self.hidd_nod_label.configure(foreground="#000000")
        self.hidd_nod_label.configure(highlightbackground="#d9d9d9")
        self.hidd_nod_label.configure(highlightcolor="black")
        self.hidd_nod_label.configure(text='''number of hidden nodes''')

        self.epo_label = tk.Label(self.nn_set_label)
        self.epo_label.place(relx=0.034, rely=0.727, height=21, width=152
                , bordermode='ignore')
        self.epo_label.configure(activebackground="#f9f9f9")
        self.epo_label.configure(activeforeground="black")
        self.epo_label.configure(anchor='w')
        self.epo_label.configure(background="#e3e3e1")
        self.epo_label.configure(disabledforeground="#a3a3a3")
        self.epo_label.configure(font="-family {Century Gothic} -size 10")
        self.epo_label.configure(foreground="#000000")
        self.epo_label.configure(highlightbackground="#d9d9d9")
        self.epo_label.configure(highlightcolor="black")
        self.epo_label.configure(text='''number of epochs''')

        global h_layers, h_nodes, epochs

        self.TEntry2 = Entry(self.nn_set_label)
        self.TEntry2.place(relx=0.396, rely=0.242, relheight=0.127
                , relwidth=0.217, bordermode='ignore')
        self.TEntry2.configure(takefocus="")
        self.TEntry2.configure(cursor="ibeam")
        h_layers = self.TEntry2

        self.TEntry3 = ttk.Entry(self.nn_set_label)
        self.TEntry3.place(relx=0.396, rely=0.485, relheight=0.127
                , relwidth=0.217, bordermode='ignore')
        self.TEntry3.configure(takefocus="")
        self.TEntry3.configure(cursor="ibeam")
        h_nodes = self.TEntry3

        self.TEntry4 = ttk.Entry(self.nn_set_label)
        self.TEntry4.place(relx=0.396, rely=0.727, relheight=0.127
                , relwidth=0.217, bordermode='ignore')
        self.TEntry4.configure(takefocus="")
        self.TEntry4.configure(cursor="ibeam")
        epochs = self.TEntry4

        self.Button2 = tk.Button(self.nn_set_label)
        self.Button2.place(relx=0.748, rely=0.364, height=64, width=107
                , bordermode='ignore')
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(borderwidth="4")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Century Gothic} -size 11")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Confirm''')
        self.Button2.configure(command=self.train)

        self.log_label = tk.LabelFrame(top)
        self.log_label.place(relx=0.047, rely=0.55, relheight=0.408
                , relwidth=0.892)
        self.log_label.configure(relief='groove')
        self.log_label.configure(font="-family {Century Gothic} -size 14")
        self.log_label.configure(foreground="black")
        self.log_label.configure(text='''Log display''')
        self.log_label.configure(background="#e3e3e1")

        self.log_text = Label(self.log_label)
        self.log_text.place(relx=0.036, rely=0.168, height=171, width=444
                , bordermode='ignore')
        self.log_text.configure(anchor='nw')
        self.log_text.configure(background="#e3e3e1")
        self.log_text.configure(disabledforeground="#a3a3a3")
        self.log_text.configure(foreground="#000000")
        self.log_text.configure(text="WAITING TO TRAIN")
        self.log_text.configure(font="-family {Century Gothic} -size 11")

    def train(self):
        m.training(str(lab.get()), int(h_layers.get()), int(h_nodes.get()), int(epochs.get()))
        self.log_text['text'] = "THE NEURAL NETWORK IS DONE"


if __name__ == '__main__':
    vp_start_gui()
