#!/usr/bin/python

"""
py by Obijah(ohbster@protonamil.com)
Purpose: This is an excersise for learning to code in python using objects,
MVC pattern, and database for persistance layer
It will almost be useful when it is "completed". If I like it, I will build it
into something I could actually use IRL.

Special thanks to the following resources which help me get through this
##https://www.giacomodebidda.com/posts/mvc-pattern-in-python-sqlite/
##https://www.tutorialsteacher.com/python/python-class
##https://www.educba.com/function-overloading-in-python/
##https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection

"""
import sqlite3


"""
global Variables
"""
class InventoryManagerModel:
       
    
    """
    constructor
    
    """
    
    #!TODO: add _table_products_name and _table_qoh_name as constructor args
    #in case there is a need to initialize the table names to something different
    def __init__(self, _db_path=None):
       
        #The name of the Products table in database
        self.table_products = "Products"
        #The name of the Quantity Table in database
        self.table_quantity_on_hand = "QuantityOnHand"
     
        self.conn = None
        
        #if a db path name is passed to constructor, we use that path
        #otherwise, use a default
        if _db_path != None:
            self.db_path = _db_path
        
        else:
            self.db_path = "inventory_manager.db"
        
        #open a conection to the database
        self.connect_to_db()
        #DEBUG: Checking multiple connection attempts
        #self.connect_to_db()
        
        #create the Products and QoH tables if not already existing. 
        self.create_table_products()
        self.create_table_QuantityOnHand()
    
    
    """
    Connect / Disconnect
    
    """
    
    def connect_to_db(self,_db_path=None):
        if _db_path is None:
            print(f'Attempting connection with {self.db_path}')
            self.conn = sqlite3.connect(self.db_path)
            
        else:
            print(f"Attempting connection with {_db_path}")
            #TODO: Create a new connection if not using defualt
            #In the case of connecting to outside databases (IE, amazon, etsy)
            #that way can maintain multiplce connections in parallel
            self.conn = sqlite3.connect(_db_path)
            
        
        print("Connection Established!")
        

    
    def disconnect_from_db(self,_db_path=None):
        #TODO: Check if _db_path is valid
        self.conn.close()
        

    """
    Create your tables
    
    """
    
    #Main inventory table
    #@connect
    def create_table_products(self):
        #TODO: WHen you redisign the DB, consider using AUTOINCREMENT on 
        #Product_ID. Product_ID can be an internal key while SKU could 
        #be used as a secondary key. In case sku's accross different
        #selling platforms conflict/collide  
        sql = f'''CREATE TABLE IF NOT EXISTS {self.table_products}
        (Product_ID INT PRIMARY KEY NOT NULL,
        Name TEXT NOT NULL,
        Image VARCHAR NOT NULL,
        Description VARCHAR(500),
        Msrp REAL
        );''' 
        
        #TODO: This block of code appears twice. Try to create a function to 
        #reuse it. Make it neater
        try:
            self.conn.execute(sql)
        except sqlite3.IntegrityError as e:
            print(e)
        
        print("Table created")

    
    def create_table_QuantityOnHand(self):
        sql = f'''CREATE TABLE IF NOT EXISTS {self.table_quantity_on_hand}
        (Product_id INT,
        Qoh INT NOT NULL,
        CONSTRAINT FK_{self.table_quantity_on_hand} FOREIGN KEY (Product_ID) REFERENCES {self.table_products}(Product_ID)
        );'''
        
        print(f"{self.table_quantity_on_hand} table created")
        
        try:
            self.conn.execute(sql)
        except sqlite3.IntegrityError as e:
            print(e)
        
        print("Table created")

#conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY) \
#VALUES(1, 'SKY', 39, 'NEW YORK', 200000.00)");

    """
    Create
    functions used to create products
    """
    #To create new products you will need to create the product tuple, and the qoh
    #tuple seperately
    def add_product(self,_product_id=None, _name=None, _image=None, _desc=None, _msrp=None):
        
        _product_id = self.scrub(_product_id)
        _name =  self.scrub(_name)
        _image = self.scrub(_image)
        _desc = self.scrub(_desc)
        _msrp = self.scrub(_msrp)
        #what about real numbers? need to allow '.'
        
        sql = f"""INSERT INTO {self.table_products} (Product_ID, Name, Image, Description, Msrp)
        VALUES  ({_product_id},"{_name}","{_image}","{_desc}", {_msrp});"""
        
        print(f'Attempting: {sql}')
        try:
            self.conn.execute(sql)
            self.conn.commit()
            print("Product Created!")
        except sqlite3.IntegrityError as e:
            print(e)
        
        
   
    
    #def createProduct():


    """
    Update
    functions used to update  products
    """

    """
    Read
    functions to read / retrieve products 
    """
    def tuple_to_dict(self, _tuple):
        _dict = dict()
        _dict['id'] = _tuple[0]
        _dict['name'] = _tuple[1]
        _dict['image'] = _tuple[2]
        _dict['desc'] = _tuple[3]
        _dict['msrp'] = _tuple[4]
        
        return _dict
    
    
    #possibly make this into a static method as  it doesn't alter state of instance
    def get_products(self):
        sql = f"""SELECT * FROM Products; """
        try:
                c=self.conn.execute(sql)
                result = c.fetchall()
                #print(result)
                
                if result is not None:
                    #return self.tuple_to_dict(result)
                    return list(map(lambda x: self.tuple_to_dict(x), result))
                
        except sqlite3.IntegrityError as e:
            print(e)
            
    def get_product(self, _id):
        sql = f"""SELECT * FROM Products
        WHERE Product_ID = {_id}; """
        c=self.conn.execute(sql)
        result = c.fetchone()
        if result is not None:
            return self.tuple_to_dict(result)
        else:            
            #are there any standard error names to go by? look into it.
            #this is not the proper way to handle this. Raising exception is not 
            #necessary
            e =f"""No record matching {_id} in table {self.table_products}"""
            #raise sqlite3.OperationalError(e)
                

    """
    Delete
    function to delete products
    """
    def delete_product(self,_id):
        
        #TODO: Create a check to ensure that _id is a type int
        
        #_id = self.scrub(_id)
        sql = f"""DELETE FROM {self.table_products}
        WHERE Product_ID = {_id};"""
        try:
            self.conn.execute(sql)
            self.conn.commit()
            print(f"Deleted product {_id}")
        except sqlite3.OperationalError as e:
            print(e)
            
    """ 
    Update products
    
    """
            
    def set_product(self, _id, _name, _image, _desc, _msrp):
        #TODO: Overload this  function so that only arguments given are updated
        
        sql = f"""UPDATE {self.table_products}
        SET Name = "{_name}", Image = "{_image}", Description = "{_desc}", MSRP = {_msrp}
        WHERE Product_ID = {_id}; """
        
        try:
            self.conn.execute(sql)
            self.conn.commit()
            print(f"Product {_id} updated!")
         
        except sqlite3.OperationalError as e:
            print(e)
        
    """
    Get Quantities
    """
    #TODO:
    
    """
    Set Quantities
    """
    #TODO:
    
    """    
    Scrub / Sanitize input strings
    """
    #TODO!:need to modify this to allow '.' for real numbers amd spaces
    def scrub(self,input_string):
        return ''.join(k for k in input_string if k.isalnum() or k == ' ' or k == '.')
        
    
"""
Testing code
"""
myModel = InventoryManagerModel()
myModel.add_product("1", "ankh", "ankh.jpg", "this is an ankh", "12.00")
myModel.add_product("2", "africa", "africa.jpg", "this is an african pendant", "13.00")
products= myModel.get_products()
print("Listing Products")
print(products)
product= myModel.get_product(1)
print(product)
product= myModel.get_product(999)
product= myModel.get_product(2)
print(product)
myModel.delete_product(1)
products = myModel.get_products()
print(products)
myModel.set_product("2","myAfrica", "myAfrica.jpg", "This is myAfrica", "12.01")
products = myModel.get_products()
print(products)


