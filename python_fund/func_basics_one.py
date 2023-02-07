# #1
# def number_of_food_groups():
#     return 5
# print(number_of_food_groups())

##prediction returns '5'
# #
# #2
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# #predictions: error since we do not have one of the functions defined. 

# #3
# def number_of_books_on_hold():
#     return 5
#     return 10
# print(number_of_books_on_hold())

#predictions: prints just '5' since the return exits out the function regardless of what else may be in it

# #4
# def number_of_fingers():
#     return 5
#     print(10)
# print(number_of_fingers())
# #prediction: also only prints out '5' since the return exits our function

# #5
# def number_of_great_lakes():
#     print(5)
# x = number_of_great_lakes()
# print(x)
#prediction: prints out the number '5' since we are calling the function and the function prints something out. However, we are not printing it a second time because the function number_of_great_lakes returns none


# #6
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))

# #prediction:error because the function add is not returning anything

# #7
# def concatenate(b,c):
#     return str(b)+str(c)
#     print(concatenate(2,5))
# #predictions: nothing is happening because we never call the functions

# #8
# def number_of_oceans_or_fingers_or_continents():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(number_of_oceans_or_fingers_or_continents())
# #prints 100 first becuase of line 53 and then it prints 10 becuae b = 100 which meets the condition for else in line 56 

# #9
# def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# #prediction: since 2 is less than 3, prints out 7 with the return
# print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# #prediction: since 5 is not less than 3, prints out 14
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# #prediction: prints out 21 since the return for function(2,3) is 7 and the return for function(5,3) is 14 and we are printing the sum. 



# #10
# def addition(b,c):
#     return b+c
#     return 10
# print(addition(3,5))

# #prediction: we print out the function addition(3,5) which is returns b+c which is 3+5 in this case it prints out 8


# #11
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
# print(b)
# foobar()
# print(b)

# #prediction: prints out 500, prints out 500 again for line 93, prints out 300 bc the function foobar is called, prints out 500 again


# #12
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# foobar()
# print(b)

# #prediction: prints out 500 for line 102, prints out 500 again for line 107, prints out 300 bc the function foobar is called, prints out 500


# #13
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=foobar()
# print(b)

# #prediction: prints out 500 for line 116, prints out 500 again for line 121, prints out 300 bc the function foobar is called, prints out 300 bc now b stores whatever the function returns


# #14
# def foo():
#     print(1)
#     bar()
#     print(2)
# def bar():
#     print(3)
# foo()

# #prediction: calls function foo, prints '1', calls function bar, prints '3' from that function, comes back to function foo and prints out '2'

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#prediction: prints '1', prints '3', prints 5, prints 10