from os import path

input_file_path = path.join(".", "file_samples", "direct_order.txt")

with open(input_file_path) as input_file:
    line_list = input_file.read().splitlines()

line_list.reverse()

output_file_path = path.join(".", "file_samples", "output_reverse_order.txt")
with open(output_file_path, "w") as output_file:
    output_file.write("\n".join(line_list))
