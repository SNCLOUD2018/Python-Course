my_variable = 'hello'
my_list_variable = ['hello', 'hi', 'nice to meet you']
my_tuple_variable = ('hello', 'hi', 'nice to meet you')
my_set_variable = {'hello', 'hi', 'nice to meet you'}

print(my_list_variable)
print(my_tuple_variable)
print(my_set_variable)

my_short_tuple_variable = ("hello",)
another_short_tuple_variable = "hello",

print(my_list_variable[0])
print(my_tuple_variable[0])
#print(my_set_variable[0])  # This won't work, because there is no order. Which one is element 0?

my_list_variable.append('another string')
print(my_list_variable)

#my_tuple_variable.append('a string')  # This won't work, because a tuple is not a list.
my_tuple_variable = my_tuple_variable + ("a string",)
print(my_tuple_variable)
#my_tuple_variable[0] = 'can I change this?'  # No, you can't

my_set_variable.add('hello')
print(my_set_variable)
my_set_variable.add('hello')
print(my_set_variable)


# len function gives the length of list, dictionary, sets.
grades = [5, 4, 7, 8]

print(len(grades))

#sum is used to get the sum of numbers in list, tuples.
print(sum(grades))