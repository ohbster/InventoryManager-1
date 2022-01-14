import EntityBase

class Product(EntityBase.EntityBase):
    def __init__(self, product_id, name=None, image=None, description=None, msrp=None):
        self.set_product_id(product_id)
        self.set_name(name)
        self.set_image(image)
        self.set_description(description)
        self.set_msrp(msrp)
        
    """
    Getters
    """
        
    def get_product_id(self):
        return self.product_id
    
    def get_name(self):
        return self.name
    
    def get_image(self):
        return self.image
    
    def get_description(self):
        return self.description
    
    def get_msrp(self):
        return self.msrp

    
    """
    Setters
    """
    
    def set_product_id(self, product_id):
        self.product_id = self.sanitize(product_id)
        
    def set_name(self,name):
        self.name = self.sanitize(name)
        
    def set_image(self, image):
        self.image = self.sanitize(image)
        
    def set_description(self, description):
        self.description = self.sanitize(description)
        
    def set_msrp(self, msrp):
        self.msrp = self.sanitize(msrp)
        
        
    
