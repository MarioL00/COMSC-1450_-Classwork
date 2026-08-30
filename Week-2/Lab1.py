'''firstname = input("Enter your first name ")
lastname = input("Enter your last name ")

print("Hello" , lastname,"," , firstname)

x = 32
y = "Sara"
z = 3.5

print(type(x), type(y), type(z))


print("A\nB\nC\nD\nE\nF\n")'''

x = "C:\\Users\\rick\\Documents"
# print(x)

y = ''' --SYSTEM MENU--
1. Open File
2. Save File '''
#print (y)

#print( "The professor said, 'Make sure you escape matching quotes!'")
# the sentence above can also be made into a variable and printed out using the print function. 

#lenght = float(input("Enter the length of the rectangle: "))
#width = float(input("Enter the width of the rectangle: "))
#area = lenght * width
#print("The area of the rectangle is:", area)

name = input("Please enter your name: ")
monthly_budget = float(input("Enter your monthly budget: "))
d_foodcost = float(input("Enter your monthly food cost: "))
mo_food = d_foodcost * 30
rem = monthly_budget - mo_food
text = "-- BUDGET SUMMARY --"
print(text)
print(name, "| Food", mo_food, "| Remaining", rem, "|")