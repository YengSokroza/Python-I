import subprocess
subprocess.run("cls", shell=True)

# Sample Data
my_cart = {
    'apple':  {'price': 0.50, 'qty': 4},
    'bread':  {'price': 2.00, 'qty': 1},
}

# def create_cart():
#     """Return a new empty cart."""
#     return {}

# my_cart = create_cart()

def title(text):
    width = 30
    print('=' * width)
    print(text.center(width))
    print('=' * width)

def add_item(cart, name, price, qty=1):
    """Add an item, or increase its quantity if it already exists."""
    if name in cart:
        cart[name]['qty'] += qty
    else:
        cart[name] = {'price': price, 'qty': qty}
    return cart

def add_many(cart, *items):
    """Add several (name, price, qty) tuples at once."""
    # TODO 1: 
    # using for loop thruogh each item
    # using add_item() function
    # return cart


def update_item(cart, name, **changes):
    """Change price and/or qty of an existing item."""
    if name in cart:
        cart[name].update(changes)
    return cart

def remove_item(cart, name, qty):
    """Remove an item completely, or reduce its quantity."""
    # TODO 2
    pass
 

def get_total(cart, tax=0.0):
    """Return the final total after tax."""
    # TODO 3
    pass


def show_cart(cart):
    """Print every item with its line total."""
    title('Checkout')
    if not cart:
        print('Cart is empty')
        return
    for name, info in cart.items():
        qty = info['qty']
        price = info['price']
        print(f'{name:<8} {qty} x {price:.2f} = {qty * price:.2f}')
    print('='*30)
    get_total(cart,0.1)

show_cart(my_cart)
