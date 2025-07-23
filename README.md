<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>STRYDAIR | Streetwear for Hustlers</title>
  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@600&family=Inter&display=swap" rel="stylesheet">
  <!-- Font Awesome -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    :root {
      --font-heading: 'Orbitron', sans-serif;
      --font-body: 'Inter', sans-serif;
      --color-bg: #121212;
      --color-accent: #00ffd5;
      --color-text: #ffffff;
      --color-secondary: #2c2c3c;
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      background-color: var(--color-bg);
      color: var(--color-text);
      font-family: var(--font-body);
    }

    header {
      background-color: var(--color-secondary);
      padding: 1rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    header h1 {
      font-family: var(--font-heading);
      cursor: pointer;
      color: var(--color-accent);
    }

    nav a {
      margin: 0 1rem;
      color: var(--color-text);
      text-decoration: none;
      font-weight: bold;
    }

    nav a:hover {
      color: var(--color-accent);
    }

    .hero {
      text-align: center;
      padding: 4rem 2rem;
      background: linear-gradient(to right, #0f0f0f, #1c1c1c);
    }

    .hero h2 {
      font-family: var(--font-heading);
      font-size: 2.5rem;
      color: var(--color-accent);
    }

    .products {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 1rem;
      padding: 2rem;
    }

    .product {
      background-color: var(--color-secondary);
      padding: 1rem;
      border-radius: 8px;
      text-align: center;
    }

    .product img {
      max-width: 100%;
      border-radius: 4px;
    }

    .product h3 {
      margin-top: 0.5rem;
    }

    .product p {
      margin: 0.5rem 0;
    }

    .product button {
      background-color: var(--color-accent);
      border: none;
      padding: 0.5rem 1rem;
      cursor: pointer;
      border-radius: 4px;
      font-weight: bold;
    }

    .cart {
      position: fixed;
      top: 0;
      right: -320px;
      width: 300px;
      height: 100vh;
      background-color: #1a1a1a;
      color: #fff;
      padding: 1rem;
      overflow-y: auto;
      box-shadow: -2px 0 10px rgba(0, 0, 0, 0.5);
      transition: right 0.3s ease-in-out;
      z-index: 1000;
    }

    .cart.open {
      right: 0;
    }

    .cart-toggle {
      cursor: pointer;
    }

    .checkout-form {
      margin-top: 1rem;
    }

    .checkout-form input,
    .checkout-form select,
    .checkout-form textarea {
      width: 100%;
      margin: 0.5rem 0;
      padding: 0.5rem;
      border-radius: 4px;
      border: none;
    }

    .checkout-form button {
      background-color: var(--color-accent);
      padding: 0.5rem;
      width: 100%;
      border: none;
      border-radius: 4px;
      font-weight: bold;
      cursor: pointer;
    }

    footer {
      text-align: center;
      padding: 1rem;
      background-color: var(--color-secondary);
      font-size: 0.9rem;
    }

    @media (max-width: 600px) {
      .products {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>

<body>
  <header>
    <h1 onclick="goHome()">STRYDAIR</h1>
    <nav>
      <a href="#home">Home</a>
      <a href="#shop">Shop</a>
      <a href="#about">About</a>
      <a href="#contact">Contact</a>
      <a class="cart-toggle" onclick="toggleCart()">Cart</a>
    </nav>
  </header>

  <section class="hero" id="home">
    <h2>Streetwear for Hustlers</h2>
    <p>Built by 14-year-olds from Hyderabad & Rajasthan</p>
  </section>

  <section class="products" id="shop">
    <!-- Generate 100 products -->
    <script>
      const products = [
        ...Array(100).keys()
      ].map(i => ({
        name: `STRYDAIR Item ${i + 1}`,
        price: Math.floor(Math.random() * 1000) + 499,
        image: `https://via.placeholder.com/200?text=Item+${i + 1}`
      }));

      document.write(products.map(p => `
        <div class="product">
          <img src="${p.image}" alt="${p.name}" />
          <h3>${p.name}</h3>
          <p>₹${p.price}</p>
          <button onclick="addToCart('${p.name}', ${p.price})">Add to Cart</button>
        </div>
      `).join(''));
    </script>
  </section>

  <aside class="cart" id="cart">
    <h2>Your Cart <span style="float:right; cursor:pointer;" onclick="toggleCart()">&times;</span></h2>
    <ul id="cart-items"></ul>
    <p><strong>Total: ₹<span id="total">0</span></strong></p>

    <form class="checkout-form">
      <input type="text" placeholder="Name" required>
      <input type="email" placeholder="Email" required>
      <input type="text" placeholder="Phone Number" required>
      <textarea placeholder="Shipping Address" required></textarea>
      <select required>
        <option value="">Payment Method</option>
        <option value="cod">Cash on Delivery</option>
        <option value="upi">UPI</option>
        <option value="card">Credit/Debit Card</option>
      </select>
      <button type="submit" onclick="placeOrder(event)">Place Order</button>
    </form>
  </aside>

  <footer>
    &copy; 2025 STRYDAIR. Built with ❤️ by young hustlers.
  </footer>
<section id="about" style="padding: 2rem; background-color: #1c1c1c; text-align: center;">
  <h2 style="font-family: var(--font-heading); color: var(--color-accent); margin-bottom: 1rem;">About STRYDAIR</h2>
  <p style="max-width: 600px; margin: auto;">
    STRYDAIR is a youth-led streetwear brand built by 14-year-olds from Hyderabad and Rajasthan. We believe in hustling hard,
    staying bold, and wearing your story. Every piece we create is inspired by passion, street culture, and ambition.
  </p>
</section>

<section id="contact" style="padding: 2rem; background-color: #121212; text-align: center;">
  <h2 style="font-family: var(--font-heading); color: var(--color-accent); margin-bottom: 1rem;">Contact Us</h2>
  <p>Email: <a href="mailto:hello@strydair.com" style="color: var(--color-accent); text-decoration: none;">hello@strydair.com</a></p>
  <p>Instagram: <a href="https://instagram.com/strydair" target="_blank" style="color: var(--color-accent); text-decoration: none;">@strydair</a></p>
  <p>Phone: +91-9876543210</p>
</section>
  <script>
    let cart = [];

    function goHome() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function toggleCart() {
      const cartElement = document.getElementById("cart");
      cartElement.classList.toggle("open");
    }

    function addToCart(name, price) {
      cart.push({ name, price });
      updateCart();
    }

    function updateCart() {
      const cartList = document.getElementById("cart-items");
      const totalDisplay = document.getElementById("total");
      cartList.innerHTML = "";
      let total = 0;
      cart.forEach(item => {
        const li = document.createElement("li");
        li.textContent = `${item.name} - ₹${item.price}`;
        cartList.appendChild(li);
        total += item.price;
      });
      totalDisplay.textContent = total;
    }

    function placeOrder(e) {
      e.preventDefault();
      const orderId = `ORD-${Date.now()}`;
      alert(`Order ID: ${orderId}\nThank you for your order! We'll contact you soon.`);
      cart = [];
      updateCart();
      toggleCart();
    }
  </script>
</body>

</html>
