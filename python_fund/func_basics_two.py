#countdown:
def countdown(num):
    new_list=[]
    for i in range(num, -1, -1):
        new_list.append(i)
    return new_list

result = countdown(10)
#print(result)

#2: print and return
def print_return(list):
    temp_list = []
    for i in list:
        temp_list.append(i)
    #print(temp_list[0])
    return temp_list[1]
x = print_return([1,2])
#print(x)

#3: first plus length
def first_plus_length(list_given):
    sum = 0
    sum = list_given[0] + len(list_given)
    return sum
#y = first_plus_length([1,2,3,4,5, 7])
#print(y)

#4 Values greater than second

def greater_than_second(list_given):
    new_list = []
    min = list_given[1]
    print(min)
    for i in range(0,len(list_given)):
        if list_given[i] > min:
            new_list.append(list_given[i])
    print(len(new_list))
    return new_list

z = greater_than_second([5,2,3,2,1,4])

print (z)

#5 This Length, That Value
def length_value(a,b):
    new_list=[]
    for i in range(0,a):
        new_list.append(b)
    return new_list
list = length_value(4,2)

print(list)