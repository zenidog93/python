# print("Hello World!")

# x = "What's up, World!"
# print(x)
# y = 32
# z = '8'
# print (y +int(z))

# name = 'Marco Polo'
# age = '29'

# print('Hello', name)

# print('Hello ' + name)

# print('Hello ' + name + ', age: '+ age)

#String Interpolation

first_name = "Marco"
last_name = "Polo"
age = 29
print(f"My name is {first_name} {last_name} and I am {age} years old.")

hobbie = 'snowboard'
favorite_food = 'Pad Thai'
print(f"My favorite dish is {favorite_food} and I enjoy to {hobbie}")

first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.

fav_hobbie = 'snowboard'
fav_food ='Pad Thai'
print('My favorite dish is {} and I enjoy to {}'.format(fav_hobbie, fav_food))

hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3 
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27

'''
'''
