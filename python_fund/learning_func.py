def add(a,b): # a and b are the parameters
    x = a + b
    return x

new_val= add(3,5) #3 and 5 are the arguments
print(new_val)
#prints out 8 by calling the function add with paramaters a =3 and b =5


def say_hi(name): #name is the parameter
    print("Hi, " + name)
    
say_hi("Marco") #'Marco' is the argument being passed into the function say_hi
say_hi("Alberto")

#a function call is equal to whatever that function RETURNS

def say_bye(name):
    return "Bye, " + name

goodbye= say_bye("Polo")
print(goodbye)

#returns also means exiting
#print statments are for debugging
#printing something does not save any information
# returning statements will provide us an output


def full_name(first, second):
    return f"{first} {second}"

name2= full_name("billy", "Bob")
name1= full_name("Marco", "Polo")
print(name1)
print(name2)

def multiply(num_list, num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
# >>>[2,4,10,16]
