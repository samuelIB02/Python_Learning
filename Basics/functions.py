# Exercise 1: Calculate discount
def calculate_price(price, discount=0):
    if discount < 0 or discount > 100:
        return None

    discount_transform = discount/100

    final_price = price - (price * discount_transform)

    return final_price


print(calculate_price(100,-10))
print(calculate_price(100, 20))
print(calculate_price(250, 10))

# Exercise 2: Learning how to use *args
def get_maximum(*args):
    if not args:
        return None

    max_number = args[0]

    for number in args[1:]:
            
        if number > max_number:
            max_number = number
    return max_number

print(get_maximum(4, 9, 2))      # 9
print(get_maximum(15, 3, 27, 8)) # 27
print(get_maximum())             # None

#Exercise 3: Learning how to use **kwargs
def create_profile(**kwargs):
    if not kwargs.get("name"):
        return None
    return kwargs


print(create_profile(name="Samuel", age=24))
print(create_profile(name="Laura", role="Developer", active=True))
print(create_profile(age=30))

#Exercise 4: Learning how to create lambda functions

calculate_square = lambda number: number * number

print(calculate_square(4))   # 16
print(calculate_square(7))   # 49
print(calculate_square(-3))  # 9

#Exercise 5: Sorting products with lambda and sorted()

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Monitor", "price": 300},
    {"name": "Keyboard", "price": 80}
]

sorted_product = sorted(products, key=lambda product: product["price"] )
sorted_product_za = sorted(products, key=lambda product: product["name"],reverse = True )

print(sorted_product_za)

#Exercise 6: Filtrate products using filter(). List used: products from Exercise 5

expensive_products = list(filter(lambda product: product["price"] > 100,products))

print(expensive_products)

#Exercise 7: Transformin products using map(). List used: products from Exercise 5

discounted_prices = list(map(lambda prodcut: prodcut["price"]*0.8,products))

print(discounted_prices)

#Exercise 8: Concept reinforcement

users = [
    {"name": "Samuel", "age": 24, "active": True},
    {"name": "Laura", "age": 17, "active": True},
    {"name": "Carlos", "age": 32, "active": False},
    {"name": "Ana", "age": 28, "active": True},
    {"name": "Pedro", "age": 16, "active": False}
]

valid_users = list(map(lambda user: user ["name"].upper(), filter(lambda user: user["active"] and user["age"] >= 18,users)))

print(valid_users)
