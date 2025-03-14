class Employee:
    def __init__(self, employee_name, age, salary):
        self.employee_name = employee_name
        self.age = age
        self.salary = salary
        self.is_active = True
        
    def __str__(self):
        status = "Active" if self.is_active else "Terminated"
        return("{}, {}, {}, {} TL : {}".format(self.employee_name, self.age, self.salary, status))

# A class to hold employees
class Company:
    def __init__(self):
        self.employees = []  # This is defined to add employees later
    
    def add_employee(self, employee):
        self.employees.append(employee)
        print("{} has been added to the company \U00002705".format(employee.employee_name))
        
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            print("{} has been removed from the company.\U0000274C".format(employee.employee_name))
        else:
            print("There is no employee named {}.".format(employee.employee_name))

company = Company()

employee1 = Employee("Aylin", 24, 50000)
employee2 = Employee("Brain", 27, 60000)
employee3 = Employee("Mia", 30, 62000)

company.add_employee(employee1)
company.add_employee(employee2)
company.remove_employee(employee2)
company.add_employee(employee3)
