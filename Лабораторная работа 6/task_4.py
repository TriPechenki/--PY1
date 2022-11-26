import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str, delmiter: str = ",", new_line: str = "\n") -> list[dict]:
    """
    Функция конвертирует данные из csv файл в список, состоящий из словарей
    :param filename: адрес файла для чтения
    :param delmiter: разделитель между данными в строке в читаемом файле
    :param new_line: разделитель между строками в читаемом файле
    :return: список словарей
    """
    with open(filename) as f:
        csv_list = f.read().split(new_line)  # чтение файла с разделением по разделителю строк (по умолчание "\n")
        data_for_dict = []
        for line in csv_list:
            data_for_dict.append(line.split(delmiter)) # формирование списка со списками, в которыд данные разделены про разделителю данных (по умолчание ",")
        """
        Возвращение списка со словарями: первая строка data_for_dict содержит заголовки данных,
        поэтому неизменна в формировании ключей словрей. Запись значений идет из всех остальных строк data_for_dict 
        (поэтому значения data_for_dict[b+1][i]). 
        """
        return [{data_for_dict[0][i]: data_for_dict[b+1][i] for i in range(len(data_for_dict[0]))} for b in range(len(data_for_dict)-1)]


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

# Запись json файла
with open("json_data.json", "w") as f:
    json.dump(csv_to_list_dict(INPUT_FILE), f)
