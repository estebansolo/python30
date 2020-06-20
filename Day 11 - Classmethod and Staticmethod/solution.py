"""
Create a class called Pizza that allows you to create different
types of them. When you create them, give them the price of the
pizza.

The class should calculate the size of the pizza based on the
price.

0 - 10 small
11 - 20 medium
21 - 30 large
"""

class Pizza:
    def __init__(self, ingredients, price):
        self.price = price
        self.ingredients = ingredients
        self.size = self._pizza_size(price)
    
    @classmethod
    def chicken(cls, price):
        ingredients = ["cheese", "chicken", "mushroom"]
        return cls(ingredients, price)
    
    @classmethod
    def italian(cls, price):
        ingredients = ["salami", "cheese", "tomato", "basil"]
        return cls(ingredients, price)
    
    @staticmethod
    def _pizza_size(price):
        sizes = {
            "small": (0, 10),
            "medium": (11, 20),
            "large": (21, 30)
        }

        pizza_size = ""
        for size, (min_price, max_price) in sizes.items():
            if min_price <= price <= max_price:
                pizza_size = size
                break
        
        return pizza_size

chicken_pizza = Pizza.chicken(10)
print(chicken_pizza.size)
print(chicken_pizza.ingredients)

italian_pizza = Pizza.italian(22)
print(italian_pizza.size)
print(italian_pizza.ingredients)

# Output:
# small
# ['cheese', 'chicken', 'mushroom']
#
# large
# ['salami', 'cheese', 'tomato', 'basil']