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

#Custom class defining a product
import Product
import Store
import Quantity
import ProductQuantity


"""
global Variables
"""
class Model:
       
    
    """
    constructor
    
    """
    
    #!TODO: add _table_products_name and _table_qoh_name as constructor args
    #in case there is a need to initialize the table names to something different
    def __init__(self, _db_path=None):
       
        #The name of the Products table in database
        self.table_products = "Products"
        #The name of the Quantity Table in database
        self.table_quantities = "Quantities"
        #Name of the table used keep track of the stores
        self.table_stores = "Stores"
     
        self.conn = None
        
        
        #if a db path name is passed to constructor, we use that path
        #otherwise, use a default
        if _db_path != None:
            self.db_path = _db_path
        
        else:
            self.db_path = "im.db"
        
        #open a conection to the database
        self.connect_to_db()
        #DEBUG: Checking multiple connection attempts
        #self.connect_to_db()
        
        #create the Products and QoH tables if not already existing. 
        self.create_table_products()
        self.create_table_stores()
        self.create_table_quantities()
          
    
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
    Handle Queries
    """
    def do_sql(self, _sql):
        #TODO:Need some sanitize code here to protect from SQL INJECTION
        
        try:
            c=self.conn.execute(_sql)
            return c
            
        except sqlite3.IntegrityError as e:
            print(e)    

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
           
        self.do_sql(sql)
        print(f"""Table "{self.table_products}" created""")
            
    def create_table_stores(self):
        sql = f""" CREATE TABLE IF NOT EXISTS {self.table_stores}
        (Store_ID INT PRIMARY KEY NOT NULL,
        Type VARCHAR(20) NOT NULL,
        Address VARCHAR(200)
        );
         """
        
        self.do_sql(sql)
        print(f"""Table "{self.table_stores}" created""")
        
    """
    TODO:cc
    TODO:Need to create a fk constraint for store_id from store tab
    TODO:Also, come up with better names for the fk constraints. (Table1_Table2), (Table2_Table3)
    
    """
    
    def create_table_quantities(self):
        sql = f'''CREATE TABLE IF NOT EXISTS {self.table_quantities}
        (Product_ID INT,
        Store_ID INT,
        Quantity INT NOT NULL,
        CONSTRAINT FK_{self.table_quantities}_{self.table_products} FOREIGN KEY (Product_ID) REFERENCES {self.table_products} (Product_ID),
        CONSTRAINT FK_{self.table_quantities}_{self.table_stores} FOREIGN KEY (Store_ID) REFERENCES {self.table_stores} (Store_ID)
        CONSTRAINT Product_Store_ID PRIMARY KEY (Product_ID, Store_ID)
        );'''
                    
        
        self.do_sql(sql)
        print(f"""Table "{self.table_quantities}"  created""")
        
        
    """
    *********************************
    Create
    functions used to create products
    
    *********************************
    """
    #To create new products you will need to create the product tuple, and the qoh
    #tuple seperately
    def add_product(self,product_id=None, name=None, image=None, description=None, msrp=None):
        
        product_id = self.scrub(product_id)
        name =  self.scrub(name)
        image = self.scrub(image)
        description = self.scrub(description)
        msrp = self.scrub(msrp)
        #what about real numbers? need to allow '.'
        
        sql = f"""INSERT INTO {self.table_products} (Product_ID, Name, Image, Description, Msrp)
        VALUES  ({product_id},"{name}","{image}","{description}", {msrp});"""
        
        print(f'Attempting: {sql}')

        self.do_sql(sql)
        self.conn.commit()
        print("Product Created!")


    #def createProduct():
    
    def add_store(self, store_id=None, type=None, address=None):
        #Sanitize the arguments
        store_id = self.scrub(store_id)
        type = self.scrub(type)
        address = self.scrub(address)
        
        sql = f"""INSERT INTO {self.table_stores}
        (Store_ID, Type, Address)
        VALUES
        ({store_id}, "{type}", "{address}")
        ;"""
 
        self.do_sql(sql)
        self.conn.commit()
        print("Store Created!")

                
    def add_quantity(self,product_id=None, store_id=None, quantity=None):
        #sanitize the arguments
        product_id = self.scrub(product_id)
        store_id = self.scrub(store_id)
        quantity = self.scrub(quantity)        
        
        sql = f"""INSERT INTO {self.table_quantities}
        (Product_ID, Store_ID, Quantity)
        VALUES
        ({product_id}, {store_id}, {quantity})
        ;"""
        

        self.do_sql(sql)
        self.conn.commit()
        print("Quantity created")
        
    def add_product_quantity(self, pq):
        self.add_product(pq.get_product_id(), pq.get_name(), pq.get_image(), pq.get_description(), pq.get_msrp())
        self.add_quantity(pq.get_product_id(), pq.get_store_id(), pq.get_quantity())
   
    """
    Conversion functions
    """ 
    
    def tuple_to_dict(self, _tuple):
        _dict = dict()
        _dict['id'] = _tuple[0]
        _dict['name'] = _tuple[1]
        _dict['image'] = _tuple[2]
        _dict['desc'] = _tuple[3]
        _dict['msrp'] = _tuple[4]
        
        return _dict
    #Convert a tuple from Product table to a Product Object
    def tuple_to_product(self, _tuple):
        _product = Product.Product(product_id =_tuple[0],
                          name =_tuple[1],
                          image = _tuple[2],
                          description = _tuple[3],
                          msrp = _tuple[4]
                          )
        return _product
    
    #convert tuple from Store table to a Store object
    def tuple_to_store(self, _tuple):
        _store = Store.Store(store_id = _tuple[0],
                             type = _tuple[1],
                             address = _tuple[2]
                             )
        return _store
        
        #Convert tuple from Quantity table into a Quantity object
    def tuple_to_quantity(self, _tuple):
        _quantity = Quantity.Quantity(product_id = _tuple[0],
                                     store_id = _tuple[1],
                                     quantity = _tuple[2]
                                     )
        return _quantity
        
    """
    *********************************
    "READ
    "Select / Retreive functions
    "    products
    "    stores
    "    quantities
    
    *********************************
    """

    #possibly make this into a static method as  it doesn't alter state of instance
    def get_products(self):
        sql = f"""SELECT * FROM Products; """

        c=self.do_sql(sql)
        result = c.fetchall()

        if result is not None:
            return list(map(lambda x: self.tuple_to_product(x), result))
            
    def get_product(self, _product_id):
        sql = f"""SELECT * FROM Products
        WHERE Product_ID = {_product_id}; """
        c=self.do_sql(sql)
        result = c.fetchone()
        if result is not None:
            #return self.tuple_to_dict(result)
            return self.tuple_to_product(result)
        else:            
            #TODO:are there any standard error names to go by? look into it.
            #this is not the proper way to handle this. Raising exception is not 
            #necessary
            e =f"""No record matching {_product_id} in table {self.table_products}"""
            print(e)
            #raise sqlite3.OperationalError(e)
    
    """
    Get Stores
    """
    def get_store(self, _store_id):
        sql = f"""SELECT * FROM Stores
        WHERE Store_ID = {_store_id};  """
        c=self.do_sql(sql)
        result = c.fetchone()
        if result is not None:
            return self.tuple_to_store(result)
        else:
            #TODO: Properly exception handle this
            e =f"""No record matching {_store_id} in table {self.table_stores}"""
            print(e)
            
    def get_stores(self):
        sql = f"""SELECT * FROM Stores; """
        c = self.do_sql(sql)
        result = c.fetchall()
        if result is not None:
            return list(map(lambda x: self.tuple_to_store(x), result))
        else:
            print(f"""Warning: No stores found in table {self.table_stores}. """)
  
    """
    Get Quantities
    """
    #TODO:
    def get_quantity(self, _product_id, _store_id):
        sql = f"""SELECT * FROM {self.table_quantities}
        WHERE Product_ID = {_product_id}
        AND Store_ID = {_store_id}
        ; """
        if(_product_id is not None) and (_store_id is not None):
        
            c=self.do_sql(sql)
            result = c.fetchone()
                
            if result is not None:
                return self.tuple_to_quantity(result)
            else:
                print(f"No results for product_id:{_product_id}, store_id{_store_id} in table {self.table_quantities}")
            
            #return    
        else:
            print(f"Error Missing Arguements: get_quantity(product_id={_product_id},store_id={_store_id})")
            
    def get_quantities(self):
        sql = f"""SELECT * FROM {self.table_quantities} ; """
        c = self.do_sql(sql)
        result = c.fetchall()
        if result is not None:
            return list(map(lambda x: self.tuple_to_quantity(x), result))
        else:
            print(f"Warning: No quantity found in table, {self.table_quantities}")
            
    #return a dictionary of all product, quantity pairs in the Quantity table, using product_id as index            
    
    
    #create a new function to create a dict from the get_quantities function
    def get_store_quantities(self, _store_id):
        sql = f"""SELECT * 
        FROM {self.table_quantities} 
        WHERE Store_ID = {_store_id}
        ;
        """
        quantity=Quantity.Quantity()
        thisdict={}
        c = self.do_sql(sql)
        result = c.fetchall()
        if result is not None:
            for item in result:

                quantity=self.tuple_to_quantity(item)
                
                thisdict = {
                    f"{quantity.get_product_id()}" : quantity
                                        
                    }
            return thisdict
        else:
            print(f"Warning: No inventory available for Store_ID {_store_id} in tables {self.table_quantities}")
            return None
        
    def tuple_to_product_quantity(self, _tuple):
        pq = ProductQuantity.ProductQuantity(product_id = _tuple[0],
                                             name = _tuple[1],
                                             image = _tuple[2],
                                             description = _tuple[3],
                                             msrp = _tuple[4], 
                                             store_id = _tuple[5],
                                             quantity = _tuple[6] )
        return pq
    
    #Do i still need get_store_quantities?()    
    def get_product_quantities(self, store_id):
        sql = f"""SELECT {self.table_products}.Product_ID, {self.table_products}.Name, {self.table_products}.Image, 
        {self.table_products}.Description, {self.table_products}.MSRP, {self.table_quantities}.Store_ID, {self.table_quantities}.Quantity 
        FROM {self.table_products} INNER JOIN {self.table_quantities} 
        ON {self.table_products}.Product_ID = {self.table_quantities}.Product_ID 
        WHERE {self.table_quantities}.Store_ID = {store_id}
        ;"""
        
        c=self.do_sql(sql)
        result = c.fetchall()
        if result is not None:
            return list(map(lambda x: self.tuple_to_product_quantity(x), result))
        else:
            print(f"Warning: Query returned no results: <{sql}>")
            return None
  
    """ 
    *********************************
    UPDATE
    Update products
    "    products
    "    stores
    "    quantities
    
    *********************************
    """
            
    def set_product(self, _id, _name, _image, _desc, _msrp):
        #TODO: Overload this  function so that only arguments given are updated
        
        sql = f"""UPDATE {self.table_products}
        SET Name = "{_name}", Image = "{_image}", Description = "{_desc}", MSRP = {_msrp}
        WHERE Product_ID = {_id}; """

        self.do_sql(sql)
        self.conn.commit()
        print(f"Product {_id} updated!")

        
    
    """
    Set Stores
    """
    #TODO!
    
    """
    Set Quantities
    """
    #TODO:
    def set_quantity(self, product_id, store_id, quantity):
        sql = f"""UPDATE {self.table_quantities}
        SET Quantity = {quantity}
        WHERE Product_ID = {product_id} AND Store_ID = {store_id};"""
        

        self.do_sql(sql)
        self.conn.commit()
        print(f"Quantity updated!")

    """
    *********************************
    DELETE
    function to delete records
    
    *********************************
    """
    def delete_product(self,_id):
        
        #TODO: Create a check to ensure that _id is a type int
        
        #_id = self.scrub(_id)
        sql = f"""DELETE FROM {self.table_products}
        WHERE Product_ID = {_id};"""

        self.do_sql(sql)
        self.conn.commit()
        print(f"Deleted product {_id}")

            
    #TDDO: Delete Store
    #TODO: Delete Quantity
    
    
    
    """    
    Scrub / Sanitize input strings
    """
    #TODO!:need to modify this to allow '.' for real numbers amd spaces
    def scrub(self,input_string):
        #test if the input is a type string before attempting to scrub
        if isinstance(input_string, str):
            print("Yay, string!")
            return ''.join(k for k in input_string if k.isalnum() or k == ' ' or k == '.')
            
        else:
            print("Scrub: None string input detected!")
            return input_string
        #return ''.join(k for k in input_string if k.isalnum() or k == ' ' or k == '.')
        
    
"""
*****************
Testing Area
*****************
"""

