
def welcome():
    print(' ----------------------------------------- ')
    print('|     Welcome to phonebook manager.py     |')
    print(' ----------------------------------------- ')
    print('\n\n\n')

def main_menu():
    pass

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