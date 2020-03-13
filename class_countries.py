import requests
import json
from pprint import pprint
import wikipediaapi
from tqdm import tqdm


class iterator_countries:

    def __init__(self):
        self.count = -1
        with open('countries.json', encoding='utf-8') as file:
            countries = json.load(file)
        self.content = countries

    def __iter__(self):
        return self.content

    def __next__(self):  # the source file is presented as a list of dictionaries, so I iterate by numbers
        while self.count <= len(self.content):
            self.count += 1
            information = self.content[self.count]['name']['common']
            return information
        else:
            raise StopIteration

    def create_dict(self):
        self.dict = {}
        self.wiki_wiki = wikipediaapi.Wikipedia('en')
        for i in tqdm(range(len(self.__iter__())), ncols=100):
            country = self.__next__()
            page_py = self.wiki_wiki.page(country.replace(' ', '_'))
            self.dict[country] = page_py.fullurl
            i += 1
        return self.dict

    def create_file(self):
        with open('list_countries.json', 'w', encoding='utf-8') as file:
            json.dump(self.create_dict(), file, ensure_ascii=False, indent=2)
        print('list_countries.json created')


if __name__ in '__main__':
    a = iterator_countries()
    a.create_file()