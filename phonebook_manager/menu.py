
def welcome():
    print(' ----------------------------------------- ')
    print('|     Welcome to phonebook manager.py     |')
    print(' ----------------------------------------- ')
    print('\n\n\n')

def main_menu():
    print("1:    Display an existing phonebook")
    print("2:    Create a new phonebook")
    print("3:    Add a number to an existing phonebook")
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
                print("Please enter a valid option.")
        except ValueError:
            print("Please enter a valid option.")
    return choice