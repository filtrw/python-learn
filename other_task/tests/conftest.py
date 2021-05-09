import pytest
from os import path, mkdir, rmdir
from shutil import rmtree


def clean_folder_structure():
    path_to_level_1 = path.abspath(path.normpath("../../dir_level1"))
    if path.exists(path_to_level_1):
        rmtree(path_to_level_1)


@pytest.fixture(scope="function")
def create_folder_structure():
    clean_folder_structure()

    # Create folder's name structure
    path_to_level_1 = path.abspath(path.normpath("../../dir_level1"))
    path_to_level_2_1 = path.join(path_to_level_1, "dir_level2_1")
    path_to_level_2_2 = path.join(path_to_level_1, "dir_level2_2")
    path_to_level_3 = path.join(path_to_level_2_1, "level3")

    # create file's name in different level folder structure
    file_1 = path.join(path_to_level_1, "file_level1.txt")
    file_2_1 = path.join(path_to_level_2_1, "file_level2_1.txt")
    file_3 = path.join(path_to_level_3, "file_level3.txt")

    # Lists for create folder and files
    dir_list = [path_to_level_1, path_to_level_2_1, path_to_level_2_2, path_to_level_3]
    file_dict = {'root': path_to_level_1, 'files': [file_1, file_2_1, file_3]}

    for directory in dir_list:
        mkdir(directory)

    for file_s in file_dict['files']:
        with open(file_s, "w"):
            pass

    return file_dict


@pytest.fixture(scope="function")
def create_empty_folder():
    path_empty = path.abspath(path.normpath("../../test_folder"))

    if path.exists(path_empty) == True:
        rmdir(path_empty)

    mkdir(path_empty)
    return path_empty
