import json
import wikipediaapi
from tqdm import tqdm


def dict_countries():
    with open('countries.json', encoding='utf-8') as file:
        countries = json.load(file)

    dict_conries = {}
    wiki_wiki = wikipediaapi.Wikipedia('en')


    for country in tqdm(countries, ncols= 100):
        page_py = wiki_wiki.page(country['name']['common'].replace(' ', '_'))
        dict_conries[country['name']['common']] = page_py.fullurl
    return dict_conries


def create_file(dict=dict_countries()):
    with open('list_countries.json', 'w', encoding='utf-8') as file:
        json.dump(dict, file, ensure_ascii=False, indent=2)
    print('list_countries.json created')


if __name__ in '__main__':
    create_file()
