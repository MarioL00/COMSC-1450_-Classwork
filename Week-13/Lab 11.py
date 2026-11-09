''' class Student:
    def __init__(self,n,a, gp):
        self.name = n
        self.age = a
        self.gpa = float(gp)

    def display(self):
        print("This is the student's info: ", self.name, self.age, self.gpa)

    def calculate_gpa(self):
        return self.gpa * 2

s1 = Student("Sara", 18, 3.5)
s2 = Student("Dave", 19, 3.8)
s3 = Student("John", 21, 2.9)
s1.name = "Lara"

s1.display()
s2.display()
s3.display()
print(s1.calculate_gpa()) '''

#Question 1
''' class Book:
    def __init__(self, t, a, p):
        self.title = t
        self.author = a
        self.price = float(p)

    def apply_discount(self, percentage):
        self.price = self.price - (self.price * (percentage/100))

    def get_details(self):
        print("This is the book information: ", self.title, self.author, self.price)

s1 = Book("Hamlet", "Jacob", ) '''

#Question 2
''' class Rectangle:
    def __init__(self, l, w):
        self.lenght = l
        self.width = w

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display(self):
        return '''

#Question 3

#Question 4

#Question 5
''' class Student:
    def __init__(self, n):
        self.name = n
        self.grades = []

    def add_grade(self, g):
        self.grades.append(g)

    def get_average(self):
        total = 0
        for i in self.grades:
            total = total + i
        res = total/len(self.grades)
        return res

s1 = Student("Dave") '''

#Question 7
class BankAccount:
    def __init__(self, name, balance):
        self.__account_holder = name
        self.__balance = balance

    def get_balance(self):
        return self.get_balance

    def deposit(self, amount):
        if amount > 0:
           self.__balance += amount
        else:
            print("Amount should be positive. ")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Funds. ")      

