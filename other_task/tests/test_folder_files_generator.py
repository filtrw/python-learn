import other_task.folder_files_generator as folder_gen
import os


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
        try:
            for element in folder_gen.get_file_names(os.path.abspath(path_not_exist), recursive=False):
                not_exist_dir.append(element)
        except Exception as e:
            assert e.args[1] == "No such file or directory"
