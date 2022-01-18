from tkinter import * 
from tkinter.ttk import *
from tkinter import ttk as ttk
import webbrowser
from Product import Product
from Store import Store
from Quantity import Quantity
from ProductQuantity import ProductQuantity
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter.messagebox import showwarning




class Dark_Theme(object):
    def __init__(self):                
        """
        Color scheme
        
        """
        self.bg_light='#767676'
        self.bg_dark='#2f2f2f'
        self.bg_medium='#373737'
        self.fg_default='#dddddd'
       
        

class View(object):
    
    def __init__ (self, root=None, controller=None): #Pass the controller as an argument?
        
        if root is None:
            self.parent=Tk()
        else:
            self.parent = root
        
        win = self.parent
        
        """******************
        DISCLAIMER
        
        *********************
        """
        showwarning(title = 'Disclaimer', message = "This program is under development. It is incomplete, buggy, experimental" 
        + " and is not intended for use in a real business scenario. Many things are missing or broken. "
        + " Not meant for production purpose. Only meant for peer review. Any feedback is appreciated, ohbster@protonmail.com")
        
        
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
        bg_light = common_theme.bg_light
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
            
            lightcolor = bg_medium,
            darkcolor = bg_dark,
            bordercolor = bg_medium
            #foreground = bg_medium
            #tabposition='sw'
            )
        style.configure("TNotebook.Tab",
           foreground = fg_default,
           background = bg_medium,
           bordercolor = bg_medium
           )
        
        style.configure("TFrame", 
            background = bg_medium
            )
        
        style.configure("TRadiobutton",
                        background = bg_medium,
                        foreground = fg_default,
                        focuscolor = bg_dark)
        
        style.configure("Treeview",
            fieldbackground = bg_medium,
            foreground = fg_default,
            background = bg_medium
            )
        
        style.configure("Treeview.Heading",
            background = bg_medium,
            foreground = fg_default           
            )
        
        style.configure("Vertical.TScrollbar", 
                        troughcolor = bg_medium,
                        background = bg_medium,
                        bordercolor = bg_medium
                        )
        style.configure("TButton",
                        background = bg_medium,
                        foreground = fg_default
                        #lightcolor = bg_light,
                        #darkcolor = bg_dark,
                        #focuscolor = bg_light
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
        win.geometry('800x300')
        
        mn = Menu(win)
        win.config(menu=mn)
        
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
        self.store = Store()
        self.store = store
        self.draw_tab(tab_control=tab_control,store=store)
        #quantities = _parent.controller.get_quantities()
        #quantities = self.controller.get_store_quantities(store.store_id)        
        
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
        
        """*****************
        Inventory Frame
        
        ********************
        """

        inventory_frame = Frame(inventory_tab)
        inventory_frame.grid_columnconfigure(0, weight=1)
        inventory_frame.grid_rowconfigure(0, weight=1)
        inventory_frame.grid(row=0, column=0)
        
        """
        Treeview that displays all inventory information for current store
        
        """
        
        self.tv = ttk.Treeview(inventory_frame, selectmode = 'browse')
        self.tv['columns']=('Product ID', 'Name', 'Image', 'Description', 'MSRP', 'Quantity on Hand')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('Product ID', anchor=CENTER, width=70)
        self.tv.column('Name', anchor=CENTER, width=120)
        self.tv.column('Image', anchor=CENTER, width=120)
        self.tv.column('Description', anchor=CENTER, width=170)
        self.tv.column('MSRP', anchor=CENTER, width=60)
        self.tv.column('Quantity on Hand', anchor=CENTER, width=60)
        
        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('Product ID', text='Product ID', anchor=CENTER)
        self.tv.heading('Name', text='Name', anchor=CENTER)
        self.tv.heading('Image', text='Image', anchor=CENTER)
        self.tv.heading('Description', text='Description', anchor=CENTER)
        self.tv.heading('MSRP', text='MSRP', anchor=CENTER)
        self.tv.heading('Quantity on Hand', text='Quantity', anchor=CENTER)

        
        #The below function will populate the treeview with info from the database
        self.draw_inventory()
        
        self.tv.grid(row=0, column=0, sticky='ew')
        
        
        #Vertical scroll bar to the side
        scrollbar_v = ttk.Scrollbar(inventory_frame, orient='vertical', command=self.tv.yview)
        scrollbar_v.grid(row=0, column=1, sticky='ns')
        
        #assign the scroll bar to the treeview
        self.tv['yscrollcommand'] = scrollbar_v.set
        
        
        """
        Right Side Panel
        where the action buttons are going
        
        """
        panel_frame = ttk.Frame(inventory_frame)
        panel_frame.grid(row=0, column=2, sticky='ns')
        
        """
        Buttons
        """
        
        #used to create a new product and add to inventory
        new_btn = Button(panel_frame, text = 'New Product', width=15)
        #new_btn.grid(row=0, column=2)
        new_btn.bind("<Button>", lambda e:  self.openNewWindow(inventory_tab))
        new_btn.pack(ipadx = 7)
        
        #used to add a product to current inventory
        add_btn = Button(panel_frame, text = 'Add Inventory', width = 15)
        add_btn.bind('<Button>', lambda e: self.openAddWindow(inventory_tab))
        
        add_btn.pack(ipadx = 7)
        
        #Update the quantity of selected product
        update_btn = Button(panel_frame, text = 'Update', width=15)
        update_btn.bind('<Button>', lambda e: self.openUpdateWindow(inventory_tab))
        update_btn.pack(ipadx = 7)
        
        #Redraw the inventory_frame
        refresh_btn = Button(panel_frame, text = 'Refresh', width=15)
        #refresh_btn.bind('<Button>', lambda e: self.openInProgress(inventory_tab))
        refresh_btn.bind('<Button>', lambda e: self.redraw())
        refresh_btn.pack(ipadx = 7)    

    def draw_inventory(self):
        #create a list of ProductQuantity objects, holding data from Product table and Quantity table
        pq_list = self.controller.get_product_quantities(self.get_store_id())
        
        i = 0
        for myPQ in pq_list:
        
            self.tv.insert(parent='', index=0, iid=i, text='', values=(myPQ.get_product_id(),
                                                                myPQ.get_name(),
                                                                myPQ.get_image(),
                                                                myPQ.get_description(),
                                                                f'${myPQ.get_msrp():.2f}',
                                                                myPQ.get_quantity()
                                                                ))
            i += 1
        #self.tv.grid(row=1, column=0, sticky='ns')
    
    

        
    
    def openNewWindow(self, parent):
        newWindow = Toplevel(parent)
        newWindow.title("Add a new product")
        newWindow.geometry("500x200")
        
        #parameter for spacing out widgets
        field_width = 30
        
        def open_image():
            filetypes = (
                ('jpeg files', '*.jpg'),
                ('gif files', '*.gif'),
                ('All files', '*Allfile*')
            )
            filename = fd.askopenfilename(
                title = 'open image',
                filetypes = filetypes
                )
            print(filename)
            image_entry.insert(INSERT, filename)
            
        def submit():
            #store the data to a new ProductQuantity object, and tell let 
            #the object do the hard work of sanitizing and adding
            
            #check that all the fields are valid before creating an object
            
            pq = ProductQuantity(product_id = pid_entry.get(),
                                 name = name_entry.get(),
                                 image = image_entry.get(),
                                 description = description_entry.get(),
                                 msrp = msrp_entry.get(),
                                 store_id = self.get_store_id(), #The store id belongs to the current Tab
                                 quantity = quantity_entry.get()
                                 )
            self.controller.add_product_quantity(pq)
            self.redraw()
            newWindow.destroy()
            
            #print(pid_entry.get())
        
        pid_label = Label(newWindow, text = 'Enter Product ID')
        pid_label.grid(row = 0, column = 0)
        
        pid_entry = Entry(newWindow, width = field_width)
        pid_entry.grid(row = 0, column = 1)
        
        name_label = Label(newWindow, text = 'Enter Name')
        name_label.grid(row = 1, column = 0)
        
        name_entry = Entry(newWindow, width = field_width)
        name_entry.grid(row = 1, column = 1)
        
        description_label = Label(newWindow, text = 'Enter a short description')
        description_label.grid(row = 2, column = 0)
        
        description_entry = Entry(newWindow, width = field_width)
        description_entry.grid(row = 2, column = 1)
        
        msrp_label = Label(newWindow, text = 'MSRP')
        msrp_label.grid(row = 3, column = 0)
        
        msrp_entry = Entry(newWindow, width = field_width)
        msrp_entry.grid(row = 3, column = 1)
        
        quantity_label = Label(newWindow, text = 'Enter Quantity')
        quantity_label.grid(row = 4, column = 0)
        
        quantity_entry = Entry(newWindow, width = field_width)
        quantity_entry.grid(row = 4, column = 1)
        
        image_label = Label(newWindow, text = 'Select Product Image')
        image_label.grid(row = 5, column = 0)
        
        image_entry = Entry(newWindow, width = field_width)
        image_entry.grid(row = 5, column = 1)
        
        image_btn = Button(newWindow, text = 'Open Image', command=open_image)
        image_btn.grid(row = 5, column = 2)
        
        submit_btn = Button(newWindow, text = 'Submit')
        
        #submit_btn.bind('<Return>', lambda e: self.submit())
        submit_btn.bind('<Button>', lambda e: submit())
        submit_btn.grid(row = 6, column = 1)


    """ 
    List all available products in the Products table and allow user to add some to their inventory
    If item is already in inventory, add to it
    """
    def openAddWindow(self, parent):
        addWindow = Toplevel(parent)
        addWindow.title('Add to Inventory')
        addWindow.geometry('700x300')

        def submit():
            value = quantity_entry.get()
            selected_item = product_tv.focus()

            if value.isdigit() and int(value)>0:
                product_id = product_tv.item(selected_item)['values'][0]
                self.controller.add_quantity(product_id, self.get_store_id(), int(value))
                self.redraw()
                addWindow.destroy()
            else:
                showwarning(title='Invalid Input', message="Enter a positive integer value")


        """
        Product Treeview
        """

        product_tv = ttk.Treeview(addWindow, selectmode = 'browse')
        product_tv['columns']=('Product ID', 'Name', 'Image', 'Description', 'MSRP')
        product_tv.column('#0', width=0, stretch=NO)
        product_tv.column('Product ID', anchor=CENTER, width=70)
        product_tv.column('Name', anchor=CENTER, width=120)
        product_tv.column('Image', anchor=CENTER, width=120)
        product_tv.column('Description', anchor=CENTER, width=170)
        product_tv.column('MSRP', anchor=CENTER, width=60)

        product_tv.heading('#0', text='', anchor=CENTER)
        product_tv.heading('Product ID', text='Product ID', anchor=CENTER)
        product_tv.heading('Name', text='Name', anchor=CENTER)
        product_tv.heading('Image', text='Image', anchor=CENTER)
        product_tv.heading('Description', text='Description', anchor=CENTER)
        product_tv.heading('MSRP', text='MSRP', anchor=CENTER)

        product_list = self.controller.get_unlisted_products(self.get_store_id())
        #product_list = self.controller.get_products()

        
        i = 0
        for product in product_list:
        
            product_tv.insert(parent='', index=0, iid=i, text='', values=(product.get_product_id(),
                                                                product.get_name(),
                                                                product.get_image(),
                                                                product.get_description(),
                                                                f'${product.get_msrp():.2f}' 
                                                                ))
            i += 1

        
        product_tv.grid(row = 0, column =0, sticky = 'ew')

        #Vertical scroll bar to the side
        scrollbar_v = ttk.Scrollbar(addWindow, orient='vertical', command=product_tv.yview)
        scrollbar_v.grid(row=0, column=1, sticky='ns')
        
        #assign the scroll bar to the treeview
        product_tv['yscrollcommand'] = scrollbar_v.set

        """
        Entry
        """
        quantity_label = Label(addWindow, text = "How many do you want to add into inventory?")
        quantity_label.grid(row = 1, column =0)

        quantity_entry = Entry(addWindow, width = 15)
        quantity_entry.grid(row = 2, column = 0)

        submit_btn = Button(addWindow, text = 'Submit', width = 15, command = submit)
        submit_btn.grid(row = 3, column = 0)



        addWindow.transient(parent)
        


        
    def openUpdateWindow(self, parent):
        updateWindow = Toplevel(parent)
        updateWindow.geometry('400x250')
        updateWindow.resizable(False, False)
        updateWindow.title('Add or Remove')
        #updateWindow.attributes('-topmost', 1)
        selected_item = self.tv.focus()
        
        def show_selected():
            showinfo(
                title='Result',
                message = selected_action.get())
            
        def submit():
            """
            1.)check if value in entry field is a positive integer.
            if no: prompt user to enter valid input
            if yes: proceed
            2.)get the current value of Quantity.quantity for Product_ID and Store_ID
            controller.get_quantity(product_id, store_id).get_quantity()
            
            3.)check the value of selected_action. 
            if 'R' for receive: do set_quantity(product_id, store_id, (current quantity + entry value))
            if 'S' for ship: check if entry value is greater than current value. If so, prompt user 
            that there is not enough inventor and to enter a new value.
            if not greater, do set_quantity(product_id, store_id, (current quantity - entry value))
            
            4.)Redraw and destroy updateWindow
            
            
            """
            
            if ( (entry.get().isdigit())):
                if (int(entry.get()) > 0):
                    #show_selected()
                    #valid input has been given
                    print(self.tv.item(selected_item))
                    
                    #get the quantity from the user entered number
                    update_value = int(entry.get())
                    #get product id from currently selected item
                    product_id = self.tv.item(selected_item)['values'][0]
                    
                    #get the current quantity from database (in case something has changed)
                    cur_value = self.controller.get_quantity(product_id, self.get_store_id()).get_quantity()
                    
                    
                    #check radio button selection
                    if selected_action.get() == 'R':
                        new_value = cur_value + update_value
                        #tell the controller to update this record in the database with new value
                        self.controller.set_quantity(product_id, self.get_store_id(), new_value)
                        #refresh the treeview and close the update window
                        self.redraw()
                        updateWindow.destroy()
                        #print(f'New quantity = {new_value}')
                    elif selected_action.get() == 'S':
                        #Test if there is enough inventory to ship 
                        if update_value > cur_value:
                            showwarning(title = 'Not enough inventory', 
                                        message = f"Can't ship {update_value}: only {cur_value} in stock")
                            
                        else:
                            #tell the controller to update this record in the database with new value
                            new_value = cur_value - update_value
                            self.controller.set_quantity(product_id, self.get_store_id(), new_value)
                            #refresh the treeview and close the update window
                            self.redraw()
                            updateWindow.destroy()
                    
                    
                    
                    
                    
            else:

                showwarning(title = 'Invalid Input', 
                        message = f"Please enter a integer greater than 0")
                
            
        selected_action = StringVar()
        action1 = ('Receive (Add to inventory)','R')
                   
        action2 = ('Ship (Subtract from inventory)', 'S')
        
        label = Label(updateWindow, text = 'Please make a selection')
        label.pack(fill='x', padx=7, pady=7)
        
        #Add option
        r1 = Radiobutton(updateWindow, 
                        text = action1[0],
                        value = action1[1],
                        variable = selected_action
                        )
        r1.pack(fill = 'x', padx = 5, pady = 5)
        
        
        #Subtract option
        r2 = Radiobutton(updateWindow, 
                        text = action2[0],
                        value = action2[1],
                        variable = selected_action
                        )
        r2.pack(fill = 'x', padx = 5, pady = 5)
        
        
        
        entryLabel = Label(updateWindow, text = 'Enter positive integer')
        entryLabel.pack(fill = 'x', padx = 5, pady = 5)
        
        #field to enter a positive integer
        entry = Entry(updateWindow, width = 10)
        entry.insert(INSERT,0)
        entry.pack(fill = 'x', padx = 5, pady = 5)
        
        button = Button(updateWindow, text = 'Update Inventory', command = submit)
        button.pack(fill = 'x', padx = 5, pady = 5)
        
        updateWindow.transient(parent)
        r1.invoke() #default option
        #updateWindow.grab_set()
                 
            
            
        
        
    def openInProgress(self, parent):
        showinfo(
            title = 'Result',
            message= """This feature is still under construction. Check back as this code is updated frequently."""
            )
        

    def redraw(self):
        for line in self.tv.get_children():
            self.tv.delete(line)
        
        self.draw_inventory()
        

        
"""
Create a color scheme for the rows of the table
Alternate between light and bg_dark to make it easier to read
Have a Light and Dark warning color
And a Light and Dark alert color
Alternate between odd and even rows on the table.

"""
