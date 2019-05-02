
def welcome():
    print(' ----------------------------------------- ')
    print('|     Welcome to phonebook manager.py     |')
    print(' ----------------------------------------- ')
    print('\n\n\n')

def main_menu():
    print("1:    Create a new phonebook")
    print("2:    Load an existing phonebook")
    print("3:    Delete a phonebook phonebook")
    print()
    print("0:    Exit Program")
    print()
    

def select_option(options):
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option selected: "))
            if choice in options:
                option_valid = True
            else:
                print("Please enter avalid option.")
        except ValueError:
            print("Please enter a valid option.")
    return choice