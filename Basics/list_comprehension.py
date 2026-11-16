# Exercise 1: Filter even numbers and multiply them by 3
numbers = [3, 8, 12, 5, 20, 7] 

result = [ 
    number * 3 for number in numbers 
    if number % 2 == 0 ] 


print(result)

users = [
    {"name": "Samuel", "score": 85},
    {"name": "Alex", "score": 42},
    {"name": "Laura", "score": 91},
    {"name": "David", "score": 67}
]

#Exercise 2: Filter users by score.

users = [
    {"name": "Samuel", "score": 85},
    {"name": "Alex", "score": 42},
    {"name": "Laura", "score": 91},
    {"name": "David", "score": 67}
]

passed_users = [
            user["name"].upper() for user in users
            if user["score"] >= 70
]

print(passed_users)

#Exercise 3: Transform data from API

products = [
    {"name": "Laptop", "price": 1200, "stock": 5},
    {"name": "Mouse", "price": 25, "stock": 0},
    {"name": "Keyboard", "price": 80, "stock": 12},
    {"name": "Monitor", "price": 300, "stock": 0},
    {"name": "Headphones", "price": 150, "stock": 8}
]

available_products = [
        {
            "name": product["name"],
            "discounted_price": product["price"] * 0.9
        }
        for product in products
        if product["stock"] > 0
]

print(available_products)