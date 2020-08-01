"""
Try to solve one of your problems by creating a context
manager, I give you some suggestions:

- Open and close the browser (Selenium).
- Connect and Close the connection of a database.
"""

from selenium import webdriver

class DriverContext:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver")
        
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get('<url>')

    def __enter__(self):
        return self.driver

    def __exit__(self, type, value, traceback):
        self.driver.quit()


"""
You can investigate the "contextlib" module and see other
types of context managers you can create, try one to
*suppress* any ValueError exceptions.
"""

from contextlib import suppress

def suppress_value_error():
    return int(input("Insert a number (or not):"))

with suppress(ValueError):
    number = suppress_value_error()
    print(number, "is a number")

