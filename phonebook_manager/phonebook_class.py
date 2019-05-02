import pickle

class MissingDirectoryError(Exception):
    def __init__(self, filename):
        self.message = filename

    def __str__(self):
        return "There is an error, library could not be found or created in {}".format(self.message)

class Phonebook(dict):
    def __init__(self, filename,directory):
        self._filename = directory+filename
        initial = open(self._filename,'wb')
        initial.close()

    def save_phonebook(self):
        with open(self._filename,"wb") as fh:
            pickle.dump(self, fh)

