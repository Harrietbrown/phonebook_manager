from phonebook_class import Phonebook
import phonebook_manager
import pytest
import os


@pytest.fixture
def phonebook(request):
    """provides a temporary dummy phoneboook"""
    phonebook = Phonebook("testbook", os.path.dirname(__file__)+"/libtest/", "testname", "testnumber")
    def cleanup_phonebook():
        os.remove(os.path.dirname(__file__)+"/libtest/testbook.pickle")
    request.addfinalizer(cleanup_phonebook)
    return phonebook


def test_no_directory_to_create_file():
    with pytest.raises(FileNotFoundError):
        phonebook_manager.Phonebook("NOTAREALNAME", "NOTAREALDIRECTORY/", "NOTAREALNAME", "NOTAREALNUMBER")


def test_is_a_phonebook_file_created_n_test_directory(phonebook):
    testbook_path = os.path.dirname(__file__)+"/libtest/testbook.pickle"
    assert os.path.isfile(testbook_path)

def test_no_config_file_found():
    with pytest.raises(FileNotFoundError):
        open('NOTACONFIGFILE.json')
