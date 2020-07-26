"""
Use the Pizza class and implement some methods that can help you:

* Object representation
* To know if the pizza has any ingredients e.g. "cheese" in pizza_n
* Count the pizza ingredients
"""

class Pizza:
    def __init__(self, name, ingredients, price):
        self.__name = name
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
        return cls("Chicken", ingredients, price)
    
    @classmethod
    def italian(cls, price):
        ingredients = ["salami", "cheese", "tomato", "basil"]
        return cls("Italian", ingredients, price)
    
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
    
    def __repr__(self):
        return f"Pizza {self.__name}"
    
    def __contains__(self, ingredient):
        return ingredient in self.__ingredients
    
    def __len__(self):
        return len(self.__ingredients)
        

chicken_pizza = Pizza.chicken(10)
italian_pizza = Pizza.italian(22)

print(chicken_pizza)
print("salami" in chicken_pizza)

print(italian_pizza)
print("salami" in italian_pizza)

# Output:
# Pizza Chicken
# False
#
# Pizza Italian
# True