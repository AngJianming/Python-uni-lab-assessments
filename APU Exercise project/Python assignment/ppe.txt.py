print('''
--------------------------------------------
 Welcome to PPE Inventory Management System
--------------------------------------------
1. Update Inventory
2. Track Inventory
3. Search Distribution History
4. Generate Report
5. Exit
''')




choice = int(input("Enter Your Option: "))
if choice == 1:
    print("Show Items!!!")
    try:
        with open("ppe.txt", 'r') as ppe_file_variable:
            for item in ppe_file_variable:
                print("--------------------------------------------")
                print(item)
    except FileNotFoundError:
        print("Error")
elif choice == 2:
    print("How many boxes do you want to distribute?")
    user_input = int(input("Enter a value/number here: "))
    if user_input != int:
        print("Only value/number. Please rerun the program")
    else:
        with open("ppe.txt", 'r') as change_quantity:
            print(int(change_quantity.readline().strip()) - int(user_input))



