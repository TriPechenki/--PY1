list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_mean = list_numbers[0]
index_max = 0
for index, value in enumerate(list_numbers):
    if value > max_mean:
        max_mean, index_max = value, index
list_numbers[index_max], list_numbers[-1] = list_numbers[-1], list_numbers[index_max]
print(list_numbers)
