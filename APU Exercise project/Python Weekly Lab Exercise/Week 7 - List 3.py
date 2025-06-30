# Part A: List
#1.	Generate the output from the following program. Understand how the program works.
'''
my_list = [1.6, 2.7, 3.8, 4.9]
new_list = []
a_list = []

for val in my_list:
    temp = str(val)
    a_list.append(temp.split('.'))

for val in a_list:
    new_list.append(int(val[0]))
my_str = ':' . join(val)

print(my_list)
print(a_list)
print(new_list)
print(val)
print(my_str)
'''

#List are not like string, they are mutable which can change item in list.
#2.
'''
my_list1 = ['bye', 'mother', 'dad', ['halmeoni', 'grandpa']]
new_list1 = ['hi', 'mom', 'father', my_list1[3]]  # Access sub-list using index

print(my_list1)
print(my_list1)
print(new_list1)
'''

#3. Given numList = [1,3,5,5,2]. Write a program that:
# a. Sort the list.
# b. Adds 4 at the end of the list
# c. Remove on duplicate
# d. Insert 6 at index 4
# e. Print the number of items in the list.
'''
numList = [1,3,5,5,2]

# a. Sort the list.
numList.sort()
print("Sorted list:", numList) 

# b. Add 4 at the end of the list
numList.append(4)
print("List with 4 appended:", numList)

# c. Remove duplicates (converting to set and back to list preserves order)
new_list2 = list(set(numList))
print("List with duplicates removed:", new_list2)

# d. Insert 6 at index 4
new_list2.insert(4, 6)
print("List with 6 inserted at index 4:", new_list2)

# e. Print the number of items in the list.
print("Number of items:", len(new_list2))
'''

#Part B: Self Test
#1.	Write a Python code to create a list number using these number = 65, 75, 85, 95, 105
#   and check number that prompt the user to enter a number to check that number is available or not in list.
'''
my_list3 = [65, 75, 85, 95, 105]
user_input3 = int(input("Enter a number to check if that number is is available or not: "))

if user_input3 in my_list3:
    print("The number you have entered is available")
else:
    print("The number you have entered is not available")
'''

#2.	Write a Python program to shuffle and print a specified list.
#   food = [“cookies”, “brownies”, “cake”, “ice cream”, “chocolate”]
'''
food = ["cookies", "brownies", "cake", "ice cream", "chocolate"]

from random import shuffle
shuffle(food)

print("Shuffled food list:", food)
'''

#3. Write a Python program to get the difference between the two lists.
'''
list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8]

# Convert lists to sets to eliminate duplicates
set1 = set(list1)
set2 = set(list2)

# Difference between sets using the difference operator (-)
difference = set1.difference(set2)

# Convert the difference set back to a list (optional)
difference_list = list(difference)

print("Difference between lists:", difference_list)
'''

#4. Write a Python program to convert a list of characters into a string.
'''
characters_list = ['h', 'e', 'l', 'l', 'o']

# Join the characters in the list using the join() method
joined_string = ''.join(characters_list)

print("Converted string:", joined_string)
'''


#5. Write a Phyton program to generate the expected output as below:
#   Given list is [100, 200, 300, [“turmeric”, “galanga”, [“kiwi”, “apple”, “oranges”]], 50, 60, 70]
'''
given_list = [100, 200, 300, ["turmeric", "galanga", ["kiwi", "apple", "oranges"]], 50, 60, 70]

# Access the nested list of fruits while preserving the original list structure
fruits = given_list[3][2]  # Access the third element, then its second element (fruits sublist)

# Optionally flatten the fruits list if you don't need the nested structure
# flat_fruits = fruits[:]  # Create a copy to avoid modifying the original list

# Expected output with clear labeling and formatting
output = """Given list:
{}

Extracted fruits:
{}""".format(given_list, fruits)  # Using f-strings for formatted string literals

print(output)
'''


















































