##IMPORTANT FUNCTION##
##organizes files to ensure that the same contract is being assessed over time
import os
import pandas as pd

def SrContract(tikr,pdate,con):
    trkr_date = []
    trkr_return = []
    tikr = str(tikr)
    con = str(con)
    for i in range(len(pdate)):

        path = tikr+'/Oct_'+str(pdate[i])+'_2017'
        f = os.listdir(path)

        for j in range(len(f)):
            rd = pd.read_csv(path+'/'+f[j]);
            x = pd.Series(rd.iloc[:,0]);
            for l in range(len(x)):
                if str(x[l]) == con:
                    trkr_date = trkr_date + [pdate[i]]
                    trkr_return = trkr_return + [rd.loc[l,'return']] # output goes - download date, [index,epire date]

    return [trkr_date,trkr_return]

##---##

###IMPORTANT FUNCTION###
##import calls##
import matplotlib
matplotlib.use('TkAgg')
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler

from matplotlib.figure import Figure
import sys
from tkinter import *
import tkinter as Tk
import os
import pandas as pd
##finish import calls##

##contract parameters##
pdate = [14, 16, 17, 18, 19, 20, 23, 24, 25, 30, 31]
##finished contract parameters##

root = Tk.Tk()

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 60, padx = 60)

# Create Tkinter variables
tkvar = StringVar(root)
tkvar2 = StringVar(root)
tkvar3 = StringVar(root)

# List with options
choices2 = ['BAC','BUD','F','NFLX','T']
tkvar2.set(choices2[0]) # set the default option

popupMenu2 = OptionMenu(mainframe, tkvar2, *choices2)
Label(mainframe, text="Choose a stock symbol").grid(row = 24, column = 3)
popupMenu2.grid(row = 25, column =3)

###figure plot info
f = Figure(figsize=(10, 4), dpi=100)
a = f.add_subplot(111)

# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)


def on_key_event(event):
    print('you pressed %s' % event.key)
    key_press_handler(event, canvas, toolbar)

canvas.mpl_connect('key_press_event', on_key_event)


#on change of stock ticker dropdown value
def change_dropdown2(*args):
    a.cla()
    tikr = tkvar2.get()
    path0 = tikr+'/Oct_'+str(pdate[0])+'_2017'
    f0 = os.listdir(path0)

    tkvar3.set('') # set the default option
    popupMenu3 = OptionMenu(mainframe, tkvar3, *f0)
    Label(mainframe, text="Choose an exp.date").grid(row = 14, column = 5)#new
    popupMenu3.grid(row = 15, column =5)


# link function to change dropdown
tkvar2.trace('w', change_dropdown2)

#on change of expiration date dropdown value
def change_dropdown3(*args):
    if tkvar3.get()!='':
        tikr = tkvar2.get()

        path0 = tikr+'/Oct_'+str(pdate[0])+'_2017'
        f0 = os.listdir(path0)

        exp_choice = tkvar3.get()
        exp_val = f0.index(exp_choice)
        rd0 = pd.read_csv(path0+'/'+f0[exp_val]);
        con = rd0.iloc[:,0].values.tolist()
        tkvar.set('') # set the default option
        popupMenu = OptionMenu(mainframe, tkvar, *con)
        Label(mainframe, text="Choose a contract").grid(row = 14, column = 1)
        popupMenu.grid(row = 15, column =1)

# link function to change dropdown
tkvar3.trace('w', change_dropdown3)

# on change contract dropdown value
def change_dropdown(*args):
    con_choice = tkvar.get()
    con_choice2 = tkvar2.get()
    trial = SrContract(con_choice2,pdate,con_choice)
    a.plot(trial[0],trial[1],'^-', label = str(con_choice))
    a.set_xlabel('date')
    a.set_ylabel('return')
    a.legend()
    canvas.show()

# link function to change dropdown
tkvar.trace('w', change_dropdown)

def _clear_canvas():
    a.cla()
    tkvar.set('')
    tkvar2.set('')
    tkvar3.set('')

button2 = Tk.Button(master=root, text = 'clear fig', command=_clear_canvas)
button2.pack(side=Tk.RIGHT)

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

button = Tk.Button(master=root, text='Quit', command=_quit)
button.pack(side=Tk.BOTTOM)

Tk.mainloop()

#parts of code adapted from https://matplotlib.org/examples/user_interfaces/embedding_in_tk.html
#and https://pythonspot.com/en/tk-dropdown-example/