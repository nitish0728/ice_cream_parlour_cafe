document.addEventListener('DOMContentLoaded', () => {
    fetchFlavors();
    fetchIngredients();
    fetchCartItems();
});

function fetchFlavors() {
    fetch('/flavors')
        .then(response => response.json())
        .then(flavors => {
            const flavorList = document.getElementById('flavor-list');
            flavorList.innerHTML = '';
            flavors.forEach(flavor => {
                const flavorDiv = document.createElement('div');
                flavorDiv.className = 'item';
                flavorDiv.textContent = `Flavor: ${flavor.name}, Seasonal: ${flavor.is_seasonal}`;
                flavorList.appendChild(flavorDiv);
            });
        });
}

function fetchIngredients() {
    fetch('/ingredients')
        .then(response => response.json())
        .then(ingredients => {
            const ingredientList = document.getElementById('ingredient-list');
            ingredientList.innerHTML = '';
            ingredients.forEach(ingredient => {
                const ingredientDiv = document.createElement('div');
                ingredientDiv.className = 'item';
                ingredientDiv.textContent = `Ingredient: ${ingredient.name}, Quantity: ${ingredient.quantity}`;
                ingredientList.appendChild(ingredientDiv);
            });
        });
}

function fetchCartItems() {
    fetch('/cart')
        .then(response => response.json())
        .then(cartItems => {
            const cartList = document.getElementById('cart-list');
            cartList.innerHTML = '';
            cartItems.forEach(item => {
                const cartDiv = document.createElement('div');
                cartDiv.className = 'item';
                cartDiv.textContent = `Product: ${item.product_name}, Quantity: ${item.quantity}`;
                cartList.appendChild(cartDiv);
            });
        });
}

function addFlavor() {
    const name = document.getElementById('flavor-name').value;
    const isSeasonal = document.getElementById('is-seasonal').checked;

    fetch('/flavors', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, is_seasonal: isSeasonal })
    })
    .then(response => response.json())
    .then(() => {
        fetchFlavors();
    });
}

function addIngredient() {
    const name = document.getElementById('ingredient-name').value;
    const quantity = document.getElementById('ingredient-quantity').value;

    fetch('/ingredients', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, quantity })
    })
    .then(response => response.json())
    .then(() => {
        fetchIngredients();
    });
}

function addSuggestion() {
    const flavorName = document.getElementById('suggestion-flavor-name').value;
    const allergen = document.getElementById('suggestion-allergen').value;

    fetch('/suggestions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ flavor_name: flavorName, allergen })
    })
    .then(response => response.json())
    .then(() => {
        alert('Suggestion submitted!');
    });
}

function addToCart() {
    const productName = document.getElementById('cart-product-name').value;
    const quantity = document.getElementById('cart-quantity').value;

    fetch('/cart', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ product_name: productName, quantity })
    })
    .then(response => response.json())
    .then(() => {
        fetchCartItems();
    });
}
