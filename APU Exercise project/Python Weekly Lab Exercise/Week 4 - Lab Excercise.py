# Week 4 – Practices
"""
1) Write a Python program to print the following string in a specific
format (see the output).

Sample String : "Twinkle, twinkle, little star, How I wonder what you
are! Up above the world so high, Like a diamond in the sky. Twinkle,
twinkle, little star, How I wonder what you are"

Sample Output :
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
Twinkle, twinkle, little star,How I wonder what you are
"""
"""
story = '''Twinkle, twinkle, little star,
    How I wonder what you are!
        Up above the world so high,
        Like a diamond in the sky.
Twinkle, twinkle, little star, How I wonder what you are'''

print(story)"""

"""
2) Write a Python program that accepts the user's first and last name and
prints them in reverse order with a space between them.
    Sample Input/Output:
    Input your First Name : Dany
    Input your Last Name : Boon
    Hello Boon Dany
"""
"""
while True:
    try:
        first_name = input("Input your First Name: ")
        last_name = input("Input your Last Name: ")
        fist_name
    except:
        print(f"Hello {last_name} {first_name}")
"""
"""
def Vname(name):

  for char in name:
    if not char.isalpha():
      return False
  return True

def name1(prompt):

  while True:
    name = input(prompt)
    if Vname(name):
      return name
    else:
      print("Invalid input. Please enter a name with only letters.")

first_name = name1("Enter your first name: ")

last_name = name1("Enter your last name: ")

print(f"Hello {last_name} {first_name}")
"""

"""
3) Write a Python program that accepts an integer (n) and computes the
value of n+nn+nnn.
    Sample input/output
    Sample value of n is 5
    Expected Result : 615
"""
"""
n = input("Enter an integer: ")
calculate = (int(n)+int(str(n)*2)+int(str(n*3)))
print("The answer of is: ",calculate)
"""

"""
4) Write a Python program to get the volume of a sphere with radius six.
"""
"""
pi = 3.142
r = 6
volume = ((4/3) * pi * 6**3)
print (f"The volume of a shpere with radius of 6 is: {volume}")
"""

"""
5) Write a Python program to calculate the area of triangle. Accept the
base and height from user.
"""
"""
base_triangle = int(input("Enter the base of the triangle: "))
height_triangle = int(input("Enter the height of the triangle: "))
area_triangle = ((1/2) * base_triangle * height_triangle)
print(f"The area of triangle is: {area_triangle}")
"""

"""
6. Write a Python program that displays your name, age, and address on
three different lines by applying a single print() statement.
"""
"""
name1 = input("Enter your name: ")
age1 = int(input("Enter your age: "))
address1 = input("Enter your address: ")
print(f"Your name is {name1} \nand age is {age1}. \nYou live in {address1}")
"""

"""
7. Write a Python program to solve (x + y) * (x + y).

Sample Input : x = 4, y = 3
"""
"""
x = int(input("Enter the value of x e.g 5: "))
y = int(input("Enter the value of y e.g 10: "))
solve_y_x = ((x+y) * (x+y))
print(f"The equation (x + y) * (x + y) is: {solve_y_x}")
"""

"""
8. Write a Python program to calculate the future value of a specified
principal amount, rate of interest, and number of years.

Sample input/output:
    Input Data : amt = 10000, int = 3.5, years = 7
    Expected Output : 12722.79
"""
"""
amt = 10000
yearsT = 7
rateR = 3.5
principleP = int(float((amt * (1 + (rateR/100)) ** yearsT)))
print(f"The value of compound interest is: {principleP}")
"""

"""
9. Write a Python program to calculate height (in feet and inches) to
centimetres.

Sample Input/Output:
    Input your height:
    Feet: 5
    Inches: 3
    Your height is : 160 cm.
"""
"""
feet1 = int(input("Enter your height in feet: "))
inches1 = int(input("Enter your height in inches1: "))
convert_to_cm = round((feet1 * 30.48) + (inches1 * 2.54),2)
print(f"Your height in cm is: {convert_to_cm}")
"""

"""
10. Write a Python program to calculate all units of time into seconds.

Sample Input/Output:
    Input days: 4
    Input hours: 5
    Input minutes: 20
    Input seconds: 10
    The amounts of seconds 364810
"""
"""
days1 = int(input("Enter the time in days: "))
hours1 = int(input("Enter the time in hours: "))
minutes1 = int(input("Enter the time in minutes: "))
sec1 = int(input("Enter the time in seconds: "))
calculate_in_sec = round((days1 * 86400) + (hours1 * 3600) + (minutes1 * 60),2)
print(f"The time in seconds is: {calculate_in_sec}")
"""

"""
11. Write a Python program to calculate sum of digits of a number.

Sample Output:
    Input a four digit numbers: 5245
    The sum of digits in the number is 16
"""
"""
digit1 = input("Enter a four digit number e.g 1234: ")
sum1 = 0
for i in digit1:
    sum1 += int(i)

print("The value of the 4 digits are: ", sum1)
"""

"""
12. Write a Python program to prompt two numbers on a single line.

Sample input/output:
    Input the value of x & y
    2 4
    The value of x & y are: 2 4
"""
"""
x1,y1 = input("Enter a 1 digit number: ").split(',')
print("The value of x & y are: ",x1,y1)
"""


