import Product
import Quantity

class ProductQuantity(Product.Product, Quantity.Quantity):
    def __init__(self,product_id = None, name = None, image = None, description = None, msrp = None, store_id = None, quantity = None):
        self.product_id = self.sanitize(product_id)
        self.name = self.sanitize(name)
        self.image = self.sanitize(image)
        self.description = self.sanitize(description)
        self.msrp = self.sanitize(msrp)
        self.store_id = self.sanitize(store_id)
        self.quantity = self.sanitize(quantity)
        

