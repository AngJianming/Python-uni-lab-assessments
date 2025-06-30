'''def calculate(num1_str, num2_str, operator):

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
'''
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
'''
for i in range(10):
  print(i, sep=" ")
'''
'''
x = 1   #int
y = 2.0 #float
z = "3" #str

x = str(x)
y = str(y)
z = str(z)


print(x)
print(y)
print(z*3)
'''

'''
num1, num2, num3, num4 = input("Enter four number from 1 to 1000 e.g. '1,11,111,1000': ").split(',')
print(num1, num2, num3, num4)

'''


# Python assignment


MAX_LOGIN_ATTEMPTS = 3
INITIAL_STOCK = 100
ROLES = {"ADMIN": 1, "INVENTORY_CONTROLLER": 2}


class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
        self.login_attempts = 0

    def verify_login(self, entered_password):
        if entered_password == self.password:
            self.login_attempts = 0
            return True
        else:
            self.login_attempts += 1
            return False


class InventoryItem:
    def __init__(self, item_code, supplier_code, quantity):
        self.item_code = item_code
        self.supplier_code = supplier_code
        self.quantity = quantity


def create_inventory_file():
    if not os.path.exists("ppe.txt"):
        with open("ppe.txt", "w") as file:
            # Assuming 6 PPE items (modify based on Table 1)
            for item_code in ["HC", "FS", "MS", "GL", "GW", "SC"]:
                file.write(f"{item_code}, -, {INITIAL_STOCK}\n")
        print("Initial inventory data created in ppe.txt")


def create_supplier_file():
    if not os.path.exists("suppliers.txt"):
        with open("suppliers.txt", "w") as file:
            file.write("# Supplier Code, Supplier Name, Contact Information\n")
        print("suppliers.txt file created for adding supplier details.")


def load_inventory_data():
    inventory = []
    if os.path.exists("ppe.txt"):
        with open("ppe.txt", "r") as file:
            for line in file:
                item_data = line.strip().split(",")
                inventory.append(InventoryItem(item_data[0], item_data[1], int(item_data[2])))
    return inventory


def login():
    users = [  # Replace with actual user data (username, password, role)
        User("admin", "admin123", ROLES["ADMIN"]),
        User("user1", "password1", ROLES["INVENTORY_CONTROLLER"]),
        # Add more users if needed
    ]

    for attempt in range(MAX_LOGIN_ATTEMPTS):
        username = input("Username: ")
        password = input("Password: ")
        for user in users:
            if user.username == username and user.verify_login(password):
                print(f"Login successful for {user.username}")
                return user
        print(f"Invalid username or password. Attempts remaining: {MAX_LOGIN_ATTEMPTS - attempt - 1}")

    print("Login failed after maximum attempts. Terminated from the system.")
    exit()


def update_inventory(inventory):
    item_code = input("Enter item code (HC, FS, MS, GL, GW, SC): ").upper()
    found = False
    for item in inventory:
        if item.item_code == item_code:
            quantity_change = int(input(f"Enter quantity change (+ for increase, - for decrease): "))
            item.quantity += quantity_change
            found = True
            print(f"Inventory for {item_code} updated.")
            break
    if not found:
        print(f"Item with code {item_code} not found in inventory.")


def main_menu(user, inventory):
    while True:
        print("\nMain Menu:")
        if user.role == ROLES["ADMIN"]:
            print("1. View Inventory Report")
            print("2. Manage Suppliers (create, edit, view)")
            print("3. Exit")
        else:
            print("1. View Inventory Report")
            print("2. Update Inventory (Quantity)")
            print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print_inventory_report(inventory)
        elif choice == '2' and user.role == ROLES["ADMIN"]:
            manage_suppliers()
        elif choice == '2' and user.role == ROLES["INVENTORY_CONTROLLER"]:
            update_inventory(inventory)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")













