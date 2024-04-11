""""""
"""
Task 1: Create Base Product Class
    - Develop a base class Product with common attributes like product ID, name, price, and a method to display product information.
    - Expected Outcome: A Product class that can hold general information about a product and display it."""


class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_product(self):
        print(f"Product ID: {self.product_id}\nName: {self.name}\nPrice: ${self.price}")


"""
Task 2: Implement Subclasses for Specific Products
    - Create subclasses Book, Electronic, and Clothing that inherit from Product.
    - Each subclass should have additional attributes relevant to its category (e.g., author for books, specs for electronics, size for clothing).
    - Expected Outcome: Each subclass contains both inherited attributes from Product and new attributes specific to the product type.
    
Task 3: Override Display Method in Subclasses
    - Override the method to display product information in each subclass to include specific attributes.
    - For example, the Book class should display the author, Electronic should display specs, etc.
    - Expected Outcome: Calling the display method on an instance of any subclass shows both common and specific product details.
"""


class Book(Product):
    def __init__(self, author, product_id, name, price):
        super().__init__(product_id, name, price)
        self.author = author

    def display_product(self):
        print(f"Product ID: {self.product_id}\nName: {self.name}\nAuthor: {self.author}\nPrice: ${self.price}")


class Electronic(Product):
    def __init__(self, specs, product_id, name, price):
        super().__init__(product_id, name, price)
        self.specs = specs

    def display_product(self):
        print(f"Product ID: {self.product_id}\nName: {self.name}\nSpecs: {self.specs}\nPrice: ${self.price}")


class Clothing(Product):
    def __init__(self, size, material, product_id, name, price):
        super().__init__(product_id, name, price)
        self.size = size
        self.material = material

    def display_product(self):
        print(f"Product ID: {self.product_id}\nName: {self.name}\nSize: {self.size}\nMaterial: {self.material}\nPrice: ${self.price}")


"""
Task 4: Test Product Catalog Functionality
    - Instantiate objects of each subclass and call their display methods to ensure correct information is shown.
    - Expected Outcome: The system should accurately display detailed information for each type of product, demonstrating inheritance and method overriding.
"""
product1 = Product(1, "glasses", 12.99)
book1 = Book("J.K. Rowling", 2, "Harry Potter and the Sorcerer's Stone", 18.99)
electronic1 = Electronic("Storage: 2TB, Memory: 16GB, Operating System: MacOS", 3, "Macbook Pro", 1210.89)
clothes1 = Clothing("small", "cotton", 4, "t-shirt", 10.99)

product1.display_product()
book1.display_product()
electronic1.display_product()
clothes1.display_product()