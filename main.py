from db import Database
import logging
import threading

if __name__ == "__main__":

    database = Database("mongodb://chubak:4d4m4k_Dummy@localhost:27017/", "articles_db", "articles_coll")

    functions = [database.insert_abc, 
                        database.insert_bbc,
                        database.insert_cbs, 
                        database.insert_cnn, 
                        database.insert_fox, 
                        database.insert_utd, 
                        database.insert_nbc]

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = list()
    for func in functions:
        logging.info("Main    : create and start thread %d.", str(func))
        x = threading.Thread(target=lambda x: x(), args=(func,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)
    
