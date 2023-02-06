num1 = 42 #number
num2 = 2.3 # numbers spec a float
boolean = True #boolean data type
string = 'Hello World'
print(len(string))
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # list data type
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  #dictionary
fruit = ('blueberry', 'strawberry', 'banana') #tuples
print(type(fruit)) #type check
print(pizza_toppings[1]) #asking to print what is in index one in list pizza_toppings 
pizza_toppings.append('Mushrooms') #adding mushrooms to the end
print(person['name'])#printing the value of key name in dictionary person
person['name'] = 'George' #changing the value of name to be George
person['eye_color'] = 'blue' #adding the value of eye color to blue since there is no eye color before
print(fruit[2]) #print index two in tuple fruit

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
#would print is lower since num1 is 42 
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
#prints just right since the length of the first string in string is 11 between 5 and 15 characters
for x in range(5):
    print(x)
    #prints 0,1,2,3,4
for x in range(2,5):
    print(x)
    #prints 2,3,4
for x in range(2,10,3):
    print(x)
    #prints 2,5,8. starts at 2 until x is less than 10 and increases 3 every time
x = 0
while(x < 5):
    print(x)
    x += 1
    #prints 0,1,2,3,4

pizza_toppings.pop()
#takes of the last index in pizza toppings which is mushrooms
pizza_toppings.pop(1)
# removes the index 1 from list pizza topings

print(person)
#prints dictionary person
person.pop('eye_color')
#removes the last inded in dictionary person
print(person)
#prints the new dictionary person

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()
#calls function will print hello 10 times. from 0 to 9

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)
#calls function helloXTimes 4 times. x is the paramater we pass in line 74

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
#calls the function with the parameters that are aready established in line 77. hello is printed 10 times
print_hello_x_or_ten_times(4)
#calls function with new parameters. hello is printed 4 times


"""
Bonus section
"""

# print(num3)
# num3 = 72
#won't run becuase num 3 is defined after the print request in line 91
# fruit[0] = 'cranberry'
#cannot modify a tuple. Error is dispalyed
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)