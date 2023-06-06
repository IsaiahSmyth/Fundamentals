# variable declaration
# number
# Initialize
num1 = 42

# float
num2 = 2.3

# boolean
boolean = True

# string
string = 'Hello World'

# list
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

# libuary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

# tubple
fruit = ('blueberry', 'strawberry', 'banana')

# Type check
# list
# change value
print(type(fruit))

# log statement
# list
# # access value
print(pizza_toppings[1])

# list
# add value
pizza_toppings.append('Mushrooms')

# Dictionary
# access value
print(person['name'])

# Dictionary
# change key
person['name'] = 'George'

# dictionary
# change value
person['eye_color'] = 'blue'

# tuple
# access value
print(fruit[2])


# condition
# if
if num1 > 45:
    print("It's greater")

# condition 
# else
else:
    print("It's lower")

# length check
# if statement
if len(string) < 5:
    print("It's a short word!")

# if statement
# elif statement
elif len(string) > 15:
    print("It's a long word!")

# else statement
else:
    print("Just right!")

# for loop
for x in range(5):
    print(x)

# for loop
for x in range(2,5):
    print(x)

# for loop
for x in range(2,10,3):
    print(x)
x = 0

# while loop
while(x < 5):
    print(x)
    x += 1

# list
# delete value
pizza_toppings.pop()

# list
# delete value
pizza_toppings.pop(1)


# libuary
print(person)
# libuary
# delete value
person.pop('eye_color')
print(person)

# for loop
# start
for topping in pizza_toppings:
    # if statement
    if topping == 'Pepperoni':
        # continue
        continue
    print('After 1st if statement')
    # if statement
    if topping == 'Olives':
        # break
        # stop
        break

# function
def print_hello_ten_times():
    # for loop
    for num in range(10):
        print('Hello')

# parameter
print_hello_ten_times()

# function
# parameter
def print_hello_x_times(x):
    # for statement
    for num in range(x):
        print('Hello')

# parameter
print_hello_x_times(4)

# function
# parameter
def print_hello_x_or_ten_times(x = 10):
    # for loop
    for num in range(x):
        print('Hello')

# parameter
print_hello_x_or_ten_times()
# parameter
print_hello_x_or_ten_times(4)

# comment
# multi line
"""
Bonus section
"""

# comments
# single lines

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)