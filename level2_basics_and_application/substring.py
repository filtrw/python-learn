origin_string, find_string, replace_string = input(), input(), input()
count_replace = 0
current_string = origin_string

while find_string in current_string:
    current_string = current_string.replace(find_string, replace_string)
    count_replace += 1
    if (count_replace > 1000):
        print("Impossible")
        break
else:
    print(count_replace)
