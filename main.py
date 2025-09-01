from stats import count_words
from stats import count_occurrence

def get_books_test(path):
    filecontents = ""
    with open(path) as f:
        filecontents = f.read()
    return filecontents

def main():
    text = get_books_test("books/frankenstein.txt")
    num = count_words(text)
    chars = count_occurrence(text)
    print(f"{num} words found in the document")
    print(f"{chars}")

main()