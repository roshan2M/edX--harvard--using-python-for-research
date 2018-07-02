import os

from BookReader import read_book

BOOK_DIR = "./Books"

print(os.listdir(BOOK_DIR))

for LANGUAGE_DIR in os.listdir(BOOK_DIR):
    for AUTHOR_DIR in os.listdir(BOOK_DIR + "/" + LANGUAGE_DIR):
        for book_title in os.listdir(BOOK_DIR + "/" + LANGUAGE_DIR + "/" + AUTHOR_DIR):
            input_file = BOOK_DIR + "/" + LANGUAGE_DIR + "/" + AUTHOR_DIR + "/" + book_title
