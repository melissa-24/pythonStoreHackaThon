# Class is a blueprint it should be capitalized

class Store:
    def __init__(self, name): # constructor function -  this will build our stores
        self.name=name  # self is basically saying this here we are saying this.name is going to be set to name
        self.products=[] # empty list of product to be in the store. here it is saying this.products is set to a empty array
    # by default there is a return self at the end of this but it is not needed
    def add_products(self, product):
        self.products.append(product)
        return self

honeyBeesCrochet=Store("HoneyBees Crochet")
print(honeyBeesCrochet.name) # this will print the store name

class Product:
    def __init__(self, name, price, category):
        self.name=name
        self.price=price
        self.category=category
    def print_info(self):
        print(f"Product Name: {self.name}, Product Price: ${self.price}, Product Category: {self.category}")
        return self
    def update_price(self, percent_change, is_increased):
        change=self.price*percent_change
        if is_increased:
            self.price+=change
            return self
        self.price=change
        return self


summerShawl=Product("Summer Shawl", 35.00, "Shawls")
alien=Product("Alien", 20.00, "Large Stuffed Animals")

# testing products
print(summerShawl.print_info())

# adding product to store
honeyBeesCrochet.add_products(summerShawl)
honeyBeesCrochet.add_products(alien)

# Increase price
summerShawl.update_price(.02, True).print_info()
# print(summerShawl.print_info()) # not needed as the line above auto prints

