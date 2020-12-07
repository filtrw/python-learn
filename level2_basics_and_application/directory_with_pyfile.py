"""
Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, в которых есть
хотя бы один файл с расширением ".py".
Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.
Для лучшего понимания формата задачи, ознакомьтесь с примером.
"""

from os import path
from os import walk

path_to_task = path.join(".", "file_samples", "main")
result_dir_list = []
output_file = path.join(".", "file_samples", "output_dirs_order.txt")

for current_dir, dirs, files in walk(path_to_task):
    # print(f'current_dir: {current_dir}\ndirs {dirs}\nfiles {files}')
    for file_name in files:
        if file_name.endswith(".py"):
            # print(f'file_name {file_name}\tcurrent_dir {current_dir}')
            result_dir_list.append(current_dir.replace("./file_samples/", "", 1))
            break

result_dir_list.sort()
print(result_dir_list)
with open(output_file, "w") as output:
    output.write("\n".join(result_dir_list))
