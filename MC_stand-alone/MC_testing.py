import sys
import main_testing as m
import MC_testing_support
from tkinter import filedialog
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
    MC_testing_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    testing_support.init(w, top, *args, **kwargs)
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

        top.geometry("600x400+534+276")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("MC Tool Testing")
        top.configure(background="#e3e3e1")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.033, rely=0.075, height=34, width=137)
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

        self.TEntry1 = ttk.Entry(top)
        self.TEntry1.place(relx=0.283, rely=0.075, relheight=0.078
                , relwidth=0.46)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")
        global lab
        lab = self.TEntry1

        self.Button1_1 = tk.Button(top)
        self.Button1_1.place(relx=0.767, rely=0.075, height=34, width=107)
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#d9d9d9")
        self.Button1_1.configure(borderwidth="4")
        self.Button1_1.configure(command=self.test)
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font="-family {Century Gothic} -size 11")
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Confirm''')

        self.log_label = tk.LabelFrame(top)
        self.log_label.place(relx=0.033, rely=0.275, relheight=0.533
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
        self.log_text.configure(text="WAITING TO TEST")
        self.log_text.configure(font="-family {Century Gothic} -size 11")

        self.log_text1 = Label(self.log_label)
        self.log_text1.place(relx=0.036, rely=0.250, height=30, width=100
                            , bordermode='ignore')
        self.log_text1.configure(anchor='nw')
        self.log_text1.configure(background="#e3e3e1")
        self.log_text1.configure(disabledforeground="#a3a3a3")
        self.log_text1.configure(foreground="#000000")
        self.log_text1.configure(text="")
        self.log_text1.configure(font="-family {Century Gothic} -size 11")

        self.log_text2 = Label(self.log_label)
        self.log_text2.place(relx=0.036, rely=0.350, height=30, width=100
                             , bordermode='ignore')
        self.log_text2.configure(anchor='nw')
        self.log_text2.configure(background="#e3e3e1")
        self.log_text2.configure(disabledforeground="#a3a3a3")
        self.log_text2.configure(foreground="#000000")
        self.log_text2.configure(text="")
        self.log_text2.configure(font="-family {Century Gothic} -size 11")

        self.log_text3 = Label(self.log_label)
        self.log_text3.place(relx=0.036, rely=0.450, height=30, width=100
                             , bordermode='ignore')
        self.log_text3.configure(anchor='nw')
        self.log_text3.configure(background="#e3e3e1")
        self.log_text3.configure(disabledforeground="#a3a3a3")
        self.log_text3.configure(foreground="#000000")
        self.log_text3.configure(text="")
        self.log_text3.configure(font="-family {Century Gothic} -size 11")

        self.log_text4 = Label(self.log_label)
        self.log_text4.place(relx=0.036, rely=0.550, height=30, width=100
                             , bordermode='ignore')
        self.log_text4.configure(anchor='nw')
        self.log_text4.configure(background="#e3e3e1")
        self.log_text4.configure(disabledforeground="#a3a3a3")
        self.log_text4.configure(foreground="#000000")
        self.log_text4.configure(text="")
        self.log_text4.configure(font="-family {Century Gothic} -size 11")

        self.log_text5 = Label(self.log_label)
        self.log_text5.place(relx=0.036, rely=0.650, height=30, width=200
                             , bordermode='ignore')
        self.log_text5.configure(anchor='nw')
        self.log_text5.configure(background="#e3e3e1")
        self.log_text5.configure(disabledforeground="#a3a3a3")
        self.log_text5.configure(foreground="#000000")
        self.log_text5.configure(text="")
        self.log_text5.configure(font="-family {Century Gothic} -size 11")

        self.log_text6 = Label(self.log_label)
        self.log_text6.place(relx=0.036, rely=0.800, height=30, width=200
                             , bordermode='ignore')
        self.log_text6.configure(anchor='nw')
        self.log_text6.configure(background="#e3e3e1")
        self.log_text6.configure(disabledforeground="#a3a3a3")
        self.log_text6.configure(foreground="#000000")
        self.log_text6.configure(text="")
        self.log_text6.configure(font="-family {Century Gothic} -size 11")


    def test(self):
        a, f, i, v, u, len_csv = m.testing(str(lab.get()))
        self.log_text['text'] = 'Here is the estimate of the predictions:'
        self.log_text1['text'] = a
        self.log_text2['text'] = v
        self.log_text3['text'] = a
        self.log_text4['text'] = f
        self.log_text5['text'] = u
        self.log_text6['text'] = str(len_csv) + ' rows processed'


if __name__ == '__main__':
    vp_start_gui()
