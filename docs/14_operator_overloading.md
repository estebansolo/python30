# Day 14 - Operator Overloading

Every day we write multiple lines of code, comparing values or performing calculations similar to this one:

```python
print(15 > 20)
print(36 - 23)

# Output:
# False
# 13
```

Usually, we think about comparing or making numerical calculations since it is something basic that we know since we were children, but this type of comparison can be performed with any class using some magic methods.

For now we will create a `Product` class with some of its basic attributes:

```python
class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    
    def __repr__(self):
        return f"Product: {self.__name}"

pizza = Product("pizza", 5)
hotdog = Product("hotdog", 1)

print(pizza)
print(hotdog)

# Output:
# Product: pizza
# Product: hotdog
```

Two instances of the Product class were created, what about trying to compare them.

```python
print(pizza > hotdog)
print(pizza < hotdog)
print(pizza == hotdog)

# Output:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: '>' not supported between instances of 'Product' and 'Product'
```

At this point it is not possible to compare these instances, in fact it is not known what we are comparing, to fix this we will add some magic methods.

```python
class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    
    def __repr__(self):
        return f"Product: {self.__name}"
    
    def __lt__(self, other_instance):
        return self.__price < other_instance.__price
    
    def __gt__(self, other_instance):
        return self.__price > other_instance.__price
    
    def __eq__(self, other_instance):
        return self.__price == other_instance.__price

pizza = Product("pizza", 5)
hotdog = Product("hotdog", 1)
```

Let's try again to make the comparisons.

```python
print(pizza > hotdog)
print(pizza < hotdog)
print(pizza == hotdog)

# Output:
# True
# False
# False
```

These magic methods allow us to compare our items, in my case I had their prices compared, however, you can define these methods as you need them.

These methods receive as an argument another one, which is related to the value with which we are going to make the comparison.

## Operations

It is possible to perform operations between different objects, what about knowing the total of an order? why not add up each of these products and get the total.

[More info](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types)

```python
class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    
    def __repr__(self):
        return f"Product: {self.__name}"
    
    def __add__(self, other_instance):
        return self.__price + other_instance.__price

pizza = Product("pizza", 5)
hotdog = Product("hotdog", 1)

total = pizza + hotdog
print(total)

# Output:
# 6
```

[Go to the Challenge](https://github.com/estebansolo/Python30/blob/master/exercises/14_operator_overloading.py)

[Go to the Solution](https://github.com/estebansolo/Python30/blob/master/solutions/14_operator_overloading.py)