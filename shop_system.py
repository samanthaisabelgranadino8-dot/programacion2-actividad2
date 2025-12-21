# ===== CLASSES =====

class User:
    def __init__(self, name, last_name, email, password):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password


class UserManager:
    def __init__(self):
        self.users = []

    def register(self, name, last_name, email, password):
        for user in self.users:
            if user.email == email:
                return False
        self.users.append(User(name, last_name, email, password))
        return True

    def login(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                return user
        return None


class Product:
    def __init__(self, product_id, name, price):
        self.id = product_id
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.items = []

    def add(self, product, quantity):
        self.items.append([product, quantity])

    def show(self):
        if len(self.items) == 0:
            print("Cart is empty")
            return

        total = 0
        for item in self.items:
            product = item[0]
            quantity = item[1]
            subtotal = product.price * quantity
            total += subtotal
            print(product.name, "x", quantity, "=", subtotal)

        print("Total:", total)

    def clear(self):
        self.items = []
        print("Cart cleared")


# ===== PRODUCTS =====

products = [
    Product(1, "Laptop", 800),
    Product(2, "Mouse", 20),
    Product(3, "Keyboard", 50)
]

user_manager = UserManager()


# ===== MENUS =====

def store_menu():
    cart = Cart()

    while True:
        print("\n--- STORE MENU ---")
        print("1. View products")
        print("2. Add to cart")
        print("3. View cart")
        print("4. Clear cart")
        print("5. Logout")

        option = input("Option: ")

        if option == "1":
            for product in products:
                print(product.id, product.name, product.price)

        elif option == "2":
            product_id = int(input("Product ID: "))
            quantity = int(input("Quantity: "))

            for product in products:
                if product.id == product_id:
                    cart.add(product, quantity)
                    print("Added to cart")
                    break
            else:
                print("Product not found")

        elif option == "3":
            cart.show()

        elif option == "4":
            cart.clear()

        elif option == "5":
            print("Logout")
            break

        else:
            print("Invalid option")


def main_menu():
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        option = input("Option: ")

        if option == "1":
            name = input("Name: ")
            last_name = input("Last name: ")
            email = input("Email: ")
            password = input("Password: ")

            if user_manager.register(name, last_name, email, password):
                print("User registered")
            else:
                print("Email already exists")

        elif option == "2":
            email = input("Email: ")
            password = input("Password: ")

            user = user_manager.login(email, password)

            if user:
                print("Welcome", user.name)
                store_menu()
            else:
                print("Wrong email or password")

        elif option == "3":
            print("Bye")
            break

        else:
            print("Invalid option")


main_menu()