

class Controller(object):
    def __init__(self, _model, _view):
        self.model = _model
        self.view = _view
    
    def show_products(self):
        products = self.model.get_product()
        self.view.show_products()
        
    def show_product(self, _product_id):
        item = self.model.get_item(_product_id)
        self.view.show_products()
       