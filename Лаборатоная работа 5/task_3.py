from random import randint


def get_unique_list_numbers() -> list[int]:
    list_len = 15
    min_mean = -10
    max_mean = 10
    list_of_unique_numbers = []
    while len(list_of_unique_numbers) != list_len:
        new_mean = randint(min_mean, max_mean)
        if not new_mean in list_of_unique_numbers:
            list_of_unique_numbers.append(new_mean)
    return list_of_unique_numbers



list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
