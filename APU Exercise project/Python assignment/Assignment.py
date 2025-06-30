#User name and password as demo value in dictionary
users = {
    "AJM": "0000",
    "CHW": "0001",
    "CJK": "0002",
    "LTY": "0003"
}

max_attempts = 3
Login = False

def login():
    attempts = 0
    while attempts < max_attempts:
        username = input("Username: ")
        password = input("Password: ")
        if username in users and users[username] == password:
            print("Login successful!")
            break
        else:
            attempts += 1
            print(f"Incorrect username or password please try again. Attempts remaining: {max_attempts - attempts}")
            if max_attempts - attempts == 0:
                print("Login failed after too many attempts. You have been terminated from the system.\nPlease restart the program.")


controllers_login = login()


