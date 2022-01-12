import EntityBase

class Store(EntityBase.EntityBase):
    def __init__(self, store_id=None, type=None, address=None):
        self.store_id = store_id
        self.type = type
        self.address = address
        
    """
    Getters
    """
    def get_store_id(self):
        return self.store_id
    
    def get_type(self):
        return self.type
    
    def get_address(self):
        return self.address
        