import mysql.connector 
import functools
import operator
from trigger import *
import re
from random import sample

class MQLDB:

    def __init__(self, username, password, server):
        self.mydb = mysql.connector.connect(
            host=server,
            user=username,
            password=password
        )

        self.cursor = self.mydb.cursor()        
        self.cursor.execute("SHOW DATABASES")
        if not 'sentences' in [l[0] for l in self.cursor.fetchall()]:
            print("Database doesn't exist, creating...")
            self.cursor.execute("CREATE DATABASE sentences")
            self.cursor.execute("USE sentences")
            self.cursor.execute("CREATE TABLE sentences_table_new (sentence_id int NOT NULL AUTO_INCREMENT, sentence VARCHAR(2000), label VARCHAR(50))")
            self.mydb.commit()
        else:
            print("Database found, selecting...")
            self.cursor.execute("USE sentences")
            self.mydb.commit()

        self.all = None

    def __insert(self, articles):
        print(f"Got {len(articles)}")
        sql = "INSERT INTO sentences_table_new (sentence, label) VALUES (%s, %s)"

        vals = functools.reduce(operator.iconcat, [[(sentence, 'UNLABLED') for sentence in re.split('[.!?\\-]', article[3]) if sentence] for article in articles], [])
        
        self.cursor.executemany(sql, vals)
        self.mydb.commit()

        print(f"Inserted {len(vals)}")

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


    def select_rand(self):
        self.cursor.execute("SELECT * FROM sentences_table_new WHERE label = 'UNLABLED' ORDER BY RAND() limit 50")

        self.all = self.cursor.fetchall()

        
    def return_sample_sentence(self):
        if len(self.all) < 1:
            raise Exception("Sample sentences exhausted. Rerun the script.")
        
        samp =  sample(self.all, 1)[0]
        self.all.remove(samp)

        return samp

    def label_sample_sentence(self, sentence_tuple):
        update = f"UPDATE sentences_table_new SET label = {sentence_tuple[2]} WHERE sentence_id = {sentence_tuple[0]}"

        self.cursor.execute(update)

        self.mydb.commit()

    