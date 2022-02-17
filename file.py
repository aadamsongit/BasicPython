num1 = 42 ## variable declaration, data type (numbers)
num2 = 2.3 ## variable declaration, data type (numbers)
boolean = True ## data types (boolean)
string = 'Hello World' ## data types (string)
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] ## data types, composite
## data types, list (?)
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
## data types, dictionary
fruit = ('blueberry', 'strawberry', 'banana')
## data types, list (?)
print(type(fruit)) ## log statement (?)
print(pizza_toppings[1]) ## log statement (?)
pizza_toppings.append('Mushrooms') ## list, add value
print(person['name']) ## list, access value
person['name'] = 'George' ## initialize
person['eye_color'] = 'blue' ## initialize
print(fruit[2]) ## log statement (?)

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

    ## conditional (else/if)

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

    ## conditional (else/if)

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)

    ## for loop

x = 0
while(x < 5):
    print(x)
    x += 1

# while loop


pizza_toppings.pop() # list, delete value
pizza_toppings.pop(1) # list, delete item value

print(person) # log dictionary
person.pop('eye_color') # remove/delete value
print(person) # log new dictionary

for topping in pizza_toppings:
    if topping == 'Pepperoni': ## if statement
        continue ## continue statement
    print('After 1st if statement')
    if topping == 'Olives': ## if statement
        break ## break

def print_hello_ten_times(): ## function
    for num in range(10): # parameter
        print('Hello') ## return

print_hello_ten_times()

def print_hello_x_times(x): ## function
    for num in range(x): ## parameter
        print('Hello') ## return

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): ## function
    for num in range(x): ## parameter
        print('Hello') ## return

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)