#1. Write a program using function with parameters that accepts three arguments and print the values.
'''
def three_value(a, b, c):
    print(a, b, c)

three_value("Hi", "Welcome", "to the real world!")
'''

#2. Write a program to create function calc() that will accept two variables and calculate the two variables.
# Hint: Use addition and subtraction.
'''
def calc(x,y):
    return x + y
"""Two spacing as shown below vv"""


result = calc(40, 10)
print(result)
'''

#3.	Write a program to create a function named employee() using the following conditions:
# a. Program should accept the employee’s name and salary and display both.
# b. If the salary is missing in the function call, then assign default value 9000 to salary.
'''
def employee(employee_name, employee_salary=9000):
  print(f"Employee Name: {employee_name}")
  print(f"Salary: ${employee_salary}")


name1 = input("Enter your name e.g 'Ang': ")
salary1 = input("Enter your salary (RM) e.g '12000': ")
employee(name1, salary1)
'''

#4.	Write a Python program to create the following:
# a.	Create an outer function that will accept two parameters, y and z.
# b.	Create an inner function inside that will calculate the addition of y and z.
# c.	Lastly, the outer function will add 5 into addition and return it
'''
def outer_function(y, z):


  def inner_function():
    """
    This inner function calculates the sum of y and z.
    """
    return y + z


  sum = inner_function()
  return(sum + 5)


y = int(input("Enter the first number: "))
z = int(input("Enter the second number: "))

result = outer_function(y, z)
print(result)
'''

#5.	Generate a Python list of all the odd numbers between 2 to 50
'''
odd_numbers = [num for num in range(3, 51, 2)]
'''

#6.	Find and print the largest number from the given list [4, 28, 97, 56, 16].
'''
numbers = [4, 28, 97, 56, 16]

largest_number = numbers[0]
for num in numbers:
  if num > largest_number:
    largest_number = num
print(f"Largest number: {largest_number}")
'''



#Part B

#1.	Write the following program to find sum of two numbers using a function.
# Sample input/output:
# Enter first number: 23
# Enter second number: 7
# Sum of the given two numbers is: 30
'''
def sum_of_numbers(num1, num2):
  return num1 + num2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum2 = sum_of_numbers(num1, num2)
print(f"Sum of the given two numbers is: {sum2}")
'''

#2.	Write a Python program to read name of student, TP Number and enter his/her all subject marks in list. Compute the total and percentage (Average) of a student.
# At the end display Name of student, TP Number, Total, Percentage and Grade of that semester by using function as defined below.
# a)	Use Display function to print output.
# b)	Use mark function to accept parameter and return total to Display function.
# c)	Use average function by passing parameter which is generated in mark function.
# d)	Use grade function by passing parameter which is generated in average function.
'''
def get_marks():
  """
  Prompts the user to enter subject marks and returns them as a list.
  """
  num_subjects = int(input("Enter the number of subjects: "))
  marks = []
  for i in range(num_subjects):
    mark = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)
  return marks

def calculate_total(marks):
  """
  Calculates the total marks from the provided list.
  """
  total = sum(marks)
  return total

def calculate_average(total, num_subjects):
  """
  Calculates the average (percentage) from total marks and number of subjects.
  """
  average = total / num_subjects
  return average

def determine_grade(average):
  """
  Assigns a letter grade based on the average score.
  """
  if average >= 80:
    return "A+"
  elif average >= 75:
    return "A"
  elif average >= 70:
    return "B+"
  elif average >= 65:
    return "B"
  elif average >= 60:
    return "C+"
  elif average >= 55:
    return "C"
  elif average >= 50:
    return "C-"
  elif average >= 40:
    return "D"
  else:
    return "F"

def display_student_info(name, TP_number, marks, total, average, grade):
  """
  Prints the student's information in a formatted manner.
  """
  print("Student Information:")
  print(f"Name: {name}")
  print(f"TP Number: {TP_number}")
  print(f"Subject Marks: {marks}")
  print(f"Total Marks: {total}")
  print(f"Average (Percentage): {average:.2f}")  # Format average to 2 decimal places
  print(f"Grade: {grade}")

def main():
  """
  Main function to interact with the user and call other functions.
  """
  name = input("Enter student name: ")
  TP_number = input("Enter student TP number: ")
  marks = get_marks()
  total = calculate_total(marks)
  num_subjects = len(marks)  # Get number of subjects from the length of marks list
  average = calculate_average(total, num_subjects)
  grade = determine_grade(average)
  display_student_info(name, TP_number, marks, total, average, grade)

if __name__ == "__main__":
  main()
'''










