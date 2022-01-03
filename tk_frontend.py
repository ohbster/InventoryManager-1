from tkinter import *
from tkinter import ttk
import webbrowser
from caca.common import COLOR_TRANSPARENT


def callback(url):
    webbrowser.open_new_tab(url)

#set a transparent color


win=Tk()

win.title('Inventory Manager')
win.geometry('600x200')


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
tab_frame = Frame(win,bg='black')
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
qoh_labels.append(Label(qoh_frame, text='Product ID').grid(row=1, column=1, pady=1))
qoh_labels.append(Label(qoh_frame, text='Name').grid(row=1, column=2))
qoh_labels.append(Label(qoh_frame, text='Image').grid(row=1, column=3))
qoh_labels.append(Label(qoh_frame, text='Description').grid(row=1, column=4))
qoh_labels.append(Label(qoh_frame, text='MSRP').grid(row=1, column=5))




#Product ID frame
qoh_labels.append(Label(qoh_frame, text=product_list['Product_ID']).grid(row=2, column=1))
#Product Name frame
qoh_labels.append(Label(qoh_frame, width=20, fg='blue', text=product_list['Name'], cursor='hand2' ))
# [-1] is last item in list
qoh_labels[-1].grid(row=2, column=2)
qoh_labels[-1].bind("<Button-1>", lambda e:
              callback("http://clean.jewelry"))
#Image
qoh_labels.append(Label(qoh_frame, text=product_list['Image']).grid(row=2, column=3))
#Description
qoh_labels.append(Label(qoh_frame, text=product_list['Description']).grid(padx=5, row=2,column=4))
#MSRP
qoh_labels.append(Label(qoh_frame, text=f"${product_list['MSRP']:.2f}").grid(row=2, column=5))

"""
TODO: Consider using labelFrame in order to highlight each row to make it easier
to read
"""

"""
Create a color scheme for the rows of the table
Alternate between light and dark to make it easier to read
Have a Light and Dark warning color
And a Light and Dark alert color
Alternate between odd and even rows on the table.

"""

win.mainloop()
           