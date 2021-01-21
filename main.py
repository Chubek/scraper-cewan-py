from msql_db import MQLDB
import logging
import threading
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__":

    database = MQLDB(os.environ.get("MYSQL_USER"), os.environ.get("MYSQL_PASS"))

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
    for index, func in enumerate(functions):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=lambda x: x(), args=(func,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)
    
