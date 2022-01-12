import Product
import Quantity

class ProductQuantity(Product.Product, Quantity.Quantity):
    def __init__(self,product_id = None, name = None, image = None, description = None, msrp = None, store_id = None, quantity = None):
        self.product_id = product_id
        self.name = name
        self.image = image
        self.description = description
        self.msrp = msrp
        self.store_id = store_id
        self.quantity = quantity
        

