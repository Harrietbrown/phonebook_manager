import phonebook_manager
import pytest


def test_no_directory_to_create_file():
    with pytest.raises(FileNotFoundError):
        phonebook_manager.Phonebook("NOTAREALNAME", "NOTAREALDIRECTORY/")

def test_

