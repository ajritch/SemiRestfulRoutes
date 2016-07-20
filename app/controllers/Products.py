"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)

        self.load_model('Product')
        self.db = self._app.db


   
    def index(self):
        products = self.models['Product'].get_all_products()
        print products
        return self.load_view('/products/index.html', products = products)

    def new(self):
        return self.load_view('/products/new.html')

    def create(self):
        info = {
            'name': request.form['name'],
            'description': request.form['description'],
            'price': request.form['price']
        }
        create_status = self.models['Product'].create_product(info)
        if create_status['status'] == True:
            return redirect('/')
        else:
            flash(create_status['message'])
            return redirect('/products/new')

    def show(self, id):
        product = self.models['Product'].get_product_by_id(id)
        return self.load_view('/products/show.html', product = product[0])

    def edit(self, id):
        product = self.models['Product'].get_product_by_id(id)
        return self.load_view('/products/edit.html', product = product[0])

    def update(self, id):
        info = {
            'name' : request.form['name'],
            'description' : request.form['description'],
            'price' : request.form['price']
        }
        update_status = self.models['Product'].update(info, id)
        if update_status['status'] == True:
            return redirect('/')
        else:
            flash(update_status['message'])
            return redirect('/products/edit/' + str(id))

    def delete(self, id):
        self.models['Product'].destroy(id)
        return redirect('/')