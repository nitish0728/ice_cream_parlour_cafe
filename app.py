from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ice_cream_parlor.db'
db = SQLAlchemy(app)

class Flavor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    is_seasonal = db.Column(db.Boolean, default=False)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class CustomerSuggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flavor_name = db.Column(db.String(50), nullable=False)
    allergen = db.Column(db.String(50), nullable=True)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flavors', methods=['GET', 'POST'])
def manage_flavors():
    if request.method == 'GET':
        flavors = Flavor.query.all()
        return jsonify([{'name': flavor.name, 'is_seasonal': flavor.is_seasonal} for flavor in flavors])
    elif request.method == 'POST':
        data = request.json
        new_flavor = Flavor(name=data['name'], is_seasonal=data.get('is_seasonal', False))
        db.session.add(new_flavor)
        db.session.commit()
        return jsonify({'message': 'Flavor added!'}), 201

@app.route('/ingredients', methods=['GET', 'POST'])
def manage_ingredients():
    if request.method == 'GET':
        ingredients = Ingredient.query.all()
        return jsonify([{'name': ingredient.name, 'quantity': ingredient.quantity} for ingredient in ingredients])
    elif request.method == 'POST':
        data = request.json
        new_ingredient = Ingredient(name=data['name'], quantity=data['quantity'])
        db.session.add(new_ingredient)
        db.session.commit()
        return jsonify({'message': 'Ingredient added!'}), 201

@app.route('/suggestions', methods=['POST'])
def add_suggestion():
    data = request.json
    new_suggestion = CustomerSuggestion(flavor_name=data['flavor_name'], allergen=data.get('allergen'))
    db.session.add(new_suggestion)
    db.session.commit()
    return jsonify({'message': 'Suggestion added!'}), 201

@app.route('/cart', methods=['GET', 'POST', 'DELETE'])
def manage_cart():
    if request.method == 'GET':
        cart_items = Cart.query.all()
        return jsonify([{'product_name': item.product_name, 'quantity': item.quantity} for item in cart_items])
    elif request.method == 'POST':
        data = request.json
        new_item = Cart(product_name=data['product_name'], quantity=data['quantity'])
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'message': 'Item added to cart!'}), 201
    elif request.method == 'DELETE':
        data = request.json
        item = Cart.query.filter_by(product_name=data['product_name']).first()
        if item:
            db.session.delete(item)
            db.session.commit()
            return jsonify({'message': 'Item removed from cart!'}), 200
        return jsonify({'message': 'Item not found!'}), 404

if __name__ == '__main__':
    app.run(debug=True)
