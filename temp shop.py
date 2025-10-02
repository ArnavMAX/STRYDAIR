{% extends "base.html" %}
{% block content %}
<h1>Shop</h1>
<div class="products-container">
    <div class="product-card">
        <img src="{{ url_for('static', filename='hoodie.jpg') }}" class="front">
        <img src="{{ url_for('static', filename='hoodie-back.jpg') }}" class="back">
        <h3>Premium Hoodie</h3>
        <p>Price: ₹1200</p>
        <form action="/pay" method="POST">
            <input type="hidden" name="amount" value="1200">
            <button type="submit">Buy Now</button>
        </form>
    </div>
</div>
{% endblock %}
