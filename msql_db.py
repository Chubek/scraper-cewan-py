import mysql.connector 
import functools
import operator
from trigger import *

class MQLDB:

    def __init__(self, username, password):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user=username,
            password=password
        )

        self.cursor = self.mydb.cursor()        
        self.cursor.execute("SHOW DATABASES")
        print(not 'sentences' in [l[0] for l in self.cursor.fetchall()])
        if not 'sentences' in [l[0] for l in self.cursor.fetchall()]:
            self.cursor.execute("CREATE DATABASE sentences")
            self.cursor.execute("USE sentences")
            self.cursor.execute("CREATE TABLE sentences_table (sentence VARCHAR(2000), label VARCHAR(50))")
            self.mydb.commit()
        else:
            self.cursor.execute("USE sentences")
            self.mydb.commit()

    def __insert(self, articles):
        sql = "INSERT INTO sentences_table (sentence, label) VALUES (%s, %s)"

        vals = functools.reduce(operator.iconcat, [[(sentence, 'UNLABLED') for sentence in article[3].split(".") if sentence] for article in articles], [])

        self.cursor.executemany(sql, vals)
        self.mydb.commit()


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


    