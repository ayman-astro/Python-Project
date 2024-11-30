from food_item import Food_Item
from menu import Menu
from users import Admin, Employee, Customer
from restaurant import Restaurant, food_palace
from orders import Order


def customer_menu():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    phone = input("Enter Your Phone: ")
    address = input("Enter Your Address: ")

    customer = Customer(name, email, phone, address)

    while True:
        print(f"Welcome {name}!!")
        print("1. View Menu")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Pay bill")
        print("5. Exit")

        option = int(input("Enter your Option: "))

        if option == 1:
            customer.view_menu(food_palace)

        elif option == 2:
            item_name = input("Enter Item Name: ")
            item_quantity = int(input("Enter Item Quantity: "))
            customer.add_to_cart(food_palace, item_name, item_quantity)

        elif option == 3:
            customer.view_cart()

        elif option == 4:
            customer.pay_bill()

        elif option == 5:
            break

        else:
            print("Invalid")


def admin_menu():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    phone = input("Enter Your Phone: ")
    address = input("Enter Your Address: ")

    admin = Admin(name, email, phone, address)

    while True:
        print(f"Welcome {name}!!")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employees")
        print("4. View Menu")
        print("5. Delete Item")
        print("6. Exit")

        option = int(input("Enter your Option: "))

        if option == 1:
            item_name = input("Enter Item Name: ")
            item_price = int(input("Enter Item Price: "))
            item_quantity = int(input("Enter Item Quantity: "))
            item = Food_Item(item_name, item_price, item_quantity)
            admin.add_new_item(food_palace, item)

        elif option == 2:
            employee_name = input("Enter Employee's Name: ")
            employee_email = input("Enter Employee's Email: ")
            employee_phone = input("Enter Employee's Phone: ")
            employee_address = input("Enter Employee's Address: ")
            employee_age = int(input("Enter Employee's Age: "))
            employee_designation = input("Enter Employee's Designation: ")
            employee_salary = int(input("Enter Employee's Salary: "))
            employee = Employee(
                employee_name,
                employee_email,
                employee_phone,
                employee_address,
                employee_age,
                employee_designation,
                employee_salary,
            )
            admin.add_employee(food_palace, employee)
        elif option == 3:
            admin.view_employee(food_palace)

        elif option == 4:
            admin.view_menu(food_palace)

        elif option == 5:
            item_name = input("Enter Item Name: ")
            admin.remove_item(food_palace, item_name)

        elif option == 6:
            print("break")
            break

        else:
            print("Invalid")


while True:
    print(f"Welcome !!")
    print(f"----------")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    option = int(input("Enter your Option: "))

    if option == 1:
        customer_menu()

    elif option == 2:
        admin_menu()

    elif option == 3:
        print(f"\nHave A Good Day Buddy !!")
        print(f"--------------------")
        break

    else:
        print("Invalid")
