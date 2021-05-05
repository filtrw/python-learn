import os


def get_file_names(path: str, recursive: bool):
    # возвращает полный путь до каждого файла в этой директории
    # recursive = True - значит пробегаться рекурсивно по папкам тоже
    list_all_object = os.listdir(path)
    for element in list_all_object:
        path_for_element = os.path.join(path, element)
        if os.path.isfile(path_for_element):
            yield path_for_element
        else:
            if recursive:
                for sub_path in get_file_names(path_for_element, recursive):
                    yield sub_path


def main():
    dir_for_search = input()
    path_for_search = os.path.abspath(os.path.join("../", dir_for_search))
    for element in get_file_names(path_for_search, True):
        print(element)


if __name__ == "__main__":
    main()
