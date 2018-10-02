numbers_list = list(map(int, input().strip().split()))

numbers_list.sort()

print(sum(numbers_list[:-1]), end = ' ')
print(sum(numbers_list[1:]))
