
#loops

#for loops

# for _iterator__ in __collection range()___:
#range() - is a function that returns a sequence of numbers

#range() by default, the start is 0 and the iterator increase by one automatically

# for i in range(10):
#     print(i)
    

# ? iterate ove a list

our_list = ['pizza', 'cheese', 'ramen', 'sushi']

# print(our_list)

for i in range(len(our_list)):
    pass
    # print(our_list[i])
    
for food in our_list:
    pass
    # print(food)
    
#Dictionaries

cat1 = {
    'name' : 'Pickles',
    'age' : 4,
    'color' :'black'
}
cat2 = {
    'name' : 'Keo',
    'age' : 2,
    'color' :'brown'
}

cat_list = [cat1, cat2]
#print(cat_list) prints out a list with two elements. each element is a dictionary
# [{'name': 'Pickles', 'age': 4, 'color': 'black'}, {'name': 'Keo', 'age': 2, 'color': 'brown'}]

for one_cat in cat_list:
    #print(one_cat)
    for cat_key in one_cat:
        pass
        #print(one_cat[cat_key])

# print(cat1['name'])

for key in cat1:
    pass
    # print(key, cat1[key])
    

capitals = {"Washington":"Olympia",
            "California":"Sacramento",
            "Idaho":"Boise",
            "Illinois":"Springfield",
            "Texas":"Austin",
            "Oklahoma":"Oklahoma City",
            "Virginia":"Richmond"
}
# another way to iterate through the keys
for val in capitals.values(): #prints out the values for each key
    pass
    # print(val)
for val in capitals.keys(): #prints out the keys in the dictionary
    pass
    # print(val) 
    
person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
# Adds a new key value pair for email to person
person["email"] = "alovelace@codingdojo.com"
        
# Changes person's "last" value to "Bobada"
person["last"] = "Bobada"
#print(person)

# if "email" not in person:
#     person["email"] = "newemail@email.com"
# else:
#     print("Would you like to replace your existing email?")


countries_so_far = {"Mexico": 1, "Morocco": 1}
new_visits = ["Albania", "Mexico", "Togo", "Morocco"]
    
# To add Albania to the list
countries_so_far["Albania"] = 1
# To add 1 to the Mexico tally
countries_so_far["Mexico"] += 1 # Changes Mexico tally to 2!
# your code here to finish updating your travel log!

#print(countries_so_far)

my_dict = { "name": "Noelle", "language": "Python" }
for each_key in my_dict:
    pass
    #print(each_key)
# output: name, language

my_dict = { "name": "Noelle", "language": "Python" }
for each_key in my_dict:
    print(my_dict[each_key])
# output: Noelle, Python

