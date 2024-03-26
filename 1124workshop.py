'''
This does not affect the code
'''

"""
This does not affect the code
"""

# comments

var1 = 5 #integer
var2 = "I want a coffee" #string
var3 = 9.64654 # floating number

VAR = 10 # Hidden variables (All caps)

var4 = var2
var2 = "something random"

#Built-in functions
type(var4)

var5 = 10
var6 = var5 - var3
var7 = var3 - var5

# String concatenation
var2 + var4

#Type casting
var7 = str(var3)
var2 + var7
var8 = var1 + float(var5)
var5 = float(var5)

#Concatenation

Fname = "Gu"
Lname = "Tsan"

Name = Fname + " " + Lname
Name = Fname + "\n" + Lname
Name = Fname + "\t" + Lname

# String operations
var2 = var2.upper()
var2 = var2.lower()

count = var4.count('e')

print(Name)
Var2 = "something stupid"
del Var2

print("Enter a value")
input_val = input() # Will always be a string

import pandas as pd
import numpy as np
df = pd.DataFrame (
            {"a" : [4,5,6],
             "b" : [7,8,9],
             "c" : [10,11,12]},
        index = [1,2,3])
print(df)

# boolean datatype
var_bool = False
var1 = True

new_var = var5 == 10 #check if equal
new_var = var5 != 5 # check if not equal

var1 = 3.14 #float
var2 = "3.14" #string
var1 == var2
str(var1) == var2

del new_var

# membership operator
var2 = "I want some coffee"
"want" in var2 # check true/false
"coff" not in var2

var2 = var2.upper()
"COFF" in var2

'''
Task 1
1. Create a float var1
2. square the float to var2
3. count the num of 2s in var2
'''
var1 = 3.14
var2 = var1**2
#var2 = pow(var1, 2) # Alternative
var2 = str(var2)
var2.count('2') # count func for string type

my_list1 = [1,2,3,4,5,6]
my_list2 = [1.54, 3, 'this', True]
my_list3 = [my_list1, my_list2, 1, True]
my_list2[2] # Index 2 is 'this'
my_list3[1][1] # Index of lists of lists
my_list3[0]

# Slice data
new_list = my_list3[1:4]

my_list3.append("newstring") # Add elements to list
my_list3.remove(1) # Remove a specific value from the list
my_list3.pop(2) # Remove the element corresponding to the index in the list 
# pop(-1) removes the last element of the list

del new_list[0:1] # Remove elements corresponding to index 0:1

# Dictionary
my_dict = {'key1':1, 'key2':"this is a string"}
my_diict = {'rf':0.01, 'rs':0.05, 'B':2}

my_dict['key2']
popped_var = my_dict.pop('key2')

new_list = [my_dict, "5"]
new_list[0]['key2']

my_list = ['a', 'b', 'c', 'd']
g = my_list.pop(-1)
my_list.insert(1, 'e')

'''
Task 2
Create an interger list of any length and append the highest number divided by 
2 at the end of the list
'''
task_list = [1,6,45,720,90,25,568]
task_list.append(int(max(task_list)/2))

task_list.sort(reverse = True)

# Conditional statement
a = 7
b = 15
list = [-100, 50,25,18,2,0,500]

if a == 7:
    a = 100
    b = 200
    print("We are indside the statement")

a = 20
if a>= 20:
    new_var = 5
    print("I am inside the if condition" + str(new_var))
    
elif a ==20:
    print("I am inside the else if condition")
    new_var = 6
    
else: print("I am inside the else condition")

if "Gu" in Name:
    print("Name has Gu")
    
# Looping

list1 = [1,2,3,4,5,6,7]

for x in list1:
    print(x+1)
    
concat_values = ''

for x in list1:
    concat_values = concat_values + str(2*x)
    print(concat_values)

if len(list1) >6:
    for element in list1:
        print(element)
    print('if block')    
    
for x in list1:
    if x >3:
        print(x)

my_dict = {'a':5,
           'b':"bvalue",
           'c': 9.64}

# print keys
for x in my_dict:
    print(x)

# print values
for x in my_dict:
    print(my_dict[x])

# define 
def return_number_squared(x):
    y = x**2
    return y

return_number_squared(5)

def exists_in_both_lists(l1, l2, find_elem):
    val1 = find_elem in l1
    val2 = find_elem in l2
    return (val1 and val2)

list1 = [1,4,5,6]
list2 = [1,8,5,10,15,100]
list3 = list2

exists_in_both_lists(list3 , list2, 100)

user_input = "None"
while (user_input != 'yes' and user_input != 'no'): 
    print("enter yes or no")
    user_input = input()

'''
Task 3
Creatte a dictionary 
Traverse the dictionary only if number of elements are more than 3 
and print the key:value pairs of value type int.
If dictionary has less than 3 elements, print "invalid dictionary"
'''
test_dict = {'a': 1,
             'b': 2,
             'c': 3,
             'd': 4,
             'e': 5, 
             'f': 6,
             'g': 7,
             'h':8}
if len(test_dict) > 3:
    for x in test_dict:
        if type(test_dict[x]) == int:
            print("Key:" + x)
            print("Value: " + str(test_dict[x]))
        else : 
            print("Not an integer")
else : 
    print("Invalid Dictionary")







