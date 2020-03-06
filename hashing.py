import hashlib
import json


def input_path():
    path = input('Input path to file: ')

    if path.endswith('.json'):
        with open(path, encoding='utf-8') as file:
            json_file = json.load(file)

        def hash_json():
            dict_json = {}
            for key, value in json_file.items():
                key_json = hashlib.md5(key.encode())
                str_values_json = ''
                for i in value:
                    str_values_json += str(i)
                value_json = hashlib.md5(str_values_json.encode())
                dict_json[key_json.hexdigest()] = value_json.hexdigest()
            return dict_json

        return hash_json()

    elif path.endswith('.txt'):
        with open(path, encoding='utf-8') as file:
            txt_file = file.read()
        hash_text = hashlib.md5(txt_file.encode())
        text = hash_text.hexdigest()
        return text
    else:
        print('Unknown file extension')


def record(data=input_path()):
    file_name = input('Enter file name: ') + '.json'
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
    print(f'File {file_name} created!')


if __name__ in '__main__':
    record()