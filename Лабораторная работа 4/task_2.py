def get_count_char(str_):
    str_for_analysis = str_.lower()
    count_char = {}
    DEFAULT_COUNT = 0
    for alpha in str_for_analysis:
        if alpha.isalpha():
            count_char[alpha] = count_char.get(alpha, DEFAULT_COUNT) + 1
    return count_char


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))


def get_percent_of_char(dict_):
    percent_conversion = 100
    full_value = sum(dict_.values())
    for kay, value in dict_.items():
        dict_[kay] = round(value / full_value * percent_conversion, 2)
    return dict_

#print(get_percent_of_char(get_count_char(main_str)), "\n" ,sum(get_percent_of_char(get_count_char(main_str)).values())) #  Для самопроверки
