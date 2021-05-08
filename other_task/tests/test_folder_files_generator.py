import pytest
import shutil
import other_task.folder_files_generator as folder_gen
import os


def test_good():
    path_to_level_1 = os.path.abspath(os.path.normpath("../../dir_level1"))
    path_to_level_2_1 = os.path.join(path_to_level_1, "dir_level2_1")
    path_to_level_2_2 = os.path.join(path_to_level_1, "dir_level2_2")
    path_to_level_3 = os.path.join(path_to_level_2_1, "level3")
    file_1 = os.path.join(path_to_level_1, "file_level1.txt")
    file_2_1 = os.path.join(path_to_level_2_1, "file_level2_1.txt")
    file_3 = os.path.join(path_to_level_3, "file_level3.txt")

    # Lists for create folder and files
    dir_list = [path_to_level_1, path_to_level_2_1, path_to_level_2_2, path_to_level_3]
    file_list = [file_1, file_2_1, file_3]

    # List for expected results
    all_list = (dir_list[1:] + file_list)
    if os.path.exists(path_to_level_1):
        shutil.rmtree(path_to_level_1)

    for directory in dir_list:
        os.mkdir(directory)
    for files in file_list:
        with open(files, "w") as new_file:
            pass

    my_func_list = list(folder_gen.get_file_names(path_to_level_1, recursive=True))
    assert len(my_func_list) == 3
    assert my_func_list[0] == file_1
    assert my_func_list[1] == file_2_1
    assert my_func_list[2] == file_3

    # my_func_list = list(folder_gen.get_file_names(os.path.abspath(path_to_level_1), recursive=False)).sort()
    # assert my_func_list == file_list


def test_empty_folders():
    path_empty = "../../test_folder"
    if os.path.exists(path_empty) == False:
        os.mkdir(path_empty)
    empty_dir = []
    for element in folder_gen.get_file_names(os.path.abspath(path_empty), recursive=False):
        empty_dir.append(element)
    assert len(empty_dir) == 0
    os.rmdir(path_empty)


def test_non_exist_folders():
    path_not_exist = "../../not_exist"
    not_exist_dir = []
    if os.path.exists(path_not_exist) == False:
        with pytest.raises(FileNotFoundError):
            list(folder_gen.get_file_names(os.path.abspath(path_not_exist), recursive=False))
