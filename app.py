from flask import Flask, render_template, request, redirect, url_for, session
import razorpay

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Setup Razorpay client
razorpay_client = razorpay.Client(auth=("YOUR_RAZORPAY_KEY_ID", "YOUR_RAZORPAY_SECRET"))

# Dummy catalog
PRODUCTS = [
    {
        'id': 1,
        'name': 'STRYDAIR Tee Front',
        'price': 999,
        'img': 'static/images/28107A3A-3E7E-43BD-9125-0D1F0D7A4184.jpeg'
    },
    {
        'id': 2,
        'name': 'STRYDAIR Tee Back',
        'price': 999,
        'img': 'static/images/back.jpeg'
    }
]

@app.route('/')
def home():
    return render_template("home.html", logo_url=url_for('static', filename='images/Strydair.jpeg'))

@app.route('/shop')
def shop():
    cart = session.get('cart', [])
    return render_template("shop.html", products=PRODUCTS, cart=cart)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/faq')
def faq():
    return render_template("faq.html")

@app.route('/add_to_cart/<int:pid>')
def add_to_cart(pid):
    cart = session.get('cart', [])
    product = next((p for p in PRODUCTS if p['id'] == pid), None)
    if product:
        cart.append(product)
        session['cart'] = cart
    return redirect(url_for('shop'))

@app.route('/cart')
def cart():
    cart = session.get('cart', [])
    total = sum(item['price'] for item in cart)
    return render_template("cart.html", cart=cart, total=total)

@app.route('/pay', methods=['POST'])
def pay():
    cart = session.get('cart', [])
    amount = sum(item['price'] for item in cart) * 100  # Paise
    order = razorpay_client.order.create(dict(amount=amount, currency="INR", payment_capture="1"))
    return render_template("payment.html", order=order, cart=cart)

@app.route('/order_confirmation')
def order_confirmation():
    # clear cart after order
    session['cart'] = []
    return render_template("order_confirmation.html")

if __name__ == "__main__":
    app.run(debug=True)
