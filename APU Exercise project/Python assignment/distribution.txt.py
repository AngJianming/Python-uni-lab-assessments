  if action == "DISTRIBUTE":
      hospital_code = get_user_input("Enter hospital code: ").upper()
      # Implement logic to check if hospital exists (using hospitals.txt)
      # Write distribution record to distribution.txt

  print(f"Inventory for {ITEM_CODES[item_code]} ({item_code}) successfully {action.lower()}d by {quantity} boxes.")

  # Function to create suppliers.txt file for storing supplier details
  def create_suppliers_txt():
      """Creates suppliers.txt file for storing supplier details."""
      if file_exists("suppliers.txt"):
          print("suppliers.txt file already exists. Skipping creation.")
          return
      # Implement logic to prompt user for supplier details (code, name, contact information, etc.)
      # Write supplier details to suppliers.txt

  # Function to create hospitals.txt file for storing hospital details
  def create_hospitals_txt():
      """Creates hospitals.txt file for storing hospital details."""
      if file_exists("hospitals.txt"):
          print("hospitals.txt file already exists. Skipping creation.")
          return
      # Implement logic to prompt user for hospital details (code, name, address, etc.)
      # Ensure minimum number of hospitals (MIN_HOSPITALS) are created
      # Write hospital details to hospitals.txt

  # Function to print total available quantity of all items
  def print_total_inventory():
      """Prints total available quantity of all items sorted by item code."""
      if not file_exists("ppe.txt"):
          print("ppe.txt file not found.")
          return
      inventory = {}
      with open("ppe.txt", "r") as f:
          for line in f:
              code, name, stock, _ = line.strip().split(",")
              inventory[code] = int(stock)
      sorted_inventory = dict(sorted(inventory.items()))
      print("Total Inventory:")
      for code, stock in sorted_inventory.items():
          print(f"{code} ({ITEM_CODES[code]}):", stock, "boxes")

  # Function to print items with low stock
  def print_low_stock_items():
      """Prints records of items with stock quantity less than 25 boxes."""
      if not file_exists("ppe.txt"):
          print("ppe.txt file not found.")
          return
      inventory = {}
      with open("ppe.txt", "r") as f:
          for line in f:
              code, name, stock, _ = line.strip().split(",")
              inventory[code] = int(stock)
      low_stock_items = [f"{code} ({ITEM_CODES[code]}) - {stock} boxes" for code, stock in inventory.items() if
                         stock < 25]
      if low_stock_items:
          print("Items with low stock (less than 25 boxes):")
          for item in low_stock_items:
              print(item)
      else:
          print("No items with low stock found.")

  # Function to search and print distribution list of an item
  def search_distribution_list():
      """Searches and prints the distribution list of a particular item."""
      if not (file_exists("ppe.txt") and file_exists("distribution.txt")):
          print("Missing required files (ppe.txt, distribution.txt).")
          return
      item_code = get_user_input("Enter item code (HC, FS, MS, GL, GW, SC): ").upper()
      if item_code not in ITEM_CODES:
          print("Invalid item code.")
          return
      distributions = {}
      with open("distribution.txt", "r") as f:
          for line in f:
              code, hospital_code, quantity = line.strip().split(",")
              if code == item_code:
                  distributions[hospital_code] = distributions.get(hospital_code, 0) + int(quantity)
      if not distributions:
          print(f"No distributions found for {ITEM_CODES[item_code]} ({item_code}).")
  return

  print(f"Distribution List for {ITEM_CODES[item_code]} ({item_code}):")
  for hospital_code, quantity in distributions.items():
    print(f"{hospital_code}: {quantity} boxes")

# Function to print a report of list of suppliers with their supplied PPEs
def print_supplier_report():
  """Prints a report listing suppliers with their supplied PPE equipments."""
  if not (file_exists("ppe.txt") and file_exists("suppliers.txt")):
    print("Missing required files (ppe.txt, suppliers.txt).")
    return
  suppliers = {}  # Dictionary to store supplier details with their supplied items
  with open("suppliers.txt", "r") as f:
    for line in f:
      code, name, stock, supplier_code = line.strip().split(",")
      if supplier_code in suppliers:
        suppliers[supplier_code].append(f"{code} ({name})")
      else:
        suppliers[supplier_code] = [f"{code} ({name})"]

  print("List of Suppliers with Supplied PPEs:")
  for supplier_code, items in suppliers.items():
    # Implement logic to display supplier details (name, etc.) retrieved from 'suppliers' dictionary
    print(f"  - Supplied by: {supplier_code}")  # Replace with actual supplier details
    for item in items:
      print(f"      - {item}")

# Function to print a report of list of hospitals with quantity of distributed items
def print_hospital_report():
  """Prints a report listing hospitals with the quantity of distributed items."""
  if not (file_exists("hospitals.txt") and file_exists("distribution.txt")):
    print("Missing required files (hospitals.txt, distribution.txt).")
    return
  hospitals = {}  # Dictionary to store hospital details with their received quantities
  with open("hospitals.txt", "r") as f:
    for line in f:


  with open("distribution.txt", "r") as f:
    for line in f:
      code, hospital_code, quantity = line.strip().split(",")
      hospitals[hospital_code] = hospitals.get(hospital_code, 0) + int(quantity)

  print("List of Hospitals with Distributed Items:")
  for hospital_code, total_quantity in hospitals.items():
    # Implement logic to display hospital details (name, etc.) retrieved from 'hospitals' dictionary
    print(f"  - {hospital_code}: {total_quantity} boxes")  # Replace with actual hospital details

# Function to print a report for overall transactions in a month
def print_transaction_report():
  """Prints a report for overall transactions (supply received and distribution) in a month."""
  # Implement logic to request month (e.g., get user input for year and month)
  # Read transaction data from ppe.txt and distribution.txt for the specified month
  # Calculate and display total received and distributed quantities for each item code
  # Consider using datetime module for date handling
  print("Transaction Report for Month (to be implemented)")

# Main program loop
controllers = {}  # Dictionary to store registered inventory controllers
loggedIn_user = None

while True:
  if not loggedIn_user:
    print("\nInventory Management System")
    print("1. Login")
    print("2. Register Controller")
    print("3. Exit")
    choice = get_user_input("Enter your choice: ")
    if choice == '1':
      loggedIn_user = login()
    elif choice == '2':
      register_controller()
    elif choice == '3':
      break
    else:
      print("Invalid choice. Please try again.")
  else:
    print("\nMain Menu:")
    print("1. Create PPE Inventory (one-time only)")  # Disable after initial creation
    print("2. Update Inventory (Receive new data)")
    print("3. Exit")
