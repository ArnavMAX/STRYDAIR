<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>STRYDAIR</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <img src="{{ url_for('static', filename='logo.png') }}" alt="Logo" class="logo">
        <nav>
            <a href="/">Home</a>
            <a href="/shop">Shop</a>
            <a href="/about">About</a>
            <a href="/contact">Contact</a>
            <a href="/login">Login</a>
            <a href="/register">Register</a>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
