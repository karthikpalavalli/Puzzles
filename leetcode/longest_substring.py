from copy import deepcopy

input_str = input()

max_chars_seen = []

for i in range(len(input_str)):
    chars_seen = list()
    chars_seen.append(input_str[i])

    for j in range(i + 1, len(input_str)):
        if input_str[j] in chars_seen:
            break
        chars_seen.append(input_str[j])

    if len(chars_seen) > len(max_chars_seen):
        max_chars_seen = deepcopy(chars_seen)

print(len(max_chars_seen))