

class Controller(object):
    def __init__(self, _model, _view):
        self.model = _model
        self.view = _view
    
    def draw_inventory(self):
        products = self.model.get_product()
        self.view.draw_inventory()
        
    def show_product(self, _product_id):
        item = self.model.get_item(_product_id)
        self.view.draw_inventory()
        
    def get_store(self, store_id):
        store = self.model.get_store(store_id)
        return store
    
    def get_stores(self):
        return self.model.get_stores()
    
    def get_quantities(self):
        return self.model.get_quantities()

    def get_store_quantities(self, _store_id):
        return self.model.get_store_quantities(_store_id)
    
    def get_product_quantities(self, _store_id):
        return self.model.get_product_quantities(_store_id)
    
    def add_product_quantity(self, _product_quantity = None):
        self.model.add_product_quantity(_product_quantity)