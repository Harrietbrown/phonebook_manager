from phonebook_class import Phonebook, MissingDirectoryError
import menu
import json
import pickle
import os

def create_new_phonebook(directory):
    bookname = input("Please give the name of this new phonebook: ")
    if bookname in library.keys():
        print("That name is already taken. \n Returning to menu \n\n")
    else:
        library[bookname] = Phonebook(bookname, directory)
        save_library()

def load_phonebook(filename):
    with open(filename,"rb") as fh:
        return pickle.load(fh)


def save_library():
    with open(conf["library_path"]+"library.pickle","wb") as lib:
        pickle.dump(library,lib)





if __name__ == "__main__":
    program_stop = False
    #load configuration file
    with open('phonebook_config.json') as fh:
        conf = json.load(fh)
    print(conf)

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

    menu.welcome()
    #start running menu options
    while program_stop == False:
        menu.main_menu()
        option = menu.select_option([0,1,2,3])
        if option == 1:
            create_new_phonebook(conf["library_path"])
        if option == 2:
            pass
        elif option == 3:
            pass
        elif option == 0:
            program_stop = True

