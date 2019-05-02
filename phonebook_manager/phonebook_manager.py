from phonebook_class import Phonebook, MissingDirectoryError
import menu
import json
import pickle
import os

def create_new_phonebook(filename):
    Phonebook(filename)

def load_phonebook(filename):
    with open(filename,"rb") as fh:
        return pickle.load(fh)






program_stop = False
while program_stop == False:
    with open('phonebook_config.json') as fh:
        conf = json.load(fh)
    print(conf)
    if os.path.isfile(conf["library_path"]):
        with open(conf["library_path"],'rb') as lib:
            library = pickle.load(lib)
    else:
        try:
            library={}
            with open(conf["library_path"],"wb") as lib:
                pickle.dump(library,lib)
        except FileNotFoundError:
            raise MissingDirectoryError(conf["library_path"],)

    menu.welcome()
    menu.main_menu()

    program_stop=True