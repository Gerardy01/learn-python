




class Employee:

    total_employee = 0
    raise_ammount = 1.04
    
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = f'{first_name.lower()}.{last_name.lower()}@gmail.com'

        Employee.total_employee += 1

    def get_full_name(self):

        if len(self.last_name) == 0:
            return f'{self.first_name}'

        return f'{self.first_name} {self.last_name}'

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_ammount)



    @classmethod
    def set_raise_amount(cls, ammount):
        cls.raise_ammount = ammount

    @classmethod
    def from_string_employee(cls, string):
        first, last, salary = string.split('-')
        
        return cls(first, last, salary)


    
    @staticmethod # use static if we not gonna access the cls argument
    def is_working_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True




employee_one = Employee('Budi', 'Wicaksono', 20000000)
employee_two = Employee('Agung', '', 10000000)

print(employee_two.get_full_name())

Employee.set_raise_amount(1.05)
employee_one.apply_raise()

print(employee_one.salary)
print(employee_two.salary)



employee_three = Employee.from_string_employee('Yono-Jhon-50000000')

print(employee_three.get_full_name())


import datetime
my_date = datetime.date(2022, 10, 20)

print(Employee.is_working_day(my_date))





class Developer(Employee):
    
    def __init__(self, first_name, last_name, salary, device):
        super().__init__(first_name, last_name, salary) # super constructor
        
        self.device = device


dev_one = Developer('Tono', 'Sutino', 100000000, 'Laptop')

print(dev_one.get_full_name())
print(dev_one.device)

print(dev_one.salary)
dev_one.set_raise_amount(1.10)
dev_one.apply_raise()
print(dev_one.salary)





class Manager(Employee):

    def __init__(self, first_name, last_name, salary, employees = None):
        super().__init__(first_name, last_name, salary) # super constructor

        if employees == None:
            self.employees = []
        else:
            self.employees = employees
    


    def add_employees(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
    
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
    


    def get_employees(self):
        list_employee = []

        for emp in self.employees:
            list_employee.append(emp.get_full_name())
        
        return list_employee
    
    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.get_full_name())



manager_one = Manager('Jono', 'Baba', 200000000, [employee_one])

manager_one.add_employees(dev_one)

print(manager_one.get_employees())
manager_one.print_employees()



print(isinstance(manager_one, Employee)) # True 
print(issubclass(Manager, Developer)) # False

    