import hashlib
import json


def input_path():
    path = input('''Programm reads only .json and .txt files!
If the file .json, you can get an encrypted dictionary in a object "dict".
If the file .txt, you can get an encrypted dictionary in a object "hash_text".
Input path to file: ''')

    if path.endswith('.json'):
        with open(path, encoding='utf-8') as file:
            json_file = json.load(file)

        global dict
        dict = {}

        def generator(data=json_file):
            for key, value in data.items():
                key_json = hashlib.md5(key.encode())
                str_values_json = ''
                for i in value:
                    str_values_json += str(i)
                value_json = hashlib.md5(str_values_json.encode())
                key = key_json.hexdigest()
                value = value_json.hexdigest()
                yield key, value
                dict[key] = value

        return generator()

    elif path.endswith('.txt'):
        with open(path, encoding='utf-8') as file:
            txt_file = file.read()

        global hash_text
        hash_text = []

        def generator_txt(data=txt_file):
            new_list_text = []
            list_text = data.split('\n')  # Создаёт список из строк
            for i in list_text:  # Создаёт новый список из старого без пустых строк
                if i:
                    new_list_text.append(i)

            for line in new_list_text:
                str_line = hashlib.md5(line.encode())
                hash_line = str_line.hexdigest()

                yield hash_line
                hash_text.append(hash_line)

        return generator_txt()

    else:
        print('Unknown file extension')


if __name__ in '__main__':

    for i in input_path():
        print(i)
        continue

    # print(dict)
    # print(hash_text)