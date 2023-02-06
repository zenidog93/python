# #primative data types-basic building blocks in python

# #booleans

# is_hungry= True;
# print(is_hungry)
# has_frickles = False;
# print(has_frickles)

# #numbers = integers (whole numbers (no decimals)), floating point numbers (numbers with decimals), and complex numbers

# age = 35 # stores a whole number
# print(age)
# weight = 167.32 # stores a floating number
# print(weight)

# #strings = simply text/words

# myName= "Marco Polo"
# #print(myName) 

# #tuples:  type of data that is immutable (meaning you can't modify it once it has been created)
# #   - it can hold a group of values. You can mix and match the data types in here

# car = ('Kate', 'mazda3', 'grey', 13, True)

# #print(car[1]) #output is mazda3
# #print(car) #output is the entire tuple
# #car[3]= 'red'

# #lists: a type of data that is mutable (meaning you can modify) and can hold of group of values
# #usually meant to store related data

# empty_list=[]
# ninjas = ['rozen', 'KB', 'Oliver']
# print(ninjas)
# print(ninjas[2])
# ninjas[1]='Marco'
# print(ninjas)
# ninjas.append('Aaron')
# print(ninjas)
# ninjas.pop(0)
# print(ninjas)
# print(type(ninjas[0])) # finds out the data type for you in case you are unsure. 
# # here we are asking the data type for the index 0 in ninjas; outputs string

empty_dict = {}
new_person = {
        'name': 'John',
        'age': 38, 
        'weight': 160.2, 
        'has_glasses': False
}
new_person['name'] = 'Marco'	# updates if the key exists, adds a key-value pair if it doesn't
new_person['age'] = 30
new_person['weight']= 165.5
new_person['hobbies'] = ['snowboarding', 'coding']
print(new_person)	
# output: {'name': 'Marco', 'age': 30, 'weight': 165.5, 'has_glasses': False, 'hobbies': ['snowboarding', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 165.5
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}        

print(type(new_person))