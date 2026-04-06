import os
from flask import Flask, render_template, request, redirect, url_for
from apriori_module import AprioriRecommender

app = Flask(__name__)

# ----------------- Load menu from text file -----------------
def load_menu(file_path):
    menu_dict = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                category, items = line.split(":")
                item_list = [i.strip() for i in items.split(",")]
                menu_dict[category] = item_list
    return menu_dict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
menu_file = os.path.join(BASE_DIR, "Menu.txt")
menu = load_menu(menu_file)

# ----------------- Initialize Recommender -----------------
csv_path = os.path.join(BASE_DIR, "dataset/restaurant_transactions_300.csv")
recommender = AprioriRecommender(csv_path)

# ----------------- Cart -----------------
cart = []

# ----------------- Routes -----------------
@app.route('/')
def home():
    return render_template('index.html', cart=cart)

@app.route('/menu')
def menu_page():
    return render_template('menu.html', menu=menu, cart=cart, recommendations=[])

'''@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    item = request.form.get('item')
    if item and item not in cart:
        cart.append(item)
    recommendations = recommender.recommend_items(item) if item else []
    return render_template('menu.html', menu=menu, cart=cart, recommendations=recommendations)
'''
@app.route('/cart')
def cart_page():
    return render_template('cart.html', cart=cart)

@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    item = request.form.get('item')
    if item in cart:
        cart.remove(item)
    return redirect(url_for('cart_page'))

@app.route('/clear_cart')
def clear_cart():
    cart.clear()
    return redirect(url_for('cart_page'))

@app.route('/api/add_to_cart', methods=['POST'])
def api_add_to_cart():
    data = request.get_json()
    item = data.get('item')
    if item and item not in cart:
        cart.append(item)
    recommendations = recommender.recommend_items(item) if item else []
    return {"cart": cart, "recommendations": recommendations}


if __name__ == '__main__':
    app.run(debug=True)
