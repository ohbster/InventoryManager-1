import EntityBase

class Store(EntityBase.EntityBase):
    def __init__(self, store_id=None, type=None, address=None):
        
        self.set_store_id(store_id)
        self.set_type(type)
        self.set_address(address)
        
    """
    Getters
    """
    def get_store_id(self):
        return self.store_id
    
    def get_type(self):
        return self.type
    
    def get_address(self):
        return self.address
        
        
    def set_store_id(self, store_id):
        self.store_id = self.sanitize(store_id)
        
    def set_type(self, type):
        self.type = self.sanitize(type)
        
    def set_address(self, address):
        self.address = self.sanitize(address)