
print("===== WELCOME MINI STORE POS ODERING SYSTEM =====")

print("--- Product Menu ---")
print("1. Burger - PHP 50.00")
print("2. Fries - PHP 35.00")
print("3. Soft Drink - PHP 25.00")

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

Food1 = Product("Burger", 50)
Food2 = Product("Fries", 35)
Food3 = Product("Soft Drink", 25)

ProductNumber = input("Enter a Product Number(1-3): ")
Quantity = input("Enter Quantity: ")
Added = print("Added: " + str(ProductNumber) + " x " + str(Quantity))

AnotherProduct = input("Do you want to add another product? (yes/no): ")

ProductNumber = input("Enter a Product Number(1-3): ")
Quantity = input("Enter Quantity: ")
Added = print("Added: " + str(ProductNumber) + " x " + str(Quantity))

anotherProduct = input("Do you want to add another product? (yes/no): ")

Receipt = print("===== RECEIPT MINI STORE =====")

