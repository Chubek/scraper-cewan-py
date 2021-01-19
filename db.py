from pymongo import MongoClient
from trigger import *

class Database():

    def __init__(self, uri, db, collection):
        self.client = MongoClient(uri)
        print(f"Connected to {uri}")
        self.db = self.client[db]
        self.collection = self.db[collection]

    def __insert(self, insert_data):
        
        print(f"Got {len(insert_data)} data")

        data = []

        for url, title, desc, article in insert_data:            
            if not article:
                print("Article is null, continuing...")
                continue
            
            print(f"Title is {title}. Length of the article is {len(article)}.")
        
            data.append({
                'url': url,
                'title': title,
                'desc': desc,
                'article': article
            })
        
        print(f"Inserted {len(data)}")

        if data:
            res = self.collection.insert_many(data)
        else:
            res = None

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