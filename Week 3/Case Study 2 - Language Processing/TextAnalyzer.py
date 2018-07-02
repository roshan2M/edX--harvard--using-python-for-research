from collections import Counter

def remove_auxiliary(text: str) -> str:
    """
    Skips all the auxiliary characters in text and returns the lowercase string.
    """
    skips = [".", ",", ";", ":", "'", '"', "\n", "\r"]
    for s in skips:
        text = text.replace(s, "")
    return text.lower()

def count_words(text: str) -> dict:
    """
    Creates a dictionary mapping a word to the number of times it has occurred
    in the string. Removes all auxiliary characters and counts the lowercase
    string only.
    """
    word_count = Counter(remove_auxiliary(text).split(" "))
    return word_count
