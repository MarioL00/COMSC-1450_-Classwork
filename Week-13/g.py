class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def display(self):
        print(self.name, self.age, self.address)

class Student(Person):
    def __init__(self, name, age, address, gpa):
        super().__init__(name, age, address)
        self.gpa = gpa
    def display(self):
        super().display()
        print(self.gpa)
class Employee(Person):
    def __init__(self, name, age, address, salary):
        super().__init__(name, age, address)
        self.salary = salary
class TA(Person):
    pass

s1 = Student("Sara", 19, "TX",3.5)
#print(s1.gpa)
s1.display()

e1 = Employee("Dave", 39, "TX", 4000)
print(e1.salary)
