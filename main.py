from msql_db import MQLDB
import logging
import threading
from dotenv import load_dotenv
import os
import sys

load_dotenv()

if __name__ == "__main__":
    
    scrape = sys.argv[1] == "scrape"
    label = sys.argv[1] == "label"

    if scrape:
        database = MQLDB(os.environ.get("MYSQL_USER"), os.environ.get("MYSQL_PASS"), os.environ.get("MYSQL_SERVER"))

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

    elif label:
        database = MQLDB(os.environ.get("MYSQL_REMOTE_USER"), os.environ.get("MYSQL_REMOTE_PASS"), os.environ.get("MYSQL_REMOTE_SERVER"))

        print("Getting 50 random unlabled sentences...")
        database.select_rand()

        cancel = None
        i = 1
        while cancel.strip() != "c":
            random_sentence = ()
            try:
                print(f"Getting sentence {i}")
                random_sentence = database.return_sample_sentence()
            except Exception:
                print("Max Sentences reached...")
                cancel = "c"

            print(f"Sentence is {random_sentence[1]}\n 0. SKIP AND MARK USELESS\n1. Negativ\n2. Positive 3. Neutral\n Press any of these keys, be precise!")
            l = input()
            label = lambda x: {"0": "USLESS", "1": "NEG", "2": "POS", "3": "NEU"}[x](l.strip())
            print(f"You selected {label}... Inserting")
            database.label_sample_sentence((random_sentence[0], random_sentence[1], label))
            i += 1
            cancel = input("Done! Press Enter to continue! Press lowercase c to cancel...")