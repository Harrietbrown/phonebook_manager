from phonebook_class import Phonebook, MissingDirectoryError
import menu
import json
import pickle
import os

def library_checker(conf):
    #check to see if library file exists
    if os.path.isfile(conf["library_path"]+"library.pickle"):
        with open(conf["library_path"]+"library.pickle",'rb') as lib:
             library = pickle.load(lib)
    else:
        #make new library file
        try:
            library={}
            with open(conf["library_path"]+"library.pickle","wb") as lib:
                pickle.dump(library,lib)
        except FileNotFoundError:
            #cannot make library, return error
            raise MissingDirectoryError(conf["library_path"],)
    return library

def display_phonebook(directory,library):
    if len(library)==0:
        print("No phonebooks found")
    else:
        book = input("Select a phonebook to display?  ")
        targetbook = load_phonebook(directory+book+".pickle")
        targetbook.display_contents()
    return

def create_new_phonebook(directory):
    bookname = input("Please give the name of this new phonebook: ")
    if bookname in library.keys():
        print("That name is already taken. \n Returning to menu \n\n")
    else:
        name = input("We need a first entry to the phonebook, please give a name.  ")
        number = input("Please give a number.  ")
        library[bookname] = Phonebook(bookname, directory, name, number)
        save_library()

        
def add_number_to_phonebook(directory, book):
    name = input("what name should be associated with this number? ")
    number = input("please enter phone number. ")
    targetbook = load_phonebook(directory+book+".pickle")
    targetbook.add_number(name, number)
    return

def load_phonebook(filename):
    book = pickle.load(open(filename,"rb"))
    return book

def save_library():
    with open(conf["library_path"]+"library.pickle","wb") as lib:
        pickle.dump(library,lib)
    return




if __name__ == "__main__":
    program_stop = False
    #load configuration file
    with open('phonebook_config.json') as fh:
        conf = json.load(fh)
    print(conf)

    #check to see if library file exists
    library=library_checker(conf)

    menu.welcome()
    #start running menu options
    while program_stop == False:
        menu.main_menu()
        option = menu.select_option([0,1,2,3])
        if option == 1:
            display_phonebook(conf["library_path"],library)
        elif option == 2:
            create_new_phonebook(conf["library_path"])
        elif option == 3:
            book = input("Which book should this number be put into?  ")
            add_number_to_phonebook(conf["library_path"],book)
        elif option == 0:
            program_stop = True

