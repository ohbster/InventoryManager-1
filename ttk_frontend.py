from tkinter import * 
from tkinter.ttk import *
from tkinter import ttk as ttk
import webbrowser
import Product
import Store
import Quantity
import ProductQuantity

class Dark_Theme(object):
    def __init__(self):                
        """
        Color scheme
        
        """
        self.bg_dark='#2f2f2f'
        self.bg_medium='#373737'
        self.fg_default='#ffffff'
        

class View(object):
    
    def __init__ (self, root=None, controller=None): #Pass the controller as an argument?
        
        if root is None:
            self.parent=Tk()
        else:
            self.parent = root
        
        win = self.parent
        
        """***********************
        MVC Stuff goes here
        
        ***********************
        """
        self.controller = controller
        #self.set_controller(controller)
        
        """
        ***********************
        Widget Style/Theme stuff goes here
        
        ***********************       
        
        """    
              
        common_theme = Dark_Theme()
        bg_dark = common_theme.bg_dark
        bg_medium = common_theme.bg_medium
        fg_default = common_theme.fg_default
        
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
        
        style.configure("Treeview",
            fieldbackground = bg_medium,
            foreground = fg_default,
            background = bg_medium
            )
        
        style.configure("Treeview.Heading",
            background = bg_medium,
            foreground = fg_default           
            )
    
    def set_controller(self, _controller):
        self.controller = _controller
    
    def callback(self, url):
        webbrowser.open_new_tab(url)
        
    def draw_main(self):
        
        common_theme = Dark_Theme()
        bg_dark = common_theme.bg_dark
        bg_medium = common_theme.bg_medium
        fg_default = common_theme.fg_default
        
        """
        ***********************************
        Create the menus
        ***********************************
        """
        win = self.parent
       
        
        win.title('Inventory Manager')
        win.geometry('600x200')
        
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
        
        
        """
        *********************************
        Create the tab
        *********************************
        """
        
        #create a frame to hold the tabs
        self.tab_frame = Frame(win)
        self.tab_frame.pack(fill='x')
        
        #TODO
        #StoreDialog(win,self.__controller).draw()
        #InventoryTab.draw(win, self.__controller)
        
         
        #code to draw all the tabs
        self.tab_control=ttk.Notebook(self.tab_frame)
        storeList = self.controller.get_stores() #Get a list of store objects, sourced from database
        
        
        #for every store in the Store table, create a seperate tab
        for store in storeList:
            InventoryTab(controller = self.controller, _parent = self.tab_frame,tab_control=self.tab_control,store=store)
            
            #the StoreTab object will use the 'store' object being passed to query the
            #Quantities and Product tables for data on each store respectively
            
        
        
        #InventoryTab(self.tab_frame,tab_control=self.tab_control,store=myStore)
        #InventoryTab(self.tab_control,myStore)

"""
Dialogs
"""
class StoreDialog(Tk):
    def __init__(self, parent, controller):
        
        __controller = controller
        self.__parent = parent

    #this needs to be in the main window, not here
    def draw(self):
        win = Tk()
        win.title("Select Store(s)")
        win.geometry('600x200')

    """
    Tabs
    """
    
#TODO: Change this to InventoryTab instead
class InventoryTab(object):
    def __init__(self,controller, _parent,tab_control, store):
        #controller is needed to interact with back end (update and retrieve database records, etc)
        self.controller = controller
        self.tab_frame = _parent
        
        #Store object will hold relevent info to the store tab
        self.tv =  None
        self.store = Store.Store()
        self.store = store
        self.draw_tab(tab_control=tab_control,store=store)
        #quantities = _parent.controller.get_quantities()
        quantities = self.controller.get_store_quantities(store.store_id)
        if len(quantities) < 1:
            print(f"No quantities found")
        else:
            #print(f"get_store_quantities output: product_id {quantities['1'].get_product_id} : quantity  = {quantities['1'].get_quantity}")
            print(f"get_store_quantities output: product_id = {quantities.get('1').get_product_id()}")
        
        
        #TODO: Also need a list of the relevent products (Join the Quantity and Products Table where Product.Product_ID = Quanity.Product_ID
        
        
    def get_store_id(self):
        return self.store.get_store_id()
    #tabs
    def draw(self, parent):
        self.__parent = parent
        
    #TODO: the notebook code belongs to the main window with the menues
    def draw_tab(self, tab_control=None, store = None):
        
        inventory_tab = ttk.Frame(tab_control)
        
        tab_control.add(inventory_tab,text=self.store.get_type())
        
        tab_control.pack(expand=1, fill='both',side=LEFT)
        
        #add a button to optionally add more tabs
        #add_tab_btn = ttk.Button(tab_frame, text="+")
        #add_tab_btn.pack()
        
        """
        Inventory Frame
        
        """
        header_frame = Frame(inventory_tab)
        header_frame.pack()
        
        
        inventory_frame = Frame(inventory_tab)
        inventory_frame.pack(side=LEFT)
        
        self.tv = ttk.Treeview(inventory_frame)
        self.tv['columns']=('Product ID', 'Name', 'Image', 'Description', 'MSRP', 'Quantity on Hand')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('Product ID', anchor=CENTER, width=80)
        self.tv.column('Name', anchor=CENTER, width=80)
        self.tv.column('Image', anchor=CENTER, width=80)
        self.tv.column('Description', anchor=CENTER, width=80)
        self.tv.column('MSRP', anchor=CENTER, width=80)
        self.tv.column('Quantity on Hand', anchor=CENTER, width=80)
        
        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('Product ID', text='Product ID', anchor=CENTER)
        self.tv.heading('Name', text='Name', anchor=CENTER)
        self.tv.heading('Image', text='Image', anchor=CENTER)
        self.tv.heading('Description', text='Description', anchor=CENTER)
        self.tv.heading('MSRP', text='MSRP', anchor=CENTER)
        self.tv.heading('Quantity on Hand', text='Quantity on Hand', anchor=CENTER)
        
        
        self.draw_inventory()
        self.tv.pack()
        
        
    
    def draw_inventory(self):
        
        #myPQ = ProductQuantity.ProductQuantity(1,"test", "test.jpg", "This is a test", 12.00,1, 20 )
        pq_list = self.controller.get_product_quantities(self.get_store_id())
        for myPQ in pq_list:
        
            self.tv.insert(parent='', index=0, iid=0, text='', values=(myPQ.get_product_id(),
                                                                myPQ.get_name(),
                                                                myPQ.get_image(),
                                                                myPQ.get_description(),
                                                                f'${myPQ.get_msrp():.2f}',
                                                                myPQ.get_quantity()
                                                                ))
        self.tv.pack()
        x=2
       
        
        
        
        """
        _style = ""
        _bg =  ""
        
        for x in range(_count):
            #alternate between a dark and light color to make the list easier to read
            
            if x % 2 != 0:
                _style = "dark.TFrame"
                _bg = self.bg_dark
                
                
            else :
               _style = "TFrame"
               _bg = self.bg_medium
            
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
    
    #draw_inventory(10)"""
    def draw_lineitem(self,parent=None,quantity=None):
        ""
    
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

           