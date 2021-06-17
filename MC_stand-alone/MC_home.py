import sys
import MC_home_support
import MC_training as tr
import MC_testing as ts
from tkinter import *

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
    MC_home_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    menu_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

def start_train():
    tr.vp_start_gui()

def start_test():
    ts.vp_start_gui()


class Toplevel1:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x600+660+210")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("MC Tool GUI")
        top.iconbitmap('molecularstructure_87618.ico')
        top.configure(background="#e3e3e1")
        top.configure(cursor="arrow")

        self.title = tk.Label(top)
        self.title.place(relx=0.3, rely=0.017, height=51, width=224)
        self.title.configure(background="#e3e3e1")
        self.title.configure(disabledforeground="#a3a3a3")
        self.title.configure(font="-family {Century Gothic} -size 24 -weight bold")
        self.title.configure(foreground="#000000")
        self.title.configure(text='''MC TOOL''')

        self.subtitle = tk.Label(top)
        self.subtitle.place(relx=0.217, rely=0.083, height=61, width=324)
        self.subtitle.configure(background="#e3e3e1")
        self.subtitle.configure(disabledforeground="#a3a3a3")
        self.subtitle.configure(font="-family {Century Gothic} -size 15")
        self.subtitle.configure(foreground="#000000")
        self.subtitle.configure(text='''Messaging Classification Tool''')

        self.feat_label = tk.LabelFrame(top)
        self.feat_label.place(relx=0.683, rely=0.233, relheight=0.375, relwidth=0.267)
        self.feat_label.configure(relief='groove')
        self.feat_label.configure(borderwidth="3")
        self.feat_label.configure(font="-family {Century Gothic} -size 14")
        self.feat_label.configure(foreground="black")
        self.feat_label.configure(text='''Features''')
        self.feat_label.configure(background="#e3e3e1")
        self.feat_label.configure(cursor="arrow")
        self.feat_label.configure(highlightbackground="#008080")

        self.train_button = tk.Button(self.feat_label)
        self.train_button.place(relx=0.188, rely=0.267, height=44, width=97
                , bordermode='ignore')
        self.train_button.configure(activebackground="#ececec")
        self.train_button.configure(activeforeground="#000000")
        self.train_button.configure(background="#d9d9d9")
        self.train_button.configure(borderwidth="4")
        self.train_button.configure(disabledforeground="#a3a3a3")
        self.train_button.configure(font="-family {Century Gothic} -size 11")
        self.train_button.configure(foreground="#000000")
        self.train_button.configure(highlightbackground="#000000")
        self.train_button.configure(highlightcolor="#ffffff")
        self.train_button.configure(highlightthickness="3")
        self.train_button.configure(pady="0")
        self.train_button.configure(text='''Training''')
        self.train_button.configure(command=start_train)

        self.test_button = tk.Button(self.feat_label)
        self.test_button.place(relx=0.188, rely=0.622, height=44, width=97
                , bordermode='ignore')
        self.test_button.configure(activebackground="#ececec")
        self.test_button.configure(activeforeground="#000000")
        self.test_button.configure(background="#d9d9d9")
        self.test_button.configure(borderwidth="4")
        self.test_button.configure(disabledforeground="#a3a3a3")
        self.test_button.configure(font="-family {Century Gothic} -size 11")
        self.test_button.configure(foreground="#000000")
        self.test_button.configure(highlightbackground="#d9d9d9")
        self.test_button.configure(highlightcolor="black")
        self.test_button.configure(pady="0")
        self.test_button.configure(text='''Testing''')
        self.test_button.configure(command=start_test)

        self.about_label = tk.LabelFrame(top)
        self.about_label.place(relx=0.033, rely=0.767, relheight=0.208
                , relwidth=0.917)
        self.about_label.configure(relief='groove')
        self.about_label.configure(font="-family {Century Gothic} -size 14")
        self.about_label.configure(foreground="black")
        self.about_label.configure(text='''About''')
        self.about_label.configure(background="#e3e3e1")

        self.txt_ab_1 = tk.Label(self.about_label)
        self.txt_ab_1.place(relx=0.018, rely=0.24, height=25, width=205
                , bordermode='ignore')
        self.txt_ab_1.configure(activebackground="#f0f0f0f0f0f0")
        self.txt_ab_1.configure(activeforeground="#000000")
        self.txt_ab_1.configure(anchor='w')
        self.txt_ab_1.configure(background="#e3e3e1")
        self.txt_ab_1.configure(disabledforeground="#a3a3a3")
        self.txt_ab_1.configure(font="-family {Century Gothic} -size 10")
        self.txt_ab_1.configure(foreground="#000000")
        self.txt_ab_1.configure(text='''Messaging Classification Tool''')

        self.txt_ab_2 = tk.Label(self.about_label)
        self.txt_ab_2.place(relx=0.018, rely=0.4, height=25, width=205
                , bordermode='ignore')
        self.txt_ab_2.configure(activebackground="#f0f0f0f0f0f0")
        self.txt_ab_2.configure(activeforeground="#000000")
        self.txt_ab_2.configure(anchor='w')
        self.txt_ab_2.configure(background="#e3e3e1")
        self.txt_ab_2.configure(disabledforeground="#a3a3a3")
        self.txt_ab_2.configure(font="-family {Century Gothic} -size 10")
        self.txt_ab_2.configure(foreground="#000000")
        self.txt_ab_2.configure(highlightbackground="#d9d9d9")
        self.txt_ab_2.configure(highlightcolor="black")
        self.txt_ab_2.configure(text='''Version 1.1.1''')

        self.txt_ab_3 = tk.Label(self.about_label)
        self.txt_ab_3.place(relx=0.018, rely=0.56, height=25, width=205
                , bordermode='ignore')
        self.txt_ab_3.configure(activebackground="#f0f0f0f0f0f0")
        self.txt_ab_3.configure(activeforeground="#000000")
        self.txt_ab_3.configure(anchor='w')
        self.txt_ab_3.configure(background="#e3e3e1")
        self.txt_ab_3.configure(disabledforeground="#a3a3a3")
        self.txt_ab_3.configure(font="-family {Century Gothic} -size 10")
        self.txt_ab_3.configure(foreground="#000000")
        self.txt_ab_3.configure(highlightbackground="#d9d9d9")
        self.txt_ab_3.configure(highlightcolor="black")
        self.txt_ab_3.configure(text='''Università degli studi di Salerno''')

        self.txt_ab_4 = tk.Label(self.about_label)
        self.txt_ab_4.place(relx=0.018, rely=0.72, height=21, width=205
                , bordermode='ignore')
        self.txt_ab_4.configure(activebackground="#f0f0f0f0f0f0")
        self.txt_ab_4.configure(activeforeground="#000000")
        self.txt_ab_4.configure(anchor='w')
        self.txt_ab_4.configure(background="#e3e3e1")
        self.txt_ab_4.configure(disabledforeground="#a3a3a3")
        self.txt_ab_4.configure(font="-family {Century Gothic} -size 10")
        self.txt_ab_4.configure(foreground="#000000")
        self.txt_ab_4.configure(highlightbackground="#d9d9d9")
        self.txt_ab_4.configure(highlightcolor="black")
        self.txt_ab_4.configure(text='''Salerno, Italia''')


if __name__ == '__main__':
    vp_start_gui()
