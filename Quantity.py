class Quantity(object):
    def __init__(self, product_id=None, store_id=None, quantity=None):
        self.product_id = product_id
        self.store_id = store_id
        self.quantity = quantity
        
    """
    Getters
    """
    def get_product_id(self):
        return self.product_id
    
    def get_store_id(self):
        return self.store_id
    
    def get_quantity(self):
        return self.quantity
    
    """
    Setters
    """
    def set_quantity(self, _quantity):
        self.quantity = _quantity
        


        