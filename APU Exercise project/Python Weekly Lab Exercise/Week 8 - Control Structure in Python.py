#1.	Write a program that able to print the even number that in the between of 2 to 50.
'''
# Loop from 2 to 50 (inclusive) and check for even numbers
for num in range(2, 50, 2):
    print(num, end='\t')
    while num % 8 == 0:
        print()
        break
'''

#2.	Write a Python program to display numbers from 1 to 20. Note: use all types of repetitive structures
'''
for num1 in range(1, 21):
    print(num1)
'''

#3.	Write a Python program to prompt user to choose their favourite TV channel.
# Use list to store the TV channels. Display the TV channel to the screen when they make the selection.
# Whenever the TV channel entered is not in the list, prompt user either wants to save the new channel or not.
# For the condition in which user wants to save the new channel, it will be displayed together with the existing channels.
# If the channel already exist, prompt user either to continue with the TV channel system or not
'''
print("Welcome to my TV Channel")

channels = ["TV1", "TV2", "TV3", "TV4"]
for channel in channels:
    print(f"        {channel}")
print("")
user1 = input("Enter your desire TV Channel: ")

for i in channels:
    if user1 in channels:
        user2 = input("Channel already exist, would you like to continue with the TV channel system or not? (y/n): ")
        if user2 in str.casefold("y"):
            channels = ["TV1", "TV2", "TV3", "TV4"]
            for channel in channels:
                print(f"        {channel}")
            print("")
            user1 = input("Enter your desire TV Channel: ")
        else:
            print("~~~Thank you for using our TV Channels~~~")
            break
    elif user1 not in channels:
        user2 = input("TV channel entered is not in the list, would you like to save the new channel? (y/n): ")
        if user2 in str.casefold("y"):
            print(f"The TV channel {user1} that you entered is saved")
            user3 = input("Would you like to continue? (y/n): ")
            if user3 in str.casefold("y"):
                channels = ["TV1", "TV2", "TV3", "TV4", f"{user1}"]
                for channel in channels:
                    print(f"        {channel}")
                print("")
                user1 = input("Enter your desire TV Channel: ")
            else:
                print("~~~Thank you for using our TV Channels~~~")
                break
        else:
            print("~~~Thank you for using our TV Channels~~~")
            break
'''

#4.	Use a proper iterative structure to write a program that will read names and exam scores of 10 students.
#   Store all names and scores in the lists. Display student’s name, scores and the class average
#   is to be calculated and printed at the end of the report. Score can range from 0 to 100.
#   Score out of the range is not to be included in the calculations.

# Define maximum login attempts
MAX_LOGIN_ATTEMPTS = 3

# Define initial stock quantity
INITIAL_STOCK = 100

# Define user roles (can be extended for additional roles)
ROLES = {"ADMIN": 1, "INVENTORY_CONTROLLER": 2}


class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
        self.login_attempts = 0

    def verify_login(self, entered_password):
        if entered_password == self.password:
            self.login_attempts = 0  # Reset attempts on successful login
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
    """
    Creates the ppe.txt file with initial inventory data if it doesn't exist.
    """
    if not os.path.exists("ppe.txt"):
        with open("ppe.txt", "w") as file:
            # Assuming 6 PPE items (modify based on Table 1)
            for item_code in ["HC", "FS", "MS", "GL", "GW", "SC"]:
                file.write(f"{item_code}, -, {INITIAL_STOCK}\n")
        print("Initial inventory data created in ppe.txt")


def create_supplier_file():
    """
    Creates the suppliers.txt file for storing supplier details if it doesn't exist.
    You'll need to manually add supplier details later.
    """
    if not os.path.exists("suppliers.txt"):
        with open("suppliers.txt", "w") as file:
            file.write("# Supplier Code, Supplier Name, Contact Information\n")
        print("suppliers.txt file created for adding supplier details.")


def load_inventory_data():
    """
    Loads inventory data from ppe.txt into a list of InventoryItem objects.
    """
    inventory = []
    if os.path.exists("ppe.txt"):
        with open("ppe.txt", "r") as file:
            for line in file:
                item_data = line.strip().split(",")
                inventory.append(InventoryItem(item_data[0], item_data[1], int(item_data[2])))
    return inventory


def login():
    """
    Handles user login with username, password, and attempt tracking.
    """
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
    """
    Allows updating inventory quantity for a specific item.
    """
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
            # Implement function to view inventory report (displaying item details and quantities)
            print_inventory_report(inventory)
        elif choice == '2' and user.role == ROLES["ADMIN"]:
            # Implement functions for managing suppliers
            manage_suppliers()
        elif choice == '2' and user.role == ROLES["INVENTORY_CONTROLLER"]:
            update_inventory(inventory)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")





































