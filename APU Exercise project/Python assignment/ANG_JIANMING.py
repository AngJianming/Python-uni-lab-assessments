# ANG JIANMING
# TP076671

import os

# Constants
MAX_LOGIN_ATTEMPTS = 3
MAX_SUPPLIERS = 4
MAX_HOSPITAL = 3
INITIAL_QUANTITY = 100
MIN_STOCK_THRESHOLD = 25
PPE_FILE = "ppe.txt"
SUPPLIERS_FILE = "suppliers.txt"
HOSPITALS_FILE = "hospitals.txt"
DISTRIBUTION_FILE = "distribution.txt"


# Login Function
def login():
    users = {
        "AJM": "0000",
        "CHW": "0001",
        "CJK": "0002",
        "LTY": "0003"
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


# Initialize Files (Create files that we need)
def initialize_files():
    suppliers = {}
    supplier_count = 0

    while supplier_count < MAX_SUPPLIERS:
        supplier_code = input(f"Enter supplier code for supplier {supplier_count + 1}: ")
        if  supplier_code in suppliers:
            print("Repetitive supplier code error. You can't have the same supplier code. Please try again.")
        else:
            suppliers[supplier_code] = []
            supplier_count += 1
    
    with open(PPE_FILE, 'w') as file:
        ppe_items = ['HC', 'FS', 'MS', 'GL', 'GW', 'SC']
        for item in ppe_items:
            supplier_code = input(f"Enter supplier code for {item}: ")
            while supplier_code not in suppliers:
                print("Invalid supplier code. Please enter a valid supplier code.")
                supplier_code = input(f"Enter supplier code for {item}: ")
            suppliers[supplier_code].append(item)
            file.write(f"{item} | {supplier_code} | {INITIAL_QUANTITY}\n")

    hospitals = {}
    hospital_count = 0

    while hospital_count < MAX_HOSPITAL:
        hospital_code = input(f"Enter hospital code for hospital {hospital_count + 1}: ")
        if hospital_code in hospitals:
            print("Repetitive hospital code error. You can't have the same hospital code. Please try again")
        else:
            hospitals[hospital_code] = []
            hospital_count += 1

    with open(SUPPLIERS_FILE, 'w') as file:
        for supplier_code, items in suppliers.items():
            file.write(f"{supplier_code}: {', '.join(items)}\n")
    
    with open(HOSPITALS_FILE, 'w') as file:
        for hospital_code in hospitals:
            file.write(f"{hospital_code}\n")
    
    open(DISTRIBUTION_FILE, 'w').close()
    
    print("Files initialized and inventory created.")


# Update Inventory Function
def update_inventory():
    item_code = input("Enter item code to update: ")
    update_type = input("Enter 'R' to receive items or 'D' to distribute items: ")
    quantity = int(input("Enter quantity: "))
    
    items = []
    found = False
    
    with open(PPE_FILE, 'r') as file:
        for line in file:
            item, supplier, qty = line.strip().split('| ')
            qty = int(qty)

            if item == item_code:
                found = True
                if update_type == 'R':
                    qty += quantity
                elif update_type == 'D':
                    if qty < quantity:
                        print(f"Insufficient stock. Current stock is {qty}.")
                        return
                    hospital = input("Enter the hospital code: ")
                    with open(DISTRIBUTION_FILE, 'a') as file:
                        file.write(f"{item_code},{hospital},{quantity}\n")
                    print(f"Distribution logged for item {item_code} to hospital {hospital}.")
                    qty -= quantity
                else:
                    print("Invalid update type.")
                    return
            items.append(f"{item},{supplier},{qty}\n")
    
    if item == item_code:
        found = True
        with open(PPE_FILE, 'w') as file:
            file.writelines(items)
        print(f"Inventory updated for item {item_code}.")
    else:
        print(f"Item code {item_code} not found.")


# Track Inventory Function
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


# Search Distribution List Function
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


# Generate Report Function
def generate_report():
    report_type = input("Select report type (1: Suppliers, 2: Hospitals, 3: Monthly Report): ")
    
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


# Main Menu Function
def main_menu():
    while True:
        print('''
        -----------------------------------------------------
         Welcome to Group 30 PPE Inventory Management System
        -----------------------------------------------------
        1. Update Inventory
        2. Track Inventory
        3. Search Distribution History
        4. Generate Report
        5. Exit
        ''')

        choice = input("Enter your choice: ")

        if choice == '1':
            update_inventory()
        elif choice == '2':
            track_inventory()
        elif choice == '3':
            search_distribution()
        elif choice == '4':
            generate_report()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    if login():
        initialize_files()
        main_menu()

