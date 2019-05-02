import pickle

class MissingDirectoryError(Exception):
    def __init__(self, filename):
        self.message = filename

    def __str__(self):
        return "There is an error, library could not be found or created in {}".format(self.message)

class Phonebook(object):
    def __init__(self, filename,directory,firstname,firstnumber):
        self._filename = directory+filename+".pickle"
        self._dict = {firstname:firstnumber}
        self.save_phonebook()
        #saves a phonebook with only one name and number in it.

    #add a name and number to book and saved
    def add_number(self, name, number):
        self._dict[name]=number
        self.save_phonebook(self)

    #save current instance of book
    def save_phonebook(self):
        with open(self._filename,"wb") as fh:
            pickle.dump(self, fh)
        return

    #display contents of the book
    def display_contents(self):
        if len(self._dict.keys())==0:
            print("You don't seem to have any numbers saved. \n you should make some more friends")
        else:
            for key in self._dict.keys():
                print("{0:>10} | {1}".format(key,self._dict[key]))
            print("\n\n")



