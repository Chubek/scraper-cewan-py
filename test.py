from db import Database

database = Database("mongodb://chubak:4d4m4k_Dummy@localhost:27017/", "articles_db", "articles_coll")


print(database.insert_utd())