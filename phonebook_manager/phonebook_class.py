import pickle

class MissingDirectoryError(Exception):
    def __init__(self, filename):
        self.message = filename

    def __str__(self):
        return "There is an error, library could not be found or created in {}".format(self.message)

class Phonebook(dict):
    def __init__(self, filename):
        self._filename = filename
        initial = open(filename,'r')
        for line in initial:
            line = line.rstrip()
            key,value = line.split('=',1)
            dict.__setitem__(self,key,value)
        initial.close()

    def save_phonebook(self):
        with open(self._filename,"wb") as fh:
            pickle.dump(self, fh)

