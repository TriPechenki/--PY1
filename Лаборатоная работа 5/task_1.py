from pprint import pprint

min_number = 0
max_number = 15
list_of_dict = [{'bin': bin(number), 'dec': number, 'hex': hex(number), 'oct': oct(number)} for number in range(min_number, max_number + 1)]
pprint(list_of_dict)