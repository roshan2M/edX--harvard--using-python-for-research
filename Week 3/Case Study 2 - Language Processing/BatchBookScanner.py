import os
import pandas as pd
import matplotlib.pyplot as plt

from BookReader import read_book, word_statistics
from TextAnalyzer import count_words

BOOK_DIR = "./Books"

def create_book_dataframe() -> pd.DataFrame:
    """
    Creates and returns a pandas DataFrame to store all the books listed under the
    book directory.
    """
    book_stats = pd.DataFrame(columns = ("Language", "Author", "Title", "Length", "Unique"))
    title_num = 1
    for LANGUAGE_DIR in os.listdir(BOOK_DIR):
        for AUTHOR_DIR in os.listdir(BOOK_DIR + "/" + LANGUAGE_DIR):
            for book_title in os.listdir(BOOK_DIR + "/" + LANGUAGE_DIR + "/" + AUTHOR_DIR):
                input_file = BOOK_DIR + "/" + LANGUAGE_DIR + "/" + AUTHOR_DIR + "/" + book_title
                book_text = read_book(input_file)
                (num_unique, counts) = word_statistics(count_words(book_text))
                book_stats.loc[title_num] = LANGUAGE_DIR, AUTHOR_DIR.capitalize(), book_title.replace(".txt", ""), sum(counts), num_unique
                title_num += 1
    return book_stats

def display_relationship_between_length_and_unique(data: pd.DataFrame) -> None:
    """
    Displays the relationship between length of the book in words and the unique
    number of words in the book, stratified by language.
    """
    plt.figure(figsize=(10,10))
    subset = data[data.Language == "English"]
    plt.loglog(subset.Length, subset.Unique, "o", label="English", color="crimson")
    subset = data[data.Language == "French"]
    plt.loglog(subset.Length, subset.Unique, "o", label="French", color="forestgreen")
    subset = data[data.Language == "German"]
    plt.loglog(subset.Length, subset.Unique, "o", label="German", color="orange")
    subset = data[data.Language == "Portugese"]
    plt.loglog(subset.Length, subset.Unique, "o", label="Portugese", color="blueviolet")
    plt.legend()
    plt.title("Graph to Show the Length of a Book to the Number of Unique Words, Stratified by Language")
    plt.xlabel("Logarithmic Book Length (words)")
    plt.ylabel("Logarithmic Number of Unique Words (words)")
    plt.savefig("Language Plot.pdf")

book_stats = create_book_dataframe()
display_relationship_between_length_and_unique(book_stats)
