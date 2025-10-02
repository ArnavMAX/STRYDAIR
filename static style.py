body {
    background-color: black;
    color: cyan;
    font-family: 'Arial', sans-serif;
    text-align: center;
}

header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 50px;
}

header nav a {
    color: cyan;
    margin: 0 10px;
    text-decoration: none;
}

.products-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
    margin-top: 20px;
}

.product-card {
    background-color: #111;
    border: 1px solid cyan;
    border-radius: 12px;
    padding: 15px;
    width: 220px;
    text-align: center;
    position: relative;
    perspective: 1000px;
    transition: transform 0.3s ease;
}

.product-card:hover {
    transform: translateY(-10px);
}

.product-card img {
    width: 200px;
    height: 200px;
    object-fit: cover;
    border-radius: 10px;
    transition: transform 0.6s;
}

.product-card img.back {
    position: absolute;
    top: 15px;
    left: 15px;
    transform: rotateY(180deg);
    backface-visibility: hidden;
}

.product-card:hover img.front {
    transform: rotateY(180deg);
}

.product-card:hover img.back {
    transform: rotateY(0deg);
}

button {
    margin-top: 10px;
    width: 100%;
    padding: 8px;
    background-color: cyan;
    color: black;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #00ffffaa;
}
