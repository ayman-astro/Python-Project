# customer
# Employee
# Admin

from abc import ABC
from orders import Order


class User(ABC):

    def __init__(self, name, email, phone, address):
        super().__init__()
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address


class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = Order()

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if item.quantity >= quantity:
                item.quantity -= quantity
                self.cart.add_item(item)
                print(
                    f"\n{quantity} {item.name}{'s' if item.quantity > 1 else ''} added\n"
                )
            else:
                print(f"\n{item.name} quantity exceeded\n")

        else:
            print(f"{item_name} not found")

    def view_cart(self):
        print("----------Cart----------")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price: {self.cart.total_price()}")
        print("------------------------")

    def pay_bill(self):
        print(f"Total Price: {self.cart.total_price()} paid successfully")
        self.cart = Order()


class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, email, phone, address)
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):

    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)

    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)

    def view_employee(self, restaurant):
        restaurant.view_employee()

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_item(item)

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def remove_item(self, restaurant, item_name):
        restaurant.menu.remove_item(item_name)


# admin = Admin("admin", "admin@gmail.com", 2425234, "Dhaka")

# item1 = Food_Item("Pizza", 12.45, 10)
# item2 = Food_Item("Burger", 30, 30)

# admin.add_new_item(food_palace, item1)
# admin.add_new_item(food_palace, item2)
