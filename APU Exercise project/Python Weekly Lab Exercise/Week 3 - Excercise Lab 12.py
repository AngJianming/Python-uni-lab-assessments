# Part A
# 1)
print("Hello")


# 2) Write a program to get an input word from a user.
# Then, display the given word together with the sentence of “Welcome, ”
name1 = input("Enter your name: ")
welcome_message = "Welcome, " + name1

print(welcome_message)


# 3) Write a program to get two inputs from user.
# Then display the input.

A, B = (input("Enter your name and age: "))
welcome_message1 = "Your name is: " + A
welcome_message2 = "and Your age is: " + B
print(welcome_message1 and welcome_message2)


# Part B
# 1. Write a pseudocode and python program to convert the distance in mile to kilometer.
# Set KM per mile to 1.609 and distance mile to 100. Prompt the distance in mile from the user and display the distance in kilometer.
'''
Start
    Declare "mile , km"
    Prompt "Enter the distance in miles", mile
    Calculate "km = mile * 1.609"
    Print "The distance in km is: km"
'''

mile = int(input("Enter the distance in miles: "))
km = mile * 1.60934
print("The distance converted to kilometer is: ", km)


# 2. Accept 2 numbers from user and display average of it.
num1, num2 = input("Enter two numbers to find avgNum: ").split(',')
avgNum = (int(num1) + int(num2)) / 2
print("The average number is: ", avgNum)


# 3. Accept 2 input values from user and do arithmetic operation. (+, -, *, /, %).
def calculate(num1_str, num2_str, operator):

  try:
    num3 = float(num1_str)
    num4 = float(num2_str)
  except ValueError:
    print("Invalid input. Please enter numbers.")
    return None

  if operator == "+":
    return num3 + num4
  elif operator == "-":
    return num3 - num4
  elif operator == "*":
    return num3 * num4
  elif operator == "/":
    if num4 == 0:
      print("Error: Division by zero is not allowed.")
      return None
    else:
      return num3 / num4
  elif operator == "%":
    if num4 == 0:
      print("Error: Modulo by zero is not allowed.")
      return None
    else:
      return num3 % num4
  else:
    print("Invalid operator. Please use +, -, *, /, or %.")
    return None

userNum = input("Enter two numbers separated by a comma (e.g., 5,3): ")

try:
  num1_str,num2_str = userNum.split(',')
except ValueError:
  print("Invalid input. Please enter numbers separated by a comma.")
  exit()

operator = input("Enter an operator (+, -, *, /, %): ")

result = calculate(num1_str.strip(), num2_str.strip(), operator)
if result is not None:
  print(f"The result of {num1_str} {operator} {num2_str} is {result}")



# 4. Accept a numbers from user and print either a number is even or not.
def CheckNum5(num5):
  if num5 % 2 == 0:
    print(f"The number {num5} is even.")
  else:
    print(f"The number {num5} is odd.")

while True:
  try:
    num6 = input("Enter a number: ")
    num5 = int(num6)  # Convert input to integer
    break  # Exit the loop if input is valid
  except ValueError:
    print("Invalid input. Please enter a number.")

CheckNum5(num5)



# 5. Write a program to prompt the maximum and minimum temperature readings on a particular day,
# accept those readings as integers, and calculate and display to the screen the average temperature,
# calculated by (maximum temperature + minimum temperature)/2.
while True:
  try:
    max = input("Enter the maximum temperature in Degree Celsius: ")
    maxTemp = int(max)
    break
  except ValueError:
    print("Invalid input. Please enter an integer for the maximum temperature.")


while True:
  try:
    min = input("Enter the minimum temperature (integer): ")
    minTemp = int(min)
    break
  except ValueError:
    print("Invalid input. Please enter an integer for the minimum temperature.")

# Calculate the average temperature
averageTemp = (maxTemp + minTemp) / 2

# Print the average temperature
print(f"The average temperature is {averageTemp} Degrees Celsius.")



# 6. Write a pseudocode and python code to accept Basic from an employee and calculate salary of an employee by considering following things.
# (Grade_pay is double of Basic. DA is 70% of Basic. TA is RM 200. HRA is 20% of Basic.)(Formula for salary = Grade_pay + DA + TA + HRA).
'''
Start
    Declare "Function calculate_salary(basic_salary): "
    Declare "basic"
    Prompt "Enter the employee's basic salary (RM): ", basic
    Set "basic_salary = float(basic)"
    Set "grade_pay = Multiply basic_salary by 2"
    Set "da (Dearness Allowance) = Multiply basic_salary by 0.7"
    Set "travel_allowance = Assign a fixed value of 200"
    Set "house_rent_allowance = Multiply basic_salary by 0.2"
    Calculate "total_salary = Add grade_pay + da + travel_allowance + house_rent_allowance"
    Return "total_salary = Return the calculated total salary."
    Print f"The employee's total salary is RM {total_salary:.2f}."
End'''

def calculate_salary(basic_salary):

  grade_pay = basic_salary * 2


  da = basic_salary * 0.7


  travel_allowance = 200


  house_rent_allowance = basic_salary * 0.2


  total_salary = grade_pay + da + travel_allowance + house_rent_allowance

  return total_salary


while True:
  try:
    basic = input("Enter the employee's basic salary (RM): ")
    basic_salary = float(basic)
    if basic_salary < 0:
      print("Invalid input. Basic salary cannot be negative.")
      continue
    break  # Exit the loop if input is valid (positive number)
  except ValueError:
    print("Invalid input. Please enter a number for the basic salary.")

# Calculate and display the total salary
total_salary = calculate_salary(basic_salary)
print(f"The employee's total salary is RM {total_salary:.2f}.")


