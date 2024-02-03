import getpass

class Staff:
    def __init__(self, firstName, lastName, job_title, birthday, authority, SIN) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.job_title = job_title
        self.birthday = birthday
        self.authority = authority
        self.__SIN = SIN

        self.staff_dict = {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "job": self.job_title,
            "birthday": self.birthday,
            "authority": self.authority,
        }


    def get_info(self):
        return self.staff_dict
    

firstName = "Thaddeus"
lastName = "Baturensky"
job = "Doctor"
birthday = "August 24th, 2005"
authority = 2
SIN = 123456789
username = "Thadd"
password = "1234"




Staff1 = Staff(firstName, lastName, job, birthday, authority, SIN)


import msvcrt

user_database = {
    'user1': 'password123',
    'user2': 'hello@world',
    # Add more users as needed
}

def getpass_with_mask(prompt=""):
    password = ""
    print(prompt, end='', flush=True)
    while True:
        char = msvcrt.getch().decode('utf-8')
        if char == '\r':
            print()  # Move to the next line after password entry
            break
        elif char == '\x08':  # Backspace
            if password:
                password = password[:-1]
                print('\x08 \x08', end='', flush=True)  # Move back, overwrite '*', move back
        else:
            password += char
            print('*', end='', flush=True)  # Print '*' for masking
    return password

def login(username, password):
    if username in user_database:
        stored_password = user_database[username]
        if stored_password == password:
            print("Login successful.")
        else:
            print("Incorrect password. Please try again.")
    else:
        print("Username not found. Please register.")

# Example usage:
username_input = input("Enter your username: ")
password_input = getpass_with_mask("Enter your password: ")
login(username_input, password_input)






