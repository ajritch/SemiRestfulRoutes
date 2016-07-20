""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
from decimal import Decimal

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()


    def create_product(self, info):
        try:
            price = Decimal(info['price'])
        except:
            return {'status': False, 'message': 'Invalid price.'}

        query = ("INSERT INTO products " +
                "(name, description, price, created_at, updated_at) " +
                "VALUES (:name, :description, :price, NOW(), NOW())")
        data = {
            'name': info['name'],
            'description': info['description'],
            'price': price
        }
        self.db.query_db(query, data)
        return {'status': True}


    def get_all_products(self):
        return self.db.query_db("SELECT * FROM products")

    def get_product_by_id(self, id):
        query = "SELECT * FROM products WHERE id = :id"
        data = {'id': id}
        return self.db.query_db(query, data)

    def update(self, info, id):
        try:
            price = Decimal(info['price'])
        except:
            return {'status': False, 'message': 'Invalid price.'}

        query = "UPDATE products SET name = :name, description = :description, price = :price, updated_at = NOW() WHERE id = :id"
        data = {
            'name' : info['name'],
            'description' : info['description'],
            'price' : price,
            'id' : id
        }
        self.db.query_db(query, data)
        return {'status': True}


    def destroy(self, id):
        query = "DELETE FROM products WHERE id = :id"
        data = {'id': id}
        return self.db.query_db(query, data)

    """

    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """