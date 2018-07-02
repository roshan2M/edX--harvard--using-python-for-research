from TextAnalyzer import count_words

ROMEO_AND_JULIET_ENGLISH_PATH = "./Books/English/shakespeare/Romeo and Juliet.txt"
ROMEO_AND_JULIET_GERMAN_PATH = "./Books/German/shakespeare/Romeo und Julia.txt"

def read_book(title_path: str) -> str:
    """
    Read a book and return it as a string.
    """
    with open(title_path, "r", encoding="utf8") as current_book:
        text = current_book.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

def word_statistics(word_counts: dict):
    """
    Returns the number of unique words and the frequency of words in word_counts.
    """
    num_unique_words = len(word_counts)
    counts = word_counts.values()
    return (num_unique_words, counts)

def get_example_statistics():
    """
    Gets sample statistics for the book Romeo and Juliet in English and German.
    """
    romeo_and_juliet_en = read_book(ROMEO_AND_JULIET_ENGLISH_PATH)
    word_counts_en = count_words(romeo_and_juliet_en)
    (num_unique_en, counts_en) = word_statistics(word_counts_en)
    print(num_unique_en, sum(counts_en))

    romeo_and_juliet_de = read_book(ROMEO_AND_JULIET_GERMAN_PATH)
    word_counts_de = count_words(romeo_and_juliet_de)
    (num_unique_de, counts_de) = word_statistics(word_counts_de)
    print(num_unique_de, sum(counts_de))
