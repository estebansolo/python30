"""
Keep using the Pizza class, this time add some basic
methods for calculating and comparing each of the Pizza
objects created.
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
    
    def __lt__(self, other_pizza):
        return self.__price < other_pizza.price
    
    def __eq__(self, other_pizza):
        return self.__price == other_pizza.price
    
    def __gt__(self, other_pizza):
        return self.__price > other_pizza.price
    
    def __ne__(self, other_pizza):
        return self.__price != other_pizza.price
    
    def __add__(self, other_pizza):
        return self.__price + other_pizza.price
    

chicken_pizza = Pizza.chicken(13)
italian_pizza = Pizza.italian(13)

total = chicken_pizza + italian_pizza
print(f"Total: {total}")

if chicken_pizza > italian_pizza:
    print("Chicken Pizza costs more than Italian Pizza")
elif chicken_pizza < italian_pizza:
    print("Chicken Pizza costs less than Italian Pizza")
else:
    print("Chicken Pizza and Italian Pizza Costs the same")

# Output:
# Total: 6
# Chicken Pizza and Italian Pizza Costs the same