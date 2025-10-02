from flask import Flask, render_template, request, redirect, session
import razorpay
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to something secure

# Razorpay client (replace with your keys)
razorpay_client = razorpay.Client(auth=("YOUR_RAZORPAY_KEY_ID", "YOUR_RAZORPAY_SECRET"))

ADMIN_EMAIL = "arnavreddy2402@gmail.com"
users = {}  # Simple in-memory storage (for demo)

# ---------------- ROUTES ----------------
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/shop')
def shop():
    return render_template("shop.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if email in users and users[email]["password"] == password:
            session["user"] = email
            return redirect("/admin" if email == ADMIN_EMAIL else "/")
        return "Invalid login"
    return render_template("login.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        users[email] = {"password": password}
        return redirect("/login")
    return render_template("register.html")

@app.route('/admin')
def admin():
    if "user" in session and session["user"] == ADMIN_EMAIL:
        return render_template("admin.html")
    return "Access denied"

@app.route('/pay', methods=["POST"])
def pay():
    amount = int(request.form["amount"]) * 100
    order = razorpay_client.order.create(dict(amount=amount, currency="INR", payment_capture="1"))
    return render_template("payment.html", order=order)

# ---------------- RUN ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render sets PORT automatically
    app.run(host="0.0.0.0", port=port, debug=True)

