from menu import Menu


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        print("Employee List!!")
        print("---------------")
        for employee in self.employees:
            print(
                f"Name:\t{employee.name}\tEmail:\t{employee.email}\tPhone:\t{employee.phone}\tAddress:\t{employee.address}\tAge:\t{employee.age}\tDesignation:\t{employee.designation}\tSalary:\t{employee.salary}"
            )


food_palace = Restaurant("The Food Palace")
