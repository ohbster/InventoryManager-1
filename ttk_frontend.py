from tkinter import * 
from tkinter.ttk import *
from tkinter import ttk as ttk
import webbrowser
from scripts.objgraph import flat



def callback(url):
    webbrowser.open_new_tab(url)

#set a transparent color

"""
Color scheme

"""
bg_dark='#2f2f2f'
bg_medium='#373737'
fg_default='#ffffff'


#fg=fg_default, style=_style, relief=FLAT, bd=0, height=1, 
#width=15, highlightthickness=0

win=Tk()

win.title('Inventory Manager')
win.geometry('600x200')


style = ttk.Style(win)
style.configure("TEntry",
    foreground = fg_default, 
    fieldbackground = bg_medium
    )

style.configure("TLabel",
    foreground = fg_default,
    background = bg_medium
    )

style.configure("TLabelFrame",
    foreground = fg_default,
    background = bg_medium,
    bordercolor = bg_medium,
    borderwidth = 0,
    labelmargins = 0,
    labeloutside = False,
    #height = 10,
    relief = FLAT
    
    )
style.configure("dark.TFrame",
    background = bg_dark
    
    )

style.configure("TNotebook",
    background = bg_medium,
    
    lightcolor = bg_medium
    #darkcolor = bg_dark,
    #bordercolor = bg_medium,
    #foreground = bg_medium
    #tabposition='sw'
    )
style.configure("TNotebook.Tab",
   foreground = fg_default,
   background = bg_medium,
   bordercolor = bg_medium
   )

style.configure("TFrame", 
    background = bg_medium)


#Enable transparency (system dependent)
"""
Windows
"""
#win.wm_attributes("-transparentcolor",'grey')

"""
Mac
"""
#wint.wm_attributes("-transparent", True)

"""
Linux
"""

mn = Menu(win)
win.config(menu=mn)
#win.configure(bg=bg_medium)

win.tk_setPalette(background=bg_medium, foreground=fg_default, activeBackground=bg_dark, activeForeground=fg_default)
        
#Draw Menus        
file_menu = Menu(mn, tearoff = 0)

mn.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New')
file_menu.add_command(label='Save')
file_menu.add_command(label='Refresh')
file_menu.add_separator()
file_menu.add_command(label='Exit')

tabs_menu = Menu(mn, tearoff = 0)
mn.add_cascade(label='Tab', menu=tabs_menu)
tabs_menu.add_command(label='New Tab')
tabs_menu.add_command(label='Close Tab')

help_menu=Menu(mn, tearoff = 0)
mn.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='Feedback')
help_menu.add_command(label='Contact')

#create a frame to hold the tabs
tab_frame = Frame(win)
tab_frame.pack(fill='x')

"""
Tabs
"""

#tabs
tab_control=ttk.Notebook(tab_frame)
inventory_tab = ttk.Frame(tab_control)
amazon_tab = ttk.Frame(tab_control)
etsy_tab = ttk.Frame(tab_control)

tab_control.add(inventory_tab,text='Inventory')
tab_control.add(amazon_tab,text='Amazon Inventory')
tab_control.add(etsy_tab,text='Etsy Inventory')

tab_control.pack(expand=1, fill='both',side=LEFT)

#add a button to optionally add more tabs
#add_tab_btn = ttk.Button(tab_frame, text="+")
#add_tab_btn.pack()

"""
Quantity on Hand Frame

"""

product_list = dict()
product_list['Product_ID'] = 1
product_list['Name'] = 'ankh'
product_list['Image'] = 'ankh.jpg'
product_list['Description'] = "This is a 25mm ankh piece"
product_list['MSRP'] = 12.00

qoh_frame = Frame(inventory_tab)
qoh_frame.pack(side=LEFT)

qoh_labels = list()
"""
Legend

"""

"""
qoh_labels.append(Label(qoh_frame, text='Product ID').grid(row=1, column=1, pady=1))
qoh_labels.append(Label(qoh_frame, text='Name').grid(row=1, column=2))
qoh_labels.append(Label(qoh_frame, text='Image').grid(row=1, column=3))
qoh_labels.append(Label(qoh_frame, text='Description').grid(row=1, column=4))
qoh_labels.append(Label(qoh_frame, text='MSRP').grid(row=1, column=5))
"""

#2
def draw_rows(_count):
    x=2
    
    _style = ""
    _bg =  ""
    for x in range(_count):
        #alternate between a dark and light color to make the list easier to read
        
        if x % 2 != 0:
            _style = "dark.TFrame"
            _bg = bg_dark
            
            
        else :
           _style = "TFrame"
           _bg = bg_medium
        
        #print(_style)
        qoh_labels.append(Frame(qoh_frame, style=_style))
        qoh_labels[-1].grid(row=x, column=1, columnspan = 5)
        #qoh_labels[-1].grid_propagate(0)
        
        text1 = Text(qoh_labels[-1], bg=_bg, height=1, bd=0, width=15, highlightthickness=0)
        text1.grid(row=x,column=1, ipadx=5, padx=0)
        text1.insert(0.0, x)
        text1["state"] = DISABLED
        
        text2 = Text(qoh_labels[-1], bg=_bg, height=1, bd=0, width=15, highlightthickness=0)
        text2.grid(row=x,column=2, ipadx=5, padx=0)
        text2.insert(0.0, 'field 2')
        text2["state"] = DISABLED
        
        text3 = Text(qoh_labels[-1], bg=_bg, height=1, bd=0, width=15, highlightthickness=0)
        text3.grid(row=x,column=3, ipadx=5, padx=0)
        text3.insert(0.0, 'field 3')
        text3["state"] = DISABLED
        
        text4 = Text(qoh_labels[-1], bg=_bg, height=1, bd=0, width=15, highlightthickness=0)
        text4.grid(row=x,column=4, ipadx=5, padx=0)
        text4.insert(0.0, 'field 4')
        text4["state"] = DISABLED
        
        text5 = Entry(qoh_labels[-1],  width=15)
        text5.grid(row=x,column=5, ipadx=5, padx=0)
        text5.insert(INSERT,'field 5')
        #text5["state"] = DISABLED
        
        print(qoh_labels[-1].winfo_children())

draw_rows(10)

"""
TODO: Consider using labelFrame in order to highlight each row to make it easier
to read
"""

"""
Create a color scheme for the rows of the table
Alternate between light and bg_dark to make it easier to read
Have a Light and Dark warning color
And a Light and Dark alert color
Alternate between odd and even rows on the table.

"""

win.mainloop()
           