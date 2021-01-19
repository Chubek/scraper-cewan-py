from pymongo import MongoClient
from trigger import *

class Database(MongoClient):

    def __init__(self, uri, db, collection):
        self.client = super().__init__(uri)
        print(f"Connected to {uri}")
        self.db = self.client[db]
        self.collection = self.db[collection]

    def __insert(self, insert_data):
        
        data = []

        for url, title, desc, article in insert_data:
            if not title and not desc and not article:
                continue
        
            data.append({
                'url': url,
                'title': title,
                'desc': desc,
                'article': article
            })
        
        res = self.collection.insert_many(data)

        print(f"Data inserted. Result: {res}") 


    def insert_abc(self):
        res = parse_abc()

        self.__insert(res)

    def insert_fox(self):
        res = parse_fox()

        self.__insert(res)


    def insert_nbc(self):
        res = parse_nbc()

        self.__insert(res)

    def insert_cnn(self):
        res = parse_cnn()

        self.__insert(res)

    def insert_utd(self):
        res = parse_utd()

        self.__insert(res)
    
    def insert_bbc(self):
        res = parse_bbc()

        self.__insert(res)

    def insert_cbs(self):
        res = parse_cbs()

        self.__insert(res)