{% extends "base.html" %}
{% block content %}
<h2>Payment</h2>
<p>Order ID: {{ order.id }}</p>
<p>Amount: ₹{{ order.amount / 100 }}</p>
<p>Checkout with Razorpay!</p>
{% endblock %}
