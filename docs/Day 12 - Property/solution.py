"""
Use the class created about Pizza and implement the
property decorator for each of its attributes.
"""


class Pizza:
    def __init__(self, ingredients, price):
        self.__price = price
        self.__ingredients = ingredients
        self.__size = self._pizza_size(price)
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        self.__price = price
    
    @property
    def ingredients(self):
        return self.__ingredients
    
    @ingredients.setter
    def ingredients(self, ingredient):
        self.__ingredients = ingredient
    
    @property
    def size(self):
        return self.__size
    
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