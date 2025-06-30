import os

MAX_LOGIN_ATTEMPTS = 3
INITIAL_QUANTITY = 100
MIN_STOCK_THRESHOLD = 25
PPE_FILE = "ppe.txt"
SUPPLIERS_FILE = "suppliers.txt"
HOSPITALS_FILE = "hospitals.txt"
DISTRIBUTION_FILE = "distribution.txt"

#Login Func
def login():
    users = {
        "user1": "123",
        "user2": "456",
        "user3": "789",
        "user4": "000"
    }
    attempts = 0

    while attempts < MAX_LOGIN_ATTEMPTS:
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if username in users and users[username] == password:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password. Try again.")
            attempts += 1

    print("Too many failed login attempts. You are terminated from the system.")
    return False

#Create Initial Inventory file
def create_initial_inventory():
    if not os.path.exists(PPE_FILE):
        with open(PPE_FILE, 'w') as file:
            ppe_items = ["HC", "FS", "MS", "GL", "GW", "SC"]
            for item in ppe_items:
                supplier_code = input(f"Enter supplier code for {item}: ")
                file.write(f"{item},{supplier_code},{INITIAL_QUANTITY}\n")
        print("Initial inventory created.")
    else:
        print("Inventory already exists.")

#Update func
def update_inventory():
    item_code = input("Enter item code to update: ")
    update_type = input("Enter 'r' to receive items or 'd' to distribute items: ")
    quantity = int(input("Enter quantity: "))
    
    items = []
    found = False
    
    with open(PPE_FILE, 'r') as file:
        for line in file:
            code, supplier, qty = line.strip().split(',')
            qty = int(qty)
            if code == item_code:
                found = True
                if update_type == 'r':
                    qty += quantity
                elif update_type == 'd':
                    if qty < quantity:
                        print(f"Insufficient stock. Current stock is {qty}.")
                        return
                    qty -= quantity
                else:
                    print("Invalid update type.")
                    return
            items.append(f"{code},{supplier},{qty}\n")
    
    if found:
        with open(PPE_FILE, 'w') as file:
            file.writelines(items)
        print(f"Inventory updated for item {item_code}.")
    else:
        print(f"Item code {item_code} not found.")

#Tracking func
def track_inventory():
    with open(PPE_FILE, 'r') as file:
        items = [line.strip().split(',') for line in file]
    
    items.sort()
    print("Total available quantity of all items:")
    for item in items:
        print(f"Item Code: {item[0]}, Quantity: {item[2]}")
    
    print("\nItems with stock quantity less than 25 boxes:")
    for item in items:
        if int(item[2]) < MIN_STOCK_THRESHOLD:
            print(f"Item Code: {item[0]}, Quantity: {item[2]}")
      
#Search Distribution List func
def search_distribution():
    item_code = input("Enter item code to search: ")
    distributions = {}
    
    with open(DISTRIBUTION_FILE, 'r') as file:
        for line in file:
            code, hospital, qty = line.strip().split(',')
            qty = int(qty)
            if code == item_code:
                if hospital in distributions:
                    distributions[hospital] += qty
                else:
                    distributions[hospital] = qty
    
    if distributions:
        print(f"Distribution list for item {item_code}:")
        for hospital, qty in distributions.items():
            print(f"Hospital: {hospital}, Quantity: {qty}")
    else:
        print(f"No distribution records found for item {item_code}.")

#Generate Report func
def generate_report():
    report_type = input("Select report type (1: Suppliers, 2: Hospitals, 3: Monthly Transactions): ")
    
    if report_type == '1':
        with open(SUPPLIERS_FILE, 'r') as file:
            print("List of suppliers with their PPE equipments supplied:")
            for line in file:
                print(line.strip())
    elif report_type == '2':
        with open(DISTRIBUTION_FILE, 'r') as file:
            distributions = {}
            for line in file:
                item, hospital, qty = line.strip().split(',')
                qty = int(qty)
                if hospital in distributions:
                    distributions[hospital] += qty
                else:
                    distributions[hospital] = qty
            print("List of hospitals with quantity of distribution items:")
            for hospital, qty in distributions.items():
                print(f"Hospital: {hospital}, Quantity: {qty}")
    elif report_type == '3':
        month = input("Enter month (MM format): ")
        with open(DISTRIBUTION_FILE, 'r') as file:
            print(f"Overall transaction report for month {month}:")
            for line in file:
                date, item, hospital, qty = line.strip().split(',')
                if date.startswith(month):
                    print(line.strip())
    else:
        print("Invalid report type.")

#Menu selection func (Could be change)
def main_menu():
    while True:
        print("\nPPE Inventory Management System")
        print("1. Login")
        print("2. Create Initial Inventory")
        print("3. Update Inventory")
        print("4. Track Inventory")
        print("5. Search Distribution History")
        print("6. Generate Report")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            if login():
                continue
            else:
                break
        elif choice == '2':
            create_initial_inventory()
        elif choice == '3':
            update_inventory()
        elif choice == '4':
            track_inventory()
        elif choice == '5':
            search_distribution()
        elif choice == '6':
            generate_report()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

#Run the program b4 make sure they are same
if __name__ == "__main__":
    main_menu()
