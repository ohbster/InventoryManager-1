

class InventoryManagerController(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def show_products(self):
        products = self.model.get_product()
        self.view.show_products()
        
    def show_product(self, product_id):
        try:
            item = self.model.get_item(product_id)
            self.view.show_products()