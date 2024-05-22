from flask import Flask, render_template, request
import re

app = Flask(__name__, template_folder='website/templates', static_folder='website/static')

def extract_product_info(text):
    words = text.split()
    products = []
    product_info = {"name": "", "price": "", "iva": "", "total": ""}

    for word in words:
        if re.match(r'^[0-9]+$', word):  # Check if the word is an integer
            price = float(word)
            iva = price * 0.16
            total = price + iva
            product_info["price"] = f"{price:.2f}"
            product_info["iva"] = f"{iva:.2f}"
            product_info["total"] = f"{total:.2f}"
            products.append(product_info)
            product_info = {"name": "", "price": "", "iva": "", "total": ""}
        elif re.match(r'^[0-9]+\.[0-9]+$', word):  # Check if the word is a decimal number
            price = float(word)
            iva = price * 0.16
            total = price + iva
            product_info["price"] = f"{price:.2f}"
            product_info["iva"] = f"{iva:.2f}"
            product_info["total"] = f"{total:.2f}"
            products.append(product_info)
            product_info = {"name": "", "price": "", "iva": "", "total": ""}
        else:
            product_info["name"] += f"{word} "
    
    return products

@app.route('/', methods=['GET', 'POST'])
def index():
    products = []
    if request.method == 'POST':
        input_text = request.form['input_text']
        products = extract_product_info(input_text)
    return render_template('home.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
