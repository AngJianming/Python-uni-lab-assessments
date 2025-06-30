#Q1
'''
num1 = input("Enter a the number 1: ")
num2 = input("Enter a the number 2: ")

if num1 >= num2:
    print(f"{num1} is greater than {num2}")
elif num2 < num1:
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} and {num2} are equal")
'''
import array

#Q2
'''
amount_order = int(input("Enter order amount RM: "))
invoice = int(input("Enter number of day invoice issue: "))

if amount_order > 1000 and invoice <= 10:
    result = float(amount_order - (amount_order * 0.04))
    print(f"Amount due RM: {result}")
elif 500 <= amount_order <= 1000 and invoice <= 10:
    result = float(amount_order - (amount_order * 0.02))
    print(f"Amount due RM: {result}")
elif amount_order < 500:
    float(amount_order)
    print(f"Amount due RM: {amount_order}")
'''

#Q3
'''
salary = int(input("Enter your monthly salary RM: "))
if salary > 5000:
    expenses = float(salary - (salary * 0.5))
    entertainment = float(salary - (salary * 0.8))
    investment = float(salary - (salary * 0.7))
    print(f"Your monthly budget is \nfix expenses: {expenses} \nentertainment: {entertainment} \ninvestments: {investment}")
elif salary <= 5000:
    expenses = float(salary - (salary * 0.2))
    entertainment = float(salary - (salary * 0.9))
    investment = float(salary - (salary * 0.9))
    print(f"Your monthly budget is \nfix expenses: {expenses} \nentertainment: {entertainment} \ninvestments: {investment}")
'''

#Q4
'''
food_prices = {
    "1": 450,
    "2": 600,
    "3": 370,
    "4": 240
}


notes = [500, 1000, 2000]
max_order = 3

def get_food_choice():

  while True:
    food_choice = input("Enter food (1 = tuna_sandwich {RM 4.50}, 2 = mini_beef_burger {RM 6.00}, 3 = sardine_sandwich {RM 3.70}, 4 = egg_mayo_sandwich {RM 2.40}): \n")
    if food_choice in food_prices:
      return food_choice
    else:
      print("Invalid food choice. Please try again.")

def calculate_total(food_choices):

  total = 0
  for food in food_choices:
    total += food_prices[food]
  return total

def collect_payment():

  total_payment = 0
  while True:
    denomination = int(input(f"Enter note ({', '.join(str(d) for d in notes)}): "))
    if denomination not in notes:
      print("Invalid denomination. Please enter a valid value.")
    else:
      total_payment += denomination
      break
  return total_payment

def calculate_balance(payment, total):

  balance = payment - total
  if balance > 0:
    print(f"Your change is ${balance/100:.2f}")

    for denomination in notes[::-1]:
      while balance >= denomination:
        balance -= denomination
        print(f"Dispensing ${denomination/100:.2f}")

def main():

  food_choices = []
  total_cost = 0

  # Get food choices until user chooses to checkout or reaches max items
  while len(food_choices) < max_order:
    food_choice = get_food_choice()
    food_choices.append(food_choice)
    total_cost += food_prices[food_choice]
    print(f"Current total: ${total_cost/100:.2f}")
    more_items = input("Do you want to buy more items (y/n)? ").lower()
    if more_items != "y":
      break


  payment = collect_payment()
  calculate_balance(payment, total_cost)


  print("\nReceipt")
  for food in food_choices:
    print(f"{food.capitalize()}: ${food_prices[food]/100:.2f}")
  print(f"Total: ${total_cost/100:.2f}")
  print(f"Payment: ${payment/100:.2f}")
  print("Thank you!\n")

main()
'''

#Q5
'''
user_name = input("Enter your name: ")
purchase_amount = int(input("Enter your purchase amount RM: "))
tax_code = int(input("Enter the tax code: "))
error = False


if tax_code == 0:
  amount_due = purchase_amount
  print(f"Miss/Mister {user_name}")
  print(f"Your amount due after tax exempted 0% is: RM{amount_due} ")
elif tax_code == 1:
  amount_due = purchase_amount + (purchase_amount * 0.06)
  print(f"Miss/Mister {user_name}")
  print(f"Your amount due after good tax 6% is: RM{amount_due}")
elif tax_code == 2:
  amount_due = purchase_amount + (purchase_amount * 0.16)
  print(f"Miss/Mister {user_name}")
  print(f"Your amount due after good tax and service 16% is: RM {amount_due}")
'''



