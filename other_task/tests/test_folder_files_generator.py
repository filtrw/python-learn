import pytest
import other_task.folder_files_generator as folder_gen
from os import path


def test_good_recursive(create_folder_structure):
    my_func_list = list(folder_gen.get_file_names(create_folder_structure['root'], recursive=True))
    assert len(my_func_list) == len(create_folder_structure['files'])

    # need sort for same order of folder and files. Order is not significant for this function
    assert sorted(my_func_list) == sorted(create_folder_structure['files'])


def test_good(create_folder_structure):
    my_func_list = list(folder_gen.get_file_names(create_folder_structure['root'], recursive=False))
    assert my_func_list[0] == create_folder_structure['files'][0]


def test_empty_folders(create_empty_folder):
    test_result = list(folder_gen.get_file_names(create_empty_folder, recursive=False))
    assert len(test_result) == 0

def test_non_exist_folders():
    path_not_exist = "../../not_exist"
    not_exist_dir = []
    if path.exists(path_not_exist) == False:
        with pytest.raises(FileNotFoundError):
            list(folder_gen.get_file_names(path.abspath(path_not_exist), recursive=False))
