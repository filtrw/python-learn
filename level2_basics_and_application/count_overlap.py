origin_string, find_string = input(), input()
current_string = origin_string
count = 0

while find_string in current_string:
    current_string = current_string[current_string.index(find_string) + 1:]
    count += 1

print(count)
