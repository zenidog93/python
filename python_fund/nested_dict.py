#update values in dictionaries and lists
x = [ [5,2,3], [10,8,9] ] 

#1
x[1][0]=15
print(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
#2
students[0]['last_name']= 'Bryant'
print(students[0])

sports_directory = {
'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
#3
sports_directory['soccer'][0] ='Andres'
print(sports_directory['soccer'])

z = [ {'x': 10, 'y': 20} ]

#4
z[0]['y'] =30
print(z)

#iterate through a list of dictionaries

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(list_given):
    #print(list_given)
    for each_dict in list_given:#goes through each dict from the list given
        #print(each_dict)
        for each_key in each_dict: #goes through each key from within the dict we are in
            print(f'{each_key} - {each_dict[each_key]}')
    
    
def iterateDictionary2(key_name, list_given):
    for each_dict in list_given:
        print(each_dict[key_name])

    

iterateDictionary(students)

iterateDictionary2('first_name', students) 
iterateDictionary2('last_name', students) 

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for each_key in some_dict: #goes through each key in our dictionary
        print(len(some_dict[each_key]), each_key) #prints out the length of the element and prints out the name of that key
        for element in some_dict[each_key]: #goes through each element in the list
            print(element) #prints out the element

printInfo(dojo) # calls the function printInfo with argument dictionary Dojo
